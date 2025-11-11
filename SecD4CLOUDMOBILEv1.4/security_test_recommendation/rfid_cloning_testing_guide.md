# Security Testing for RFID Cloning Attacks


## 1. Overview

In IoT/edge/mobile deployments, RFID tags/cards are often used for device authentication, access control, asset tracking, mobile wallets, or RFID-enabled IoT nodes. A successful clone attack (where an attacker duplicates a valid tag and uses it in place of the genuine one) allows unauthorized access, impersonation of devices/nodes, or fraudulent asset transactions. Research shows RFID cloning remains a serious risk, even in large-scale systems.
Because such tags link into cloud/mobile/IoT flows (e.g., mobile apps reading tags, gateways verifying tags, cloud back-end logging tag events), testing must cover all layers: the RFID system itself, mobile apps/firmware, gateways, cloud backend and telemetry/analytics.

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
      <td>RFID tag sniffing & cloning</td>
      <td>Proxmark3</td>
      <td><a href="https://en.wikipedia.org/wiki/Proxmark3">Proxmark3</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Tag emulation & replay into system</td>
      <td>Flipper Zero / clone cards</td>
      <td><a href="https://flipperzero.one/">Flipper Zero</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Firmware/app review for RFID reader logic & trust model</td>
      <td>Ghidra / Binwalk</td>
      <td><a href="https://ghidra-sre.org/">Ghidra</a></td>
      <td>IoT device/mobile/gateway</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud backend review for tag registration, duplicate detection & revocation logic</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Cloud</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Network monitoring &mdash; tag interaction logs, anomalies, duplicate tag usage</td>
      <td>Zeek / Wireshark</td>
      <td><a href="https://www.zeek.org/">Zeek</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Tag authenticity & clone detection logic review</td>
      <td>Scripts implementing spatio-temporal detection (e.g., ACD) using COTS readers</td>
      <td><a href="https://doi.org/10.3390/s20082378">ACD</a></td>
      <td>IoT system</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical tag tamper/clone & insertion into live flow</td>
      <td>Blank RFID tags + clone writer devices</td>
      <td><a href="https://www.rfidcard.com/rfid-card-anti-cloning-best-practices-and-tool-recommendations/">Blank RFID tags</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Testbed & Workflow

**Components / Setup:**

* RFID infrastructure: tags, readers, gateway/edge device connected to cloud, mobile apps reading tags (if used).
* Logging pipeline: reader logs, gateway logs, cloud ingestion of tag reads, asset/tracking database.
* Clone‐capable hardware: e.g., Proxmark3, Flipper Zero or equivalent.
* Monitoring/analytics: network capture at gateway, duplicate use detection, anomaly dashboards.
* Review tools: firmware/image extraction for reader/gateway, cloud backend code review tools.

**Step-by-Step Workflow:**

1. **Baseline** &mdash; operate system normally: record tag readings, timestamps, asset movements, duplicate tag usage (should be none).
2. **Firmware/App review** &mdash; inspect reader/gateway firmware for trust model (does it accept any tag UID, allow registration, log duplicates), inspect mobile app if it reads tags.
3. **Cloud backend review** &mdash; check for logic handling duplicate tag IDs, tag‐revocation, logging of tag usage from multiple places, duplicate detection.
4. **Cloning** &mdash; Use Proxmark3: sniff a genuine tag in situ, attempt to duplicate it onto blank tag, or emulate it. Insert the cloned tag into system (mobile/IoT/gateway) as if genuine.
5. **Replay / tag injection** &mdash; Use clone to trigger reader as genuine. Observe system: does reader/gateway accept? Are there duplicate detections (same tag ID used concurrently)?
6. **Analytics detection** &mdash; Monitor logs for anomalies: same tag ID seen from two locations, improbable movements, unexpected read frequency, new asset ID not in inventory. Use Zeek/Wireshark or cloud analytics.
7. **Spatio-temporal clone detection** &mdash; Use tag movement logs to detect if same tag ID appears at distant readers in unrealistic time intervals (based on ACD method).
8. **Remediation testing** &mdash; After implementing mitigations (e.g., tag uniqueness checks, two‐factor verification, asset movement constraints), retest — ensure clone is blocked or flagged.
9. **Mobile/IoT integration** &mdash; For mobile apps reading RFID (or IoT nodes using RFID tokens), test what happens when a cloned token is presented: does app allow operations? Are cloud services updated?
10. **Reporting** &mdash; Document: which tags were clonable, time to clone, which readers/gateway accepted clones, what logs triggered (or didn’t), mitigation results, risk rating and recommendations (e.g., PUF tags, active authentication, logging duplicate use, stronger credentials).

---

## 4. References

1. Zhao, W., Zhang, Y., & Wang, X. (2020). ACD: An Adaptable Approach for RFID Cloning Attack Detection. *Sensors*, 20(8), 2378. [https://doi.org/10.3390/s20082378](https://doi.org/10.3390/s20082378).
2. Feng, Y., Huang, W., Wang, S., Zhang, Y., Jiang, S., & Cao, Z. (2023). Anti-Clone: A Lightweight Approach for RFID Cloning Attacks Detection. In *Collaborative Computing: Networking, Applications and Worksharing (CollaborateCom 2022)*. Springer. [https://doi.org/10.1007/978-3-031-24386-8_5](https://doi.org/10.1007/978-3-031-24386-8_5).
3. Piva, M., Maselli, G., & Restuccia, F. (2021). **The tags are alright: Robust large-scale RFID clone detection through federated data-augmented radio fingerprinting**. In *Proceedings of the Twenty-second International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing* (pp. 41-50).
4. Mehmood, A., Aman, W., Rahman, M. M. U., Imran, M. A., & Abbasi, Q. H. (2020). **Preventing identity attacks in RFID backscatter communication systems: A physical-layer approach**. In *2020 International Conference on UK-China Emerging Technologies (UCET)* (pp. 1-5). IEEE.