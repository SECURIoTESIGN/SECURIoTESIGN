# Security Testing for GPS Jamming Attacks

## 1. Overview

GPS jamming is interference that denies PNT (position, navigation, timing) and is detected using power/AGC/C/N0 monitoring, correlation/quality metrics, multi-antenna and multi-constellation methods, and ML models &mdash; testing requires RF hardware (SDR/USRP/HackRF), controlled test ranges (Faraday/isolated), and careful legal authorisation.

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
    <tr>
      <td>Black-box</td>
      <td>DAST (RF)</td>
      <td>Broadband / narrowband RF jamming (PHY-level)</td>
      <td>USRP B200/B210, HackRF</td>
      <td><a href="https://www.ettus.com">Ettus USRP</a>, <a href="https://greatscottgadgets.com/hackrf/">HackRF</a></td>
      <td>Both (Android/iOS clients, IoT)</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST (RF)</td>
      <td>Signal generator + GPS-SDR-SIM based waveform jamming</td>
      <td>GPS-SDR-SIM + SDR transmit chain</td>
      <td><a href="https://github.com/osqzss/gps-sdr-sim">GPS-SDR-SIM</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Detection</td>
      <td>Reactive/triggered jamming & power sweep tests</td>
      <td>GNU Radio flowgraphs, sdrplay/USRP scripts</td>
      <td><a href="https://www.gnuradio.org">GNU Radio</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Network</td>
      <td>Measure device behaviour & time-sync degradation</td>
      <td>Android GPSLogger, iOS location logs, RTK/PPP receivers</td>
      <td>Android: <a href="https://play.google.com/store/apps/details?id=com.mendhak.gpslogger">GPSLogger</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / ML detection</td>
      <td>ML-based jamming detection (edge models)</td>
      <td>TensorFlow Lite, scikit-learn (feature extraction)</td>
      <td><a href="https://www.tensorflow.org/lite">TensorFlow Lite</a></td>
      <td>Both (edge IoT, Android)</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST / Config</td>
      <td>Firmware & application review for fallback handling</td>
      <td>Static code analysis (CodeQL), manual review</td>
      <td><a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST / Forensics</td>
      <td>Spectrum capture & logging</td>
      <td>RTL-SDR, spectrum analyzer, SigDigger</td>
      <td><a href="https://www.rtl-sdr.com">RTL-SDR</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Emulation</td>
      <td>Lab emulation & repeatable scenarios (drones, vehicles)</td>
      <td>Spirent / Orolia (if available) or SDR-based simulators</td>
      <td><a href="https://www.orolia.com">Orolia</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Short Testing Setup &mdash; Practical Steps

1. **Legal & safety first**

   * Obtain written authorization and local/regulatory clearance. Perform tests only in an RF-isolated enclosure (Faraday cage) or licensed test range. Jamming outside controlled environments is illegal and can disrupt critical services. 

2. **Hardware & software inventory**

   * SDR transmitter (USRP B200/B210 or HackRF), SDR RX (RTL-SDR or USRP), spectrum analyzer (if available).
   * GNSS simulation software: **GPS-SDR-SIM** or vendor simulators (Spirent/Orolia) for controlled signal generation.

3. **Baseline & instrumentation**

   * Deploy test targets: Android phones (multiple OS versions), iOS device(s), representative IoT GNSS modules (u-blox, MediaTek), and a reference high-quality GNSS receiver (RTK/PPP) to compare. Log: receiver NMEA, C/N0, AGC, number of satellites, fix type, PPS/timestamp stability, and application-level behaviour (e.g., navigation app route deviation). 

4. **Controlled jamming experiments** (start low power / short durations)

   * **Broadband noise jamming**: transmit wideband noise covering L1/L2 to observe loss of lock and C/N0 drop.
   * **Narrowband sweep**: sweep transmitter power/frequency and duty cycle to map susceptibility and receiver thresholds.
   * **Reactive jamming**: trigger interference only when device is tracking to simulate stealthy denial. Use GNU Radio to implement reactive flows. 

5. **Measurements & detection signals**

   * Monitor AGC, sudden jumps in received power, C/N0 reductions, satellite count changes, and GNSS receiver alarms. Collect SDR spectrum traces and NMEA logs for each run. These metrics are common for jamming detection.

6. **ML / feature-based detection prototypes**

   * Extract features (power spectral density, AGC trends, C/N0 time series, Doppler anomalies) and train a lightweight classifier (scikit-learn / TensorFlow Lite) to detect jamming vs. benign interference. Recent work shows ML+multimodal approaches can be highly effective. 

7. **Resilience & mitigation tests**

   * Test multi-constellation (GPS+GLONASS+Galileo), multi-frequency receivers and anti-jamming hardware (CRPA, antenna nulling) and evaluate improvement. Validate fallback behaviours for apps (e.g., use inertial sensors, Wi-Fi/GNSS fusion).

8. **Reporting & safe teardown**

   * For each test case record: test ID, equipment & power, duration, spectrum capture, NMEA logs, observed effects (loss of lock, time offset, position error), and suggested mitigations. Remove transmitter and verify environment returned to baseline.

---

## 4. Quick Checklist (priority tests)

* Can a low-power jammer cause loss of fix or position/time errors on consumer Android/iOS devices? (measure C/N0 and #SV).
* Threshold mapping: what TX power / duty cycle causes denial for each receiver? (do power sweep).
* Stealthy/reactive jamming: can short bursts timed to acquisition prevent reacquisition yet remain hard to detect? (use reactive SDR flows).
* Detection: does AGC/C/N0-based detection or ML classifier reliably flag jamming before service loss? (evaluate false positives).
* Mitigation effectiveness: quantify benefit from multi-constellation, multi-frequency, inertial/GNSS fusion or anti-jamming antennas.

---

## 5. References

1. Ghanbarzade, A., & Soleimani, H. (2025). GNSS/GPS spoofing and jamming identification using machine learning and deep learning. *arXiv preprint arXiv:2501.02352*.
2. Radoš, K., Brkić, M., & Begušić, D. (2024). Recent advances on jamming and spoofing detection in GNSS. *Sensors*, 24(13), 4210.
3. Khan, S. Z., Mohsin, M., & Iqbal, W. (2021). On GPS spoofing of aerial platforms: a review of threats, challenges, methodologies, and future research directions. *PeerJ Computer Science*, 7, e507.
4. Liu, S., Cheng, X., Yang, H., Shu, Y., Weng, X., Guo, P., ... & Yang, Y. (2021, January). Stars can tell: A robust method to defend against gps spoofing using off-the-shelf chipset. In *Proceedings of The 30th USENIX Security Symposium (USENIX Security)*.
5. Abhishek, A. N., Balaji, A., Avinash, D., Harish, D., & Santhameena, S. (2025, March). Evaluating GNSS Spoofing and Jamming Attacks on UAV Navigation: Implementation and Impact. In *2025 IEEE 14th International Conference on Communication Systems and Network Technologies (CSNT)* (pp. 540-546). IEEE.
6. Ahmad, M., Farid, M. A., Ahmed, S., Saeed, K., Asharf, M., & Akhtar, U. (2019, January). Impact and detection of GPS spoofing and countermeasures against spoofing. In *2019 2nd International Conference on Computing, Mathematics and Engineering Technologies (iCoMET)* (pp. 1-8). IEEE.
