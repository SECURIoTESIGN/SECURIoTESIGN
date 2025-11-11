# Security Testing for RFID Spoofing Attacks

## 1. Overview

RFID spoofing involves an attacker impersonating or emulating a legitimate RFID tag or reader to either gain unauthorized access, manipulate IoT devices, relay or replay tag data, or inject false telemetry. In a cloud-mobile-IoT environment, spoofed RFID tokens may grant unauthorized mobile/IoT device access, trigger unauthorized actions, or feed false telemetry into the cloud, compromising integrity. Research continues to show RFID spoofing is a viable threat, especially where reader logic is weak and backend analytics lack detection of token impersonation. Thus testing must span: tag/reader hardware, mobile apps (if reading tags), IoT gateways, cloud backend, and analytics.

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
      <td>DAST</td>
      <td>Tag spoofing / emulation (clone + modify UID/data)</td>
      <td>Proxmark3</td>
      <td><a href="https://en.wikipedia.org/wiki/Proxmark3">Proxmark3</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Tag emulation on mobile via HCE / Android NFC</td>
      <td>Android NFC HCE emulator + Android App</td>
      <td><a href="https://developer.android.com/guide/topics/connectivity/nfc/hce">Android NFC HCE emulator</a></td>
      <td>Android</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Reader firmware review &mdash; tag validation logic</td>
      <td>Ghidra / Binwalk</td>
      <td><a href="https://ghidra-sre.org/">Ghidra</a></td>
      <td>IoT reader/gateway</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud backend logic review &mdash; tag registration, uniqueness, spoof detection</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a></td>
      <td>Cloud</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Network monitoring &mdash; duplicate tag read detection, spoof detection logs</td>
      <td>Zeek / Wireshark</td>
      <td><a href="https://www.zeek.org/">Zeek</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Analytics/ML review for spoof detection (radio-fingerprint etc.)</td>
      <td>Python scikit-learn / RF fingerprint libs</td>
      <td><a href="https://scikit-learn.org/">scikit-learn</a></a></td>
      <td>Cloud/Edge</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical blank tag writing & injection into system</td>
      <td>Blank RFID tags + tag writer hardware</td>
      <td><a href="https://www.rfidcard.com/rfid-card-anti-spoofing-best-practices/">Blank RFID tags</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Testbed & Workflow

### Components & Setup

* **RFID infrastructure**: readers (IoT or mobile client), tags (legacy and encrypted), gateways to cloud backend that logs tag events.
* **Spoofing hardware**: Proxmark3, blank tags, HCE emulation on Android.
* **Monitoring**: Logging at reader/gateway, network capture (Zeek/Wireshark), cloud backend ingestion of tag read events with device/time/location metadata.
* **Review/analysis tools**: Firmware extraction for readers (Binwalk), mobile app instrumentation if tags used via mobile (MobSF/Frida), cloud backend code review (CodeQL/Semgrep), analytics platform for duplicate detection.

### Workflow

1. **Baseline operation** &mdash; record legitimate tag usage: tag IDs, reader IDs, timestamps, frequencies, asset mapping.
2. **Firmware/mobile review** &mdash; examine reader firmware and mobile app for tag validation logic, UID as sole identifier, absence of cryptographic challenge, hard-coded tag IDs.
3. **Cloud backend review** &mdash; verify logic enforces unique tag-ID reads, detects duplicate tag IDs across readers, tracks asset movement/locations, and includes revocation logic.
4. **Tag spoofing test** &mdash; use Proxmark3 to read a valid tag, then write blank tag or emulate using HCE on Android. Insert clone into reader/gateway system. Observe whether reader accepts clone, what logs are recorded, whether cloud flags duplicate usage.
5. **Tag emulation via mobile** &mdash; configure Android HCE app to emulate tag, present to reader; observe mobile/gateway/cloud response.
6. **Insert spoofed tag flows** &mdash; emulate asset readings by spoof tag at locations/multiple readers; monitor for unrealistic asset movement, duplicate tag IDs used at different readers/locations in short time.
7. **Network/analytics monitoring** &mdash; capture reader/gateway traffic, log tag read events, detect suspicious patterns: same tag ID read by multiple readers, short time between widely separated readers, blank tag IDs not registered. Use Zeek or logs.
8. **Analytics & fingerprinting** &mdash; optionally use RF-fingerprint (e.g., antenna/reader fingerprint) or ML on reading patterns to detect spoofed tags (research emerging).
9. **Remediation checks** &mdash; ensure system includes cryptographic tag authentication (challenge/response tags), asset tag registration and uniqueness verification, revocation workflows, anomaly detection logic. After this, retest to verify clones are blocked or flagged.
10. **Logging & reporting** &mdash; log tag IDs, clone times, detection timestamps; produce risk report: tag classes non-secure, readers accepting clones, backend lacks detection, mitigation path.

---

## 4. References

1. Zhao, W., Zhang, Y., & Wang, X. (2020). ACD: An Adaptable Approach for RFID Cloning Attack Detection. *Sensors*, 20(8), 2378. [https://doi.org/10.3390/s20082378](https://doi.org/10.3390/s20082378).
2. Feng, Y., Huang, W., Wang, S., Zhang, Y., Jiang, S., Cao, Z. (2022). Anti-Clone: A Lightweight Approach for RFID Cloning Attacks Detection. In: Gao, H., Wang, X., Wei, W., Dagiuklas, T. (eds) Collaborative Computing: Networking, Applications and Worksharing. CollaborateCom 2022. Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, vol 461. Springer, Cham. [https://doi.org/10.1007/978-3-031-24386-8_5](https://doi.org/10.1007/978-3-031-24386-8_5). 
3. Piva, M., Maselli, G., & Restuccia, F. (2021). The tags are alright: Robust large-scale RFID clone detection through federated data-augmented radio fingerprinting. In Proceedings of the Twenty-second International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing (pp. 41-50)[https://doi.org/10.1145/3466772.3467033](https://doi.org/10.1145/3466772.3467033).
4. MMehmood, A., Aman, W., Rahman, M. M. U., Imran, M. A., & Abbasi, Q. H. (2020). Preventing identity attacks in RFID backscatter communication systems: A physical-layer approach. In *2020 International Conference on UK-China Emerging Technologies (UCET)* (pp. 1-5). IEEE. [10.1109/UCET51115.2020.9205427](10.1109/UCET51115.2020.9205427).
