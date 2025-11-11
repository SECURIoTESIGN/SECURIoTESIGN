# Security Testing Setup for Node Jamming Attacks

## 1. Overview

Node jamming (broadband, narrowband, reactive, selective, protocol-specific) can cause denial-of-service, data loss, or force fallback to less-secure communication paths in IoT deployments. Testing should validate detection, containment and recovery across the whole stack &mdash; radio, gateway, mobile client, and cloud telemetry.

---

## 1. High-level Testing Workflow

1. **Scope & threat model** &mdash; list radio technologies in use (Wi-Fi, BLE, Zigbee, LoRa, NB-IoT, cellular), node types (sensors, gateways, mobile clients), and critical flows (telemetry, control, OTA updates).
2. **Baseline collection** &mdash; capture normal radio metrics and application behaviour: RSSI, packet loss, ETX, link quality, latency, heartbeats, node re-registration events.
3. **Passive monitoring & signature collection** &mdash; use passive receivers (RTL-SDR, spectrum analyzer) to collect spectrum occupancy and transient events; build baseline spectrograms/waterfalls.
4. **Controlled interference (lab only, with authorization)** &mdash; in RF-shielded/attenuated lab, run *controlled* jamming tests (broadband, narrowband, reactive, selective) against test nodes to measure impact (packet loss, node outage, failover). Use vendor or research SDR jamming toolchains &mdash; **do not** transmit outside shielded/authorized test environment.
5. **Observe system response** &mdash; evaluate node/fleet re-registration, gateway failover, cloud alerting, missed heartbeats, and mobile UX degradation. Measure detection latencies and false positives.
6. **Detection engineering** &mdash; test radio-level detectors (RSSI variance, sudden spectral occupancy, packet error bursts), MAC/PHY indicators, and higher-level counters (sudden heartbeats drop, multi-node correlated outage). Use ML/edge detection where appropriate.
7. **Mitigation & resilience tests** &mdash; validate channel hopping, frequency diversity, redundancy (multi-gateway), retransmission/backoff strategies, duty-cycle limits, and fallback to alternative links (cellular) while assessing security tradeoffs.
8. **Report & remediation** &mdash; produce prioritized findings (detection gaps, missing redundancy, weak telemetry) and recommend changes (antenna/site hardening, monitoring thresholds, firmware updates, operational playbooks).

---

## 2. Security Test Approaches & Tools


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
    <!-- Passive spectrum monitoring -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Spectrum monitoring & waterfall capture</td>
      <td>RTL-SDR (RTL2832U) + CubicSDR / GQRX</td>
      <td>https://www.rtl-sdr.com/</td>
      <td>Both (IoT/gateways/mobile radio bands)</td>
    </tr>
    <!-- Research/precise jamming (lab only) -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Controlled RF interference (research SDR)</td>
      <td>HackRF One (SDR) + GNU Radio</td>
      <td>https://github.com/mossmann/hackrf , https://www.gnuradio.org/</td>
      <td>Both (lab)</td>
    </tr>
    <!-- High-precision professional SDR -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>High-power / multi-channel jamming (research lab)</td>
      <td>USRP (Ettus) + GNU Radio</td>
      <td>https://www.ettus.com/</td>
      <td>Both (lab)</td>
    </tr>
    <!-- RF spectrum analysis -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Precise RF characterization & power measurement</td>
      <td>Bench spectrum analyzer (Keysight / Rigol) / RF Explorer</td>
      <td>https://www.keysight.com/ , https://www.rigolna.com/ , https://www.rf-explorer.com/</td>
      <td>Both</td>
    </tr>
    <!-- Protocol-specific sniffers -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Protocol capture: Zigbee / Thread / BLE / LoRa</td>
      <td>Ubertooth (BLE), TI/CC debugger tools, Semtech/LoRa sniffers</td>
      <td>https://github.com/greatscottgadgets/ubertooth</td>
      <td>Both (per-protocol)</td>
    </tr>
    <!-- Network/tactical detection -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Packet & flow monitoring (network view of jamming effects)</td>
      <td>Zeek, Wireshark</td>
      <td>https://www.zeek.org/ , https://www.wireshark.org/</td>
      <td>Both</td>
    </tr>
    <!-- Edge detection (TinyML) -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Edge/Node jamming detection (TinyML/CSI)</td>
      <td>Edge ML frameworks (TensorFlow Lite) + CSI/PHY collectors</td>
      <td>https://www.tensorflow.org/lite</td>
      <td>IoT nodes / gateways</td>
    </tr>
    <!-- Fleet telemetry & SIEM -->
    <tr>
      <td>White-box</td>
      <td>SAST/DAST</td>
      <td>Cloud telemetry analysis & correlation</td>
      <td>Elastic Stack (ELK), Splunk</td>
      <td>https://www.elastic.co/elastic-stack/ , https://www.splunk.com/</td>
      <td>Both (cloud)</td>
    </tr>
    <!-- IoT testbed orchestration -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Automated testbed & scenario orchestration</td>
      <td>Custom testbed (Raspberry Pi, ESP32, LoRa nodes) + orchestration scripts</td>
      <td>&mdash; (custom)</td>
      <td>IoT</td>
    </tr>
    <!-- Regulatory / compliance scanning -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Equipment & site RF compliance & attenuation checks</td>
      <td>Attenuators, RF shielding chamber (anechoic)</td>
      <td>Vendor sites (Keysight, ETS-Lindgren)</td>
      <td>Lab</td>
    </tr>
  </tbody>
</table>

---

## 3. Practical Testbed & Minimal Component List

* **Isolated RF lab / attenuation**: anechoic chamber or RF shielding + high-quality attenuators to prevent uncontrolled emissions. Use only in authorized lab.
* **Passive receivers**: RTL-SDR for broad monitoring; RF Explorer or Keysight spectrum analyzer for measurements.
* **SDR transmitters (lab only)**: HackRF One (research), USRP for targeted experiments and reactive jamming emulation. (Use only inside shielded environment.) 
* **Protocol sniffers**: Ubertooth (BLE), TI packet sniffers, Semtech/LoRa sniffers for protocol-level capture. 
* **Node test fleet**: representative sensors (ESP32, nRF52, LoRa/LPWAN nodes), gateways, and test mobile devices (Android phones) to observe UX effects.
* **Network capture & telemetry**: Zeek/Wireshark, ELK or Splunk to correlate node outages, increased retransmits, and missing telemetry. 
* **Edge detection**: small ML models on gateways or nodes (TinyML) using features like RSSI variance, packet error rates, Channel State Information (CSI) where available.

---

## 4. References

1. Pirayesh, H., & Zeng, H. (2022). Jamming attacks and anti-jamming strategies in wireless networks: A comprehensive survey. *IEEE communications surveys & tutorials*, 24(2), 767-809. 
2. Yadav, A. M. P., & Gillingham, P. (2025, February). Poster: Evaluation of Radio Jamming Countermeasures in IoT Thread Networks. In *Network and Distributed System Security (NDSS) Symposium* (USA)(NDSS 2025).
3. Ali, A. S., Baddeley, M., Bariah, L., Lopez, M. A., Lunardi, W. T., Giacalone, J. P., & Muhaidat, S. (2022). Jamrf: performance analysis, evaluation, and implementation of rf jamming over wi-fi. *IEEE Access*, 10, 133370-133384.
4. Reynvoet, M., Gheibi, O., Quin, F., & Weyns, D. (2022, September). Detecting and mitigating jamming attacks in IoT networks using self-adaptation. In 2022 IEEE International *Conference on Autonomic Computing and Self-Organizing Systems Companion (ACSOS-C)* (pp. 7-12). IEEE. 
5. Šabić, J., Perković, T., Begušić, D., & Šolić, P. (2025). Practical Realization of Reactive Jamming Attack on Long-Range Wide-Area Network. Sensors, 25(8), 2383. 
6. Zahra, F. T., Bostanci, Y. S., & Soyturk, M. (2023). Real-time jamming detection in wireless IoT networks. *IEEE Access*, 11, 70425-70442. 
