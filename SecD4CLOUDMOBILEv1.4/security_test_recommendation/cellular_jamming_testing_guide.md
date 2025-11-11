# Security Testing for Cellular Jamming Attacks

## 1. Overview

Assess detection, mitigation, and resilience of cloud/mobile/IoT deployments to *cellular jamming* (broadband/narrowband, reactive, protocol-aware/"smart" jammers) by combining: RF instrumentation (SDR), protocol-aware testbeds (srsRAN / OpenBTS / OpenAirInterface), spectrum monitoring, detection algorithms (RSSI/EVM/ML), and higher-layer resilience tests (service failover, handover, fallback to other RATs). Key goals: detect jamming quickly, measure outage area/effect, validate mitigations (frequency hopping, alternative paths, multi-SIM failover, redundant connectivity), and create actionable remediation & detection rules. 

---

## 2. Short Hardware & Software Prerequisites (lab)

* RF shielded environment (Faraday cage) or licensed test frequencies.
* SDRs for transmission/reception: **USRP B210 / N210 / X310 (Ettus)**, **HackRF One**, **LimeSDR**, **bladeRF**. (USRP recommended for research-grade TX control & power.) 
* Software stacks: **srsRAN (srsLTE / srsRAN)**, **OpenBTS / OpenAirInterface** for creating test eNodeB/gNB and UEs in lab. 
* RF analysis: GNURadio, SigDigger, rtl_power/rtl_sdr tools, Wireshark (for decoded S1 / RRC messages when available).
* Jamming test software (research implementations / proof-of-concept only): JamRF / GNUradio-based jammers (use only in shielded / authorized lab). 
* Detection & analytics: tools or code to measure RSSI/RSRP/RSRQ, BER, Packet Loss, and **EVM** per resource block (recent works show EVM→useful for detection). 

---

## 3. High-level Testing Phases / Workflow

1. **Design & authorization** &mdash; obtain written approvals and define test band, time, and containment (Faraday cage). Document rules of engagement. (Mandatory.) 
2. **Baseline collection** &mdash; measure normal KPI: RSRP/RSRQ/RSSI, throughput, packet loss, latency, and EVM; collect traces from target UEs, IoT nodes, and edge cloud services. Store seed corpus for later comparison.
3. **Instrumented test eNodeB / gNB setup** &mdash; deploy srsRAN/OpenAirInterface/OpenBTS to create controlled cell(s). Connect test UEs (real phones in lab or simulated UEs). 
4. **Jammer types & staging (lab-only)** &mdash; run controlled jammers in increasing scope:

   * *Narrowband constant tone* (single RB / single carrier).
   * *Wideband noise* (entire channel band).
   * *Reactive* (jam only when a packet is detected).
   * *Smart/targeted* (jam specific control channels such as PSS/SSS/PBCH or SIB/paging windows).
     Use SDR (USRP/HackRF) with prebuilt GNUradio flows or research code (JamRF, custom GNURadio).

5. **Detection experiments** &mdash; validate detection algorithms: RSSI thresholds, packet-level metrics, throughput/BER shifts, and **EVM-based** per-RB detection (EVM shown effective for LTE/5G jamming detection). Compare simple threshold methods vs ML classifiers trained on spectrograms/IQ or KPI features.
6. **Service-level impact & resilience** &mdash; measure mobile app behavior, IoT telemetry dropouts, cloud-side alarms, SIEM events; validate failover/retry, multi-SIM handover, or satellite fallback where applicable.
7. **Mitigation validation**&mdash; test frequency hopping-like countermoves in lab (if applicable), increased redundancy, edge caching, and detection &rarr; blacklisting of affected cells.
8. **Reporting & safe clean-up** &mdash; provide reproducible test manifests and remove any active jamming devices, verify network recovery.

---

## 3. Practical Testing Setup (playbook - safe lab only; condensed)

1. **Get approvals** &mdash; written authorization + reserved test frequency or Faraday cage. (Do not proceed without this.) 
2. **Deploy controlled cell** &mdash; run srsRAN eNodeB on isolated frequency, attach test UEs. Command examples (lab):

   * `sudo apt-get install srslte` then configure `enb.conf` and run `sudo srsepc` + `sudo srseNB` (see srsRAN docs).
    
3. **Baseline KPIs** &mdash; collect RSRP/RSRQ, throughput, and EVM via SDR receiver + UE logs. Save traces.
4. **Start jammer (very controlled)** &mdash; using USRP + GNURadio jamming flow (ensure power limits & containment): start with narrowband tone on a single RB; monitor network behavior; then stop. (Example GNURadio flow = JamRF / custom flow.)
5. **Detection evaluation** &mdash; run simple detectors (RSSI drop threshold) and EVM-per-RB detector (compare to baseline). Evaluate detection latency and false positives. 
6. **Service impact & mitigations** &mdash; measure app timeouts / message retransmit, IoT telemetry gaps, and test fallback (e.g., switch to alternate SIM or RAT) in controlled environment. Document parameters that trigger mitigation.
7. **Automation & reproducibility** &mdash; script the scenario (Ansible/Docker) including SDR flows, start/stop times, and capture all logs/PCAPs and SDR IQ recordings for offline analysis.

---

## 4. Security Testing Approaches & Tools


<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Test approach</th>
      <th>Analysis Type</th>
      <th>Approach name</th>
      <th>Testing Tool</th>
      <th>Tool Hyperlink</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Black-box</td>
      <td>DAST / Physical</td>
      <td>Hardware jamming (controlled, lab-only)</td>
      <td>USRP (Ettus Research)</td>
      <td><a href="https://www.ettus.com/" target="_blank" rel="noopener">USRP</a></td>
      <td>Both (affects Android/iOS/IoT)</td>
    </tr>
    <tr>
      <td>Black-box / Low-cost</td>
      <td>DAST / Physical</td>
      <td>Proof-of-concept jamming (narrow/wideband)</td>
      <td>HackRF One</td>
      <td><a href="https://greatscottgadgets.com/hackrf/" target="_blank" rel="noopener">HackRF One</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Emulation</td>
      <td>DAST / Protocol</td>
      <td>Controlled LTE/5G test eNodeB / gNB</td>
      <td>srsRAN (srsLTE / srsRAN)</td>
      <td><a href="https://www.srslte.com/" target="_blank" rel="noopener">srsRAN</a></td>
      <td>Both (test UEs + IoT modems)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Protocol</td>
      <td>Open-source mobile network testbeds</td>
      <td>OpenAirInterface / OpenBTS</td>
      <td><a href="https://openairinterface.org/" target="_blank" rel="noopener">OpenAirInterface</a> / <a href="https://openbts.org/" target="_blank" rel="noopener">OpenBTS</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box / Research</td>
      <td>DAST / RF</td>
      <td>SDR/flow-based jamming implementations</td>
      <td>JamRF (GNUradio flows)</td>
      <td><a href="https://github.com/tiiuae/jamrf" target="_blank" rel="noopener">hJamRF</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box / Passive</td>
      <td>DAST / Passive</td>
      <td>Spectrum reconnaissance & passive detection</td>
      <td>RTL-SDR + rtl_power / gr-gsm / SigDigger</td>
      <td><a href="https://osmocom.org/projects/rtl-sdr/wiki" target="_blank" rel="noopener">RTL-SDR</a> / <a href="https://github.com/hoogkamer/sigdigger" target="_blank" rel="noopener">SigDigger</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Detection</td>
      <td>DAST / Signal metrics</td>
      <td>EVM / KPI-based detection & analytics</td>
      <td>Custom EVM monitoring (MATLAB/Python) + SDR input</td>
      <td><a href="https://doi.org/10.3390/electronics12244948" target="_blank" rel="noopener">EVM method</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Network</td>
      <td>DAST / Traffic</td>
      <td>Service-level impact testing (app / IoT telemetry)</td>
      <td>Wireshark / PCAP analysis</td>
      <td><a href="https://www.wireshark.org/" target="_blank" rel="noopener">Wireshark</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box / Simulation</td>
      <td>SAST / Model</td>
      <td>RF & protocol simulation (no TX)</td>
      <td>NS-3 / MATLAB / GNUradio simulation</td>
      <td><a href="https://www.nsnam.org/" target="_blank" rel="noopener">NS-3</a> / <a href="https://www.gnuradio.org/" target="_blank" rel="noopener">GNUradio</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / ML</td>
      <td>DAST / ML detection</td>
      <td>Spectrogram / IQ ML detectors</td>
      <td>TensorFlow / PyTorch (custom models)</td>
      <td><a href="https://www.tensorflow.org/" target="_blank" rel="noopener">TensorFlow</a> / <a href="https://pytorch.org/" target="_blank" rel="noopener">PyTorch</a></td>
      <td>Both</td>
    </tr>

  </tbody>
</table>

---

# 5. References

1. Pirayesh, H., & Zeng, H. (2022). Jamming attacks and anti-jamming strategies in wireless networks: A comprehensive survey. *IEEE Communications Surveys & Tutorials*, 24(2), 767–809.  
2. Shaik, A., Borgaonkar, R., Asokan, N., Niemi, V., & Seifert, J.-P. (2016). Practical attacks against privacy and availability in 4G/LTE mobile communication systems. *NDSS*. 
3. Capota, C., Popescu, M., Badula, E. M., Halunga, S., Fratu, O., & Popescu, M. (2023). Intelligent Jammer on Mobile Network LTE Technology: A Study Case in Bucharest.*Applied Sciences*, 13(22), 12286.
4. Örnek, C., & Kartal, M. (2023). Securing the Future: A resourceful jamming detection method utilizing the EVM metric for next-generation communication systems. *Electronics*, 12(24), 4948. 
5. Ali, A. S., Baddeley, M., Bariah, L., Lopez, M. A., Lunardi, W. T., Giacalone, J. P., & Muhaidat, S. (2022). Jamrf: performance analysis, evaluation, and implementation of rf jamming over wi-fi. *IEEE Access*, 10, 133370-133384. 
6. Lichtman, M., Jover, R. P., Labib, M., Rao, R., Marojevic, V., & Reed, J. H. (2016). LTE/LTE-A jamming, spoofing, and sniffing: threat assessment and mitigation. *IEEE Communications Magazine*, 54(4), 54-61. 