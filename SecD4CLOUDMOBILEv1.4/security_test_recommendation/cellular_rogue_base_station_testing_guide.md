
# Security Testing Setup for Cellular Rogue Base Station Attacks


## 1. Overview

**Objective**: Emulate, detect, measure impact of, and harden against rogue base station attacks that perform one or more of the following:

* Intercept or collect identifiers (IMSI/IMEI), downgrade security (force weaker ciphering), perform man-in-the-middle (MITM) for signaling or data, or perform denial-of-service (force detach/connection rejection). Test detection and mitigation across device (Android/iOS), network (local eNodeB/gNB), and cloud (backend services that rely on mobile telemetry).

---

## 2. Required Lab & Equipment 

* **Shielded RF test environment** (Faraday cage) or written regulatory permission for test frequencies. 
* **Software-Defined Radios (SDRs)** (for research-grade control): USRP family (Ettus), bladeRF, HackRF One (for low-power RX/TX in shielded lab). 
* **Software base station stacks** (for setting up test BTS/eNodeB/gNB): srsRAN (srsLTE), YateBTS, OpenAirInterface, OpenBTS.
* **GSM/LTE analysis / sniffing tools**: gr-gsm / Airprobe (GSM), Wireshark (S1/RRC decode where possible), mobile logs (adb/logcat / iOS sysdiagnose). 
* **IMSI-catcher & detector apps** (lab verification & detection): AIMSICD, SnoopSnitch, and other detector toolkits for ground truth comparison (note: these apps have limitations). 

---

## 3. High-level Testing Categories 

1. **Rogue BTS setup & configuration** &mdash; create controlled BTS (2G/3G/4G) and configure to accept test UEs.
2. **IMSI/IMEI harvesting & identity requests** &mdash; test whether your test stack can request subscriber identity, force null-ciphering, or request silent SMS. 
3. **Security downgrades & cipher forcing** &mdash; test if the UE falls back to unencrypted or weaker crypto modes. 
4. **MITM / data interception** &mdash; where lawful/contained: validate if signaling user plane can be intercepted in lab and whether applications leak sensitive data. 
5. **Detection validation** &mdash; run IMSI-catcher detector apps and compare to ground truth from the test BTS (assess false negatives / bypass approaches).
6. **Cloud/service impact** &mdash; measure mobile app behavior, telemetry loss, backend connection anomalies, and forensic traces in cloud logs.
7. **Mitigation testing** &mdash; evaluate UE hardening, operator-side mitigations, and detection rules.

---

## 3. Stepwise Testing Playbook 

Phase 0 &mdash; plan & authorize

* Written authorization (scope, time, frequencies), pre-registered test plan, emergency rollback. 

Phase 1 &mdash; baseline & instrumentation

* Deploy a test base station (YateBTS / srsRAN) inside a Faraday cage; attach test UEs (spare phones/emulators). Collect baseline KPIs and logs (UE radio logs, Wireshark S1/RRC traces, SDR IQ). 

Phase 2 &mdash; passive observation / recon

* Use gr-gsm, Airprobe, and SDR RX (RTL-SDR / HackRF) to passively observe neighbor cells and signaling. Record broadcasts (MIB/SIB/PBCH) for comparison. 

Phase 3 &mdash; controlled rogue configuration (lab only)

* Configure test BTS to advertise stronger RSSI and accept registration from UEs; test identity request messages and null-ciphering scenarios. Log all signaling and compare to expected behaviour. **Never** do this outside shielded/test bands.

Phase 4 &mdash; active tests & attack variants (incremental)

* Basic IMSI collection (simulated), null ciphering, silent SMS, downgrade attempts.
* Protocol quirks: test disguised/mimicked real cell parameters to evaluate detector bypass (see White-Stingray evaluation).

Phase 5 &mdash; detection instrumentation & validation

* Run AIMSICD and SnoopSnitch on UEs; compare app alerts against ground-truth logs from the test BTS (assess detection latency and blindspots).

Phase 6 &mdash; cloud & service effects

* Measure mobile app retry behavior, backend session churn, and SIEM alerts. Verify whether cloud logs contain sufficient telemetry for attribution.

Phase 7 &mdash; report & remediation

* Produce clearly reproducible test cases (SDR IQ files, base station configs, device logs), prioritized findings, and recommended mitigations (UE hardening, carrier detection, operator configuration changes).

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
      <td>Gray-box / Physical</td>
      <td>DAST</td>
      <td>Controlled rogue BTS / test eNodeB</td>
      <td>srsRAN (srsLTE)</td>
      <td><a href="https://www.srslte.com/" target="_blank" rel="noopener">srsRAN</a></td>
      <td>Both (Android, iOS; test UEs)</td>
    </tr>
    <tr>
      <td>Gray-box / Physical</td>
      <td>DAST</td>
      <td>Open BTS (GSM) testbed</td>
      <td>YateBTS / Yate</td>
      <td><a href="https://yatebts.com/" target="_blank" rel="noopener">YateBTS</a></td>
      <td>Both (legacy GSM & test UEs)</td>
    </tr>
    <tr>
      <td>Black-box / Recon</td>
      <td>DAST / Passive</td>
      <td>GSM/LTE sniffing & broadcast analysis</td>
      <td>gr-gsm / Airprobe</td>
      <td><a href="https://github.com/ptrkrysik/gr-gsm" target="_blank" rel="noopener">gr-gsm</a></td>
      <td>Both (passive SDR receive)</td>
    </tr>
    <tr>
      <td>Black-box / Physical</td>
      <td>DAST / RF</td>
      <td>SDR hardware for RX/TX (research & lab only)</td>
      <td>USRP (Ettus) / bladeRF / HackRF</td>
      <td><a href="https://www.ettus.com/" target="_blank" rel="noopener">USRP</a> / <a href="https://github.com/Nuand/bladeRF" target="_blank" rel="noopener">bladeRF</a> / <a href="https://greatscottgadgets.com/hackrf/one/" target="_blank" rel="noopener">HackRF</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Detection</td>
      <td>DAST / Endpoint</td>
      <td>IMSI-catcher detector apps (compare GT)</td>
      <td>AIMSICD / SnoopSnitch</td>
      <td><a href="https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector" target="_blank" rel="noopener">AIMSICD</a> / <a href="https://play.google.com/store/apps/details?id=de.srlabs.snoopsnitch" target="_blank" rel="noopener">SnoopSnitch</a></td>
      <td>Android</td>
    </tr>
    <tr>
      <td>White-box / Simulation</td>
      <td>SAST / Model</td>
      <td>Cell/UE protocol simulation (no TX)</td>
      <td>ns-3 / MATLAB / GNUradio</td>
      <td><a href="https://www.nsnam.org/" target="_blank" rel="noopener">ns-3</a> / <a href="https://www.gnuradio.org/" target="_blank" rel="noopener">GNUradio</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Network</td>
      <td>DAST / Traffic</td>
      <td>Control channel & signaling analysis</td>
      <td>Wireshark (LTE dissectors)</td>
      <td><a href="https://www.wireshark.org/" target="_blank" rel="noopener">Wireshark</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box / Research</td>
      <td>DAST / RF</td>
      <td>Research jamming / stealth techniques (lab only)</td>
      <td>JamRF / GNUradio flows (research repos)</td>
      <td><a href="https://github.com/tiiuae/jamrf" target="_blank" rel="noopener">JamRF</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box / Detection</td>
      <td>DAST / Analytics</td>
      <td>Signal-feature & ML detection (spectrogram/IQ)</td>
      <td>TensorFlow / PyTorch (custom ML)</td>
      <td><a href="https://www.tensorflow.org/" target="_blank" rel="noopener">TensorFlow</a> / <a href="https://pytorch.org/" target="_blank" rel="noopener">PyTorch</a></td>
      <td>Both</td>
    </tr>

  </tbody>
</table>


---

## 5. References

1. Park, S., Shaik, A., Borgaonkar, R., Martin, A., & Seifert, J. P. (2017). {White-Stingray}: Evaluating {IMSI} Catchers Detection Applications. In *11th USENIX workshop on Offensive Technologies* (WOOT 17).
2. Tucker, T., Bennett, N., Kotuliak, M., Erni, S., Capkun, S., Butler, K., & Traynor, P. (2025). Detecting IMSI-Catchers by Characterizing Identity Exposing Messages in Cellular Traffic. In *Proceedings of the ISOC Networking and Distributed Systems Security (NDSS) Symposium*. San Diego, CA, USA.
3. Saedi, M., Moore, A., Perry, P., Shojafar, M., Ullah, H., Synnott, J., ... & Herwono, I. (2020, June). Generation of realistic signal strength measurements for a 5G Rogue Base Station attack scenario. In *2020 IEEE Conference on Communications and Network Security (CNS)* (pp. 1-7). IEEE.
4. Shaik, A., Borgaonkar, R., Park, S., & Seifert, J. P. (2018, June). On the impact of rogue base stations in 4g/lte self organizing networks. In *Proceedings of the 11th ACM Conference on Security & Privacy in Wireless and Mobile Networks* (pp. 75-86).
5. Golde, N., Redon, K., & Borgaonkar, R. (2012, February). Weaponizing Femtocells: The Effect of Rogue Devices on Mobile Telecommunications. In *NDSS*.