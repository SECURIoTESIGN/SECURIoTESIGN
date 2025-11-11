# Physical Theft Attacks Model

**Physical Theft Attacks** involve the unlawful removal or possession of hardware assets—such as mobile devices, IoT sensors, edge nodes, or servers—resulting in potential access to sensitive data, credentials, or system control. These attacks bypass digital defenses by exploiting physical vulnerabilities in deployment environments.

- **Cloud**: Theft of edge servers, storage drives, or networking equipment.
- **Mobile**: Loss or theft of smartphones, tablets, or laptops containing personal and enterprise data.
- **IoT**: Removal of embedded devices, sensors, or actuators from smart environments.

---

## Attack Categories

| Category               | Description                                                                 | Target Ecosystem     |
|------------------------|-----------------------------------------------------------------------------|-----------------------|
| **Device Theft**        | Stealing mobile phones, laptops, or tablets                                 | Mobile, Cloud         |
| **Edge Node Theft**     | Removing fog or edge computing units from physical locations                | Cloud, IoT            |
| **Sensor/Actuator Theft**| Extracting IoT components from smart homes, factories, or vehicles         | IoT                   |
| **Storage Media Theft** | Stealing hard drives, USBs, or SD cards containing sensitive data           | All                   |
| **Insider Theft**       | Authorized personnel stealing devices or components                         | Cloud, Mobile         |

---

## Attack Mitigations

- **Full-Disk Encryption**: Protect data at rest on stolen devices.
- **Remote Wipe Capabilities**: Enable erasure of data post-theft.
- **Secure Boot & TPM**: Prevent unauthorized access to firmware and OS.
- **Physical Locks & Enclosures**: Use tamper-resistant mounts and cages.
- **Asset Tracking Systems**: GPS or RFID-based location monitoring.
- **Access Logging & Alerts**: Monitor physical access attempts and anomalies.
- **Personnel Screening & Training**: Reduce insider threats through awareness and accountability.

---

## DREAD Risk Assessment

| DREAD Component     | Definition                                                                 | Score (1–10) | Assessment |
|---------------------|----------------------------------------------------------------------------|--------------|------------|
| **Damage Potential**| Extent of harm caused to systems and users                                 | 9            | High       |
| **Reproducibility** | Ease with which the attack can be repeated                                 | 6            | Medium     |
| **Exploitability**  | Effort required to launch the attack                                       | 7            | High       |
| **Affected Users**  | Number of users or systems impacted                                        | 8            | High       |
| **Discoverability** | Likelihood of the attack being detected or noticed                         | 5            | Medium     |

**Overall Risk Score** = 35/50 = 7.2; **Rating:** High

---

## References

1. Soliman, S., Oudah, W., & Aljuhani, A. (2023). Deep learning-based intrusion detection approach for securing industrial Internet of Things. *Alexandria Engineering Journal*, 81, 371-383.
2. Sequeiros, J. B., Chimuco, F. T., Simões, T. M., Freire, M. M., & Inácio, P. R. (2024, April). An approach to attack modeling for the IoT: creating attack trees from system descriptions. In *International Conference on Advanced Information Networking and Applications* (pp. 424-436). Cham: Springer Nature Switzerland.
3. Straub, J. (2020, November). Modeling attack, defense and threat trees and the cyber kill chain, att&ck and stride frameworks as blackboard architecture networks. In *2020 IEEE International conference on smart cloud (SmartCloud)* (pp. 148-153). IEEE.

---

## Physical Theft Attack Tree Diagram



