# Security Testing for RFID Unauthorized-Access Attacks

## 1. Overview

RFID unauthorized-access attacks occur when attackers use RFID-related techniques (skimming, relay, cloning, spoofing, brute-forcing weak tag keys, replay, or unauthorized reader access) to gain entry to systems or services that trust RFID tokens for authentication/authorization. In a cloud-mobile-IoT ecosystem these tokens often gate device access, authorize maintenance actions, or trigger cloud workflows &mdash; so stolen/forged tokens can yield unauthorized physical access, device control, or fraudulent cloud activity.

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
    <!-- Tag read / skimming -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Tag skimming / eavesdropping</td>
      <td>Proxmark3</td>
      <td><a href="https://github.com/Proxmark/proxmark3">Proxmark3</a></td>
      <td>Both</td>
    </tr>
    <!-- Cloning / writing -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Tag cloning & emulation</td>
      <td>Proxmark3, Flipper Zero, blank RFID tags</td>
      <td><a href="https://flipperzero.one/">Flipper Zero</a></td>
      <td>Both</td>
    </tr>
    <!-- MIFARE classic key recovery -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Weak-key brute force / MFA Classic cracking</td>
      <td>mfoc / mfcuk / libnfc</td>
      <td><a href="https://github.com/nfc-tools/mfoc">mfoc</a></td>
      <td>Both</td>
    </tr>
    <!-- Relay & long-range relay -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Relay attack / long-range relay</td>
      <td>NFCGate / two-device relay setups</td>
      <td><a href="https://github.com/SMKLab/NFCGate">NFCGate</a></td>
      <td>Android (HCE), Both</td>
    </tr>
    <!-- Reader firmware review -->
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Reader/gateway firmware & logic review</td>
      <td>Binwalk, Ghidra</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a></td>
      <td>IoT reader/gateway</td>
    </tr>
    <!-- Mobile app / HCE testing -->
    <tr>
      <td>Gray-box</td>
      <td>DAST / SAST</td>
      <td>Mobile HCE emulation & app network validation</td>
      <td>Android HCE emulator, MobSF, Frida</td>
      <td><a href="https://developer.android.com/guide/topics/connectivity/nfc/hce">Android HCE emulator</a></td>
      <td>Android, iOS</td>
    </tr>
    <!-- Network & backend correlation -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Cloud backend logic & duplicate-use detection</td>
      <td>Semgrep, CodeQL, Elastic (ELK) / Splunk for analytics</td>
      <td><a href="https://semgrep.dev/">Semgrep</a></td>
      <td>Cloud</td>
    </tr>
    <!-- Protocol & RF fingerprinting research -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>RF fingerprint / radio-based anti-spoof detection experiments</td>
      <td>SDR (USRP/HackRF), RF fingerprint libraries / Python</td>
      <td><a href="https://www.ettus.com/">DR (USRP/HackRF)</a></td>
      <td>Both</td>
    </tr>
    <!-- Traffic capture -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Traffic capture and analysis</td>
      <td>Wireshark, Zeek</td>
      <td><a href="https://www.wireshark.org/">Wireshark</a></td>
      <td>Both</td>
    </tr>
    <!-- Physical security review -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Physical access & tamper review of tag issuance/storage</td>
      <td>Physical audit checklist, asset tracking tools</td>
      <td>&mdash; (organizational)</td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Testing Setup &mdash; lab Checklist & Safe Practices

**Legal & safety first**

* Do **not** perform RFID attacks on production systems or in public spaces. Always run tests inside an isolated lab or fully authorized staging network, with written approval from asset owners and compliance/legal teams. RFID skimming/cloning in the wild is unlawful in many jurisdictions.

**Minimum lab components**

* Representative tags used in production (test duplicates where possible).
* Readers and gateways configured like production, but on isolated VLAN.
* Proxmark3 (or equivalent) and Flipper Zero for sniff/clone/emulate.
* SDR (optional) for radio-fingerprint experiments or specialized attacks.
* Blank programmable RFID tags/cards for tests.
* Mobile test devices (Android with HCE capabilities; optional iOS depending on needs).
* PC with libnfc, mfoc, mfcuk, nfcpy installed for tag tools.
* Network monitoring: Zeek/Wireshark; central logging (Elastic / Splunk).
* Firmware analysis tooling: Binwalk, Ghidra.
* Cloud testbed: staging backend with same validation logic, logging and analytics.

---

## 4. Step-by-step Workflow

1. **Inventory & baseline**

   * Record tag types (MIFARE Classic, DESFire, ISO15693, low-freq tags), reader models, tag issuance practices, cloud flows triggered by tag reads.
   * Capture normal tag read logs, read rates, typical reader locations and asset movement baselines.

2. **Passive eavesdrop / skimming**

   * Use Proxmark3 to sniff a legitimate tag read (in lab). Capture raw frames/APDUs. Determine if any unique dynamic/auth fields exist or if reads are static UIDs.

3. **Cloning / writing**

   * Try writing captured data to a blank tag or emulate via HCE: test whether the system accepts the clone as valid. For MIFARE Classic attempt mfoc to recover keys if allowed.
   * Record time needed to clone and any reader responses.

4. **Relay attack (relay & long-range relay)**

   * Set up two devices: one near the genuine tag, one near the reader; tunnel frames in real time (NFCGate) to simulate remote unauthorized access. Observe whether readers accept proxied tags.

5. **Brute force / weak key attacks**

   * For weak tag families (e.g., MIFARE Classic), run mfoc/mfcuk to recover keys and test unauthorized access to sectors.

6. **Reader & firmware review**

   * Extract firmware from reader/gateway (if allowed) using Binwalk and examine acceptance logic: does the reader accept any UID? Are there whitelist checks? How is reader ↔ cloud authentication performed?

7. **Mobile HCE tests**

   * Implement an Android HCE app to emulate tag responses; test whether mobile-emulated tags can be used to trigger workflows or gain access.

8. **Cloud correlation & detection**

   * Monitor backend logs for suspicious patterns: same tag reading at different readers at impossible times, sudden spike of a tag at different locations, or tag reads outside expected schedule.

9. **RF fingerprint & advanced detection (optional)**

   * Use SDR captures to compute radio-fingerprint features of a tag read (amplitude/phase characteristics) and test ML models that detect when the radio fingerprint of a presented tag differs from the recorded fingerprint for that UID.

10. **Remediation verification**

    * After applying mitigation controls (cryptographic tags, backend duplicate detection, time/location checks, multi-factor), re-run attack tests to verify they fail or raise alerts.

---

## 5. References 

1. Juels, A. (2006). RFID Security and Privacy: A Research Survey. *IEEE Journal of Selected Areas in Communications, 24(2), 381-394.[10.1109/JSAC.2005.861395](10.1109/JSAC.2005.861395).
2. Zhao, W., Zhang, Y., & Wang, X. (2020). ACD: An Adaptable Approach for RFID Cloning Attack Detection. *Sensors*, 20(8), 2378. [https://doi.org/10.3390/s20082378](https://doi.org/10.3390/s20082378).
3. Piva, M., Maselli, G., & Restuccia, F. (2021). The tags are alright: Robust large-scale RFID clone detection through federated data-augmented radio fingerprinting. In *Proceedings of the Twenty-second International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing* (pp. 41-50). [https://doi.org/10.1145/3466772.3467033](https://doi.org/10.1145/3466772.3467033). 
4. Mehmood, A., Aman, W., Rahman, M. M. U., Imran, M. A., & Abbasi, Q. H. (2020, August). Preventing identity attacks in RFID backscatter communication systems: A physical-layer approach. In *2020 International Conference on UK-China Emerging Technologies (UCET)* (pp. 1-5). IEEE. [10.1109/UCET51115.2020.9205427](10.1109/UCET51115.2020.9205427)
5. Mitrokotsa, A., Rieback, M. R., & Tanenbaum, A. S. (2010). Classifying RFID attacks and defenses. Information Systems Frontiers, 12(5), 491-505.[https://doi.org/10.1007/s10796-009-9210-z](https://doi.org/10.1007/s10796-009-9210-z).