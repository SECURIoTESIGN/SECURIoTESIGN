# Security Testing for Wi-Fi SSID-tracking Attacks

## 1. Overview

A VM Migration Attack exploits vulnerabilities during the transfer of virtual machines between hosts, while Wi-Fi SSID Tracking Attacks manipulate network identifiers to deceive devices &mdash; both demand rigorous security testing to prevent data breaches and service disruption. 

Why Security Testing Is Essential: 

* Proactive Defense: Detects vulnerabilities before attackers do;
* Compliance Assurance: Meets regulatory standards for data protection;
* Trust and Reliability: Ensures users and clients can rely on secure infrastructure.

---

## 1. Security Test Approaches & Tools

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
      <td>Passive sniffing (probe/beacon collection)</td>
      <td>Kismet, Wireshark, tcpdump</td>
      <td>
        <a href="https://www.kismetwireless.net/">Kismet</a>,
        <a href="https://www.wireshark.org">Wireshark</a>
      </td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST / Data</td>
      <td>Wardriving / geo-correlation (DB)</td>
      <td>WiGLE (app & DB), custom scripts</td>
      <td><a href="https://wigle.net">WiGLE</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box / Gray-box</td>
      <td>DAST</td>
      <td>Active elicitation / probe injection</td>
      <td>Scapy, Bettercap, aireplay-ng</td>
      <td>
        <a href="https://scapy.net">Scapy</a>,
        <a href="https://www.bettercap.org">Bettercap</a>,
        <a href="https://www.aircrack-ng.org">Aircrack-ng</a>
      </td>
      <td>Both (Linux); Android (rooted) for active tests</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / ML</td>
      <td>Probe-request fingerprinting / clustering</td>
      <td>Python (scapy, pandas), scikit-learn, timestamps</td>
      <td><a href="https://pypi.org/project/scapy">scapy</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Firmware/OS review (randomization logic)</td>
      <td>CodeQL, SonarQube, manual code review</td>
      <td><a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Simulated multi-collector wardrive</td>
      <td>Raspberry Pi + multiple Wi-Fi adapters, Kismet</td>
      <td><a href="https://www.kismetwireless.net/">Kismet</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST / Privacy</td>
      <td>Probe content analysis (SSIDs reveal PII)</td>
      <td>pcap → CSV parsers, grep, regex</td>
      <td>custom scripts (Python)</td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Detection</td>
      <td>Test OS privacy settings (MAC randomization)</td>
      <td>Android adb, iOS config profiles, device logs</td>
      <td><a href="https://developer.android.com/studio/command-line/adb">adb</a></td>
      <td>Android, iOS</td>
    </tr>
  </tbody>
</table>


---

## 2. Testing Setup &mdash; Step-by-step (practical)

**Legal / ethics first:** always get written permission for any active tests; for passive collection follow local privacy & data-protection rules and anonymise results. The literature treats probe requests as sensitive data because they often expose PII.

1. **Lab & hardware**

   * Linux laptop or Raspberry Pi with 1&mdash;3 external Wi-Fi adapters that support monitor mode (Atheros/realtek with good driver support).
   * Optional GPS for wardriving, and a small mobile (Android/iOS) testbed with devices of different OS versions.
   * Install Kismet + Wireshark + scapy + python data libs. 

2. **Baseline passive capture**

   * Put adapters in monitor mode and capture for a representative period (e.g., 30 min) in the target environment. Save pcaps and export CSV of: timestamp, source MAC, SSID (if present), RSSI, channel, and any IEs. Kismet can log GPS + time for wardriving. 

3. **Probe-content analysis**

   * Parse pcaps (scapy or tshark) and scan SSID fields for PII patterns (e.g., long numeric strings, email patterns, names, home router defaults). The 2022 field study found SSIDs leaking passwords and personal data in a notable fraction of probe requests.

4. **MAC randomization testing**

   * Measure randomization behaviour: record sequences of MACs and see when devices use global vs randomized MAC; test with MAC randomization toggled on/off in settings (where available). Prior studies show many devices still leak persistent identifiers or fail to randomize reliably.

5. **Fingerprinting & re-linking**

   * Extract frame features (IE fields, supported rates, sequence timing, probe burst timing, vendor IEs). Cluster traces using time-based and feature-based clustering to attempt to link multiple randomized MACs to one device. Use scikit-learn clustering (DBSCAN / hierarchical). Deep-learning approaches can also achieve high accuracy on 802.11ac IEs.

6. **Active elicitation (ONLY with permission)**

   * Use Scapy/Bettercap to send directed probe requests or elicit responses; measure whether devices respond with PNL contents or reveal hidden SSIDs. Active probing can increase identification but must be used only in lab or permitted environments.

7. **Wardriving / historical correlation**

   * (Optional) run a controlled wardrive (or simulate multiple collectors) and store geotagged SSID sightings. Query local copies of WiGLE or your dataset to attempt location-based linking and POI inference. Public databases enable powerful correlation attacks.

8. **Firmware / OS code review**

   * Where you control firmware or app code (IoT APs, vendor firmware, mobile app), review logic that constructs probe requests and PNL sharing. Check whether SSIDs are included inadvertently (e.g., when users paste SSIDs) and review randomization code.

9. **Mitigation validation**

   * Toggle and test mitigations: MAC randomization frequency, disable probe-requests in background scans, enable/verify 802.11w/management frame protections, test client behaviour when SSID privacy features are on/off. Re-run clustering experiments to quantify reduction in linkability. 

---

## 3. Artifacts to Collect (for each run)

* pcap (timestamped), CSV of observed frames (MAC, SSID, RSSI, IEs), GPS trace (wording: lat/lon/time), device setting snapshots (MAC randomization enabled?), device logs (if available), and scripts used for parsing/analysis.

---

## 4. Quick Checklist (priority tests)

* **Probe content leak:** any SSIDs containing PII (emails, apparent passwords, names)? 
* **MAC randomization effectiveness:** how often does it rotate and when does it fall back to global MAC? 
* **Re-linkability:** can you cluster randomized MACs by timing/IEs to get stable device IDs? 
* **Historical correlation:** can wardriving / WiGLE data deanonymize traces into locations/POIs? 
* **IoT exposures:** do IoT devices advertise default/unique SSIDs that identify device type/location? (check SSID formatting).

---

## 5. Mitigations to Test / Validate

* **Frequent MAC re-randomization** (session or scan-level) and ensure random MACs are not reused across contexts.
* **Omit probe SSID fields** unless user explicitly selects a network (OS level change). 
* **Avoid PII in SSIDs** (UI/UX sanitization and user education). 
* **Management-frame protection & reduced probe emission** (802.11w and OS scan throttling). 

---

## 6. References

1. Ansohn McDougall, J., Burkert, C., Demmler, D., Schwarz, M., Hubbe, V., & Federrath, H. (2022). Probing for passwords–privacy implications of ssids in probe requests. In International Conference on Applied Cryptography and Network Security (pp. 376-395). Cham: Springer International Publishing.
2. Martin, J., Mayberry, T., Donahue, C., Foppe, L., Brown, L., Riggins, C., ... & Brown, D. (2017). A study of MAC address randomization in mobile devices and when it fails. arXiv preprint arXiv:1703.02874.
3. Gu, X., Wu, W., Gu, X., Ling, Z., Yang, M., & Song, A. (2020). Probe request based device identification attack and defense. Sensors, 20(16), 4620.
4. Rye, E., & Levin, D. (2024). Surveilling the masses with wi-fi-based positioning systems. In 2024 IEEE Symposium on Security and Privacy (SP) (pp. 2831-2846). IEEE.
5. Thomas, A. M., Kumaran, G. A., Ramaguru, R., Harish, R., & Praveen, K. (2021). Evaluation of wireless access point security and best practices for mitigation. In 2021 5th International Conference on Electrical, Electronics, Communication, Computer Technologies and Optimization Techniques (ICEECCOT) (pp. 422-427). IEEE.