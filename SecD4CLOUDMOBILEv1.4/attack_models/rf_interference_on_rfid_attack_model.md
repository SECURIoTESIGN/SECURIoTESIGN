# RF Interference (Jamming) on RFID

## Definition

**RF interference (jamming) attacks** exploit intentional or unintentional radio noise to disrupt communication between RFID tags, readers, and connected cloud or mobile applications. Attackers emit continuous or reactive signals in the RFID frequency band (LF, HF, or UHF) to prevent tag detection, corrupt transmitted data, or exhaust system retries — leading to denial of service (DoS), inventory inaccuracies, and operational downtime in cloud-synced IoT systems.

---

## Attack Categories

* **Constant/Barrage Jamming:** Continuous emission of high-power RF noise across RFID bands, blocking all communication.
* **Reactive Jamming:** Transmits interference only when RFID activity is detected, making detection harder.
* **Selective/Protocol-Aware Jamming:** Targets control or ACK frames to disrupt specific operations while avoiding detection.
* **Reader Flooding:** Deploys multiple rogue readers to generate collisions and overwhelm the medium.
* **Directional/Localized Jamming:** Focused RF interference aimed at gates, POS terminals, or warehouse antennas.
* **Firmware-level Interference:** Compromised readers manipulate transmit power or suppress legitimate reads before cloud sync.

---

## Mitigation Strategies

**RF & Hardware Layer**

* Use **frequency hopping** or **multi-band readers** to bypass narrow-band jamming.
* Deploy **directional antennas** and **shielding** around sensitive zones.
* Apply **anti-collision algorithms** and dynamic power control.
* Employ **redundant readers** and spatial diversity to mitigate localized interference.

**Cloud & Application Layer**

* Integrate **telemetry monitoring** for read-rate anomalies, CRC errors, or rising RSSI noise floors.
* Use **edge buffering** and **delayed commit logic** to prevent data loss during temporary outages.
* Implement **multi-reader confirmation** before accepting inventory or transaction events.
* Record and analyze **RF performance metrics** in cloud dashboards for early anomaly detection.

**Operational Security**

* Train staff to recognize jamming symptoms and maintain incident playbooks.
* Perform periodic **RF spectrum audits** and **environmental scanning**.
* Secure reader firmware with **signed OTA updates** and **tamper-detection sensors**.
* Coordinate with regulators for **RF interference reporting and enforcement**.

---

## DREAD Risk Assessment

| DREAD Factor         | Score (0–10) | Rationale                                                                                             |
| -------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| **Damage Potential** | **7**        | Disrupts operations, inventory accuracy, and payment processing; can indirectly cause financial loss. |
| **Reproducibility**  | **9**        | Simple and cheap hardware (e.g., SDRs, RF generators) makes attacks highly reproducible.              |
| **Exploitability**   | **8**        | Low to moderate skill; off-the-shelf tools widely available.                                          |
| **Affected Users**   | **7**        | Impacts localized zones but may cascade to cloud data or mobile applications.                         |
| **Discoverability**  | **8**        | Easy to detect with spectrum tools, but reactive jammers remain stealthy.                             |

**Total:** 7 + 9 + 8 + 7 + 8 = **39**
**Average:** 39 ÷ 5 = **7.8 → High Risk**

---

## References

1. Karygiannis, T., Eydt, B., Barber, G., Bunn, L., & Phillips, T. (2007). *Guidelines for Securing Radio Frequency Identification (RFID) Systems (NIST SP 800-98).* National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.SP.800-98](https://doi.org/10.6028/NIST.SP.800-98)
2. Pirayesh, H., & Zeng, H. (2022). *Jamming attacks and anti-jamming strategies in wireless networks: A comprehensive survey.* IEEE Communications Surveys & Tutorials. [https://doi.org/10.1109/COMST.2022.3146176](https://doi.org/10.1109/COMST.2022.3146176)
3. Avanço, L., Guelfi, A. E., Pontes, E., Silva, A. A. A., Kofuji, S. T., & Zhou, F. (2015). *An effective intrusion detection approach for jamming attacks on RFID systems.* *Proceedings of the 2015 IEEE EURFID Conference*, 100–107. [https://doi.org/10.1109/EURFID.2015.7332388](https://doi.org/10.1109/EURFID.2015.7332388)
4. ENISA. (2020). *Baseline Security Recommendations for IoT.* European Union Agency for Cybersecurity. [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
5. ISO/IEC 18000-63. (2013). *Information technology — Radio frequency identification for item management — Part 63: Parameters for air interface communications at 860 MHz to 960 MHz.* International Organization for Standardization.

---


## RF Interference on RFIDs Attack Tree Diagram