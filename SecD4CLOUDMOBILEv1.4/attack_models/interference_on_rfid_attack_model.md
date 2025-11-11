# RF Interference on RFIDs Model

## 1) Definition

**RF interference / jamming against RFID** is the intentional or accidental transmission of radio energy that degrades, blocks or corrupts the RF link between RFID readers and tags, causing denial-of-service (failed reads), corrupted reads, extended read-times, or erroneous inventory/ID results. Interference for RFID can be malicious (jamming) or unintentional (EMC from other devices, collisions, adjacent-band emissions). ([NIST Publications][1])

---

## 2) Attack categories (RFID-specific + cloud/IoT context)

* **Constant (barrage) jamming:** continuous wideband or narrowband noise that overwhelms the reader/tag link (simple, low-skill). 
* **Reactive / deceptive jamming:** jammer transmits only when reader transmits to save energy and be harder to detect. 
* **Protocol-layer collision / reader flooding:** many rogue readers or repeat queries causing tag collisions and reader overload (logical DoS). ([NIST Publications][1])
* **Intentional EMI / in-band interference:** malicious transmitters tuned to RFID band (e.g., 13.56 MHz HF or 860–960 MHz UHF) or nearby devices spilling energy into RFID sub-band. ([NIST][2])
* **Covert low-power jamming / targeted directional jamming:** localized denial-of-service affecting specific gates/read zones (retail, access control). ([NIST][2])
* **Supply-chain or reader compromise amplified by RF interference:** a cloud-integrated fleet of readers with compromised firmware may be used to overload systems or mask attacks while false telemetry is sent to cloud services. (cloud linkage / escalation)

---

## 3) Mitigation & practical controls

**Reader & tag level**

* Use readers supporting robust modulation/detection, built-in interference detection and dynamic gain control.
* Configure transmit power, antenna polarisation and physical placement to minimise exposure to likely interferers.
* Use anti-collision protocols and adaptive read-frames (tuning slot lengths) to reduce collision impact.

**Physical / RF defenses**

* Shielding, RF absorbers, or Faraday barriers for high-value read zones (access gates, POS lanes).
* Directional antennas and spatial diversity (multiple antennas/readers) to reduce single-point failure by a jammer.
* Frequency diversity (where supported) or multi-band readers (HF + UHF) to allow fallback. 

**Detection & control**

* Implement local interference detection: monitor SNR, RSSI, sudden drop in tag responses, read-time distribution, and adjacent-channel energy. Trigger automated alarms and failover. ([ResearchGate][3])
* IDS for RFID readers (anomaly detectors that raise alerts before full DoS); deploy thresholds and early-warning detectors.

**System / cloud-level**

* Require signed reader firmware, secure update channels and device attestation to avoid reader compromise being used to hide jamming events.
* Add cloud-side analytics: correlate failed-read events, geo-cluster anomalies, and sudden inventory mismatches to detect regional RF incidents or malicious masking.
* Provide wired fallback paths for critical functions (e.g., access control fallback to local PIN or wired badge readers).

**Operational**

* Site surveys and EMC testing before deployment; keep an RF incident playbook (isolate affected readers, switch to alternate authentication modes, notify regulators/CERT).

---

## 4) DREAD Risk Assessment

> **Context:** public-facing RFID deployment (retail gates, access control, logistics) with cloud reporting and IoT-enabled readers.

|         DREAD factor | Score | Rationale (concise)                                                                                                                  |
| -------------------: | :---: | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Damage Potential** | **7** | Denies inventory/checkout or access control → revenue loss, operational disruption, safety risk in critical sites.                   |
|  **Reproducibility** | **9** | Jammers and interference devices are inexpensive and easy to reproduce; unintentional interference is common.                        |
|   **Exploitability** | **8** | Low skill required for simple jammers; reactive/stealth jammers need more sophistication but are feasible.                           |
|   **Affected Users** | **7** | Localized zones typically impacted (checkout lane, gate), but cloud aggregation or supply-chain tagging can amplify business impact. |
|  **Discoverability** | **8** | RF vulnerability is obvious (open antenna, public reader), and interference patterns are discoverable by simple monitoring.          |

**Digit-by-digit DREAD arithmetic (explicit):**
Sum = 7 + 9 + 8 + 7 + 8 = 39.
Average = 39 / 5 = 7.8.

**DREAD average = 7.8**; Rating: **High / Critical** (prioritise detection, physical hardening and fallback procedures).

---

## References
1. Karygiannis, T., Eydt, B., Barber, G., Bunn, L., & Phillips, T. (2007). *Guidelines for securing Radio Frequency Identification (RFID) systems* (NIST Special Publication 800-98). National Institute of Standards and Technology. [https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf).
2. Guerrieri, J. R., Novotny, D. R., Francis, M. H., & Remley, C. A. (2009). *Electromagnetic emissions and performance for proximity RFID*. National Institute of Standards and Technology / Conference proceedings. [https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=33143](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=33143).
3. Pirayesh, H., & Zeng, H. (2022). *Jamming attacks and anti-jamming strategies in wireless networks: A comprehensive survey*. *IEEE Communications Surveys & Tutorials*. [https://inss.egr.msu.edu/papers/Hossein22_COMST_jamming_survey.pdf](https://inss.egr.msu.edu/papers/Hossein22_COMST_jamming_survey.pdf). 
4. Avanço, L., Guelfi, A. E., Pontes, E., Silva, A. A. A., Kofuji, S. T., & Zhou, F. (2015). *An effective intrusion detection approach for jamming attacks on RFID systems* (Proc. EURFID 2015). DOI:10.1109/EURFID.2015.7332388.
5. ISO/IEC 14443. (2020). *Identification cards — Contactless integrated circuit cards — Proximity cards* (ISO/IEC standard). [https://www.iso.org/standard/77388.html](https://www.iso.org/standard/77388.html).

---

## RF Interference on RFIDs Attack Tree 