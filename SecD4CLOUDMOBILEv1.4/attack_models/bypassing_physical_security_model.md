# Bypass Physical Security Attack Model

## Definition

**Bypass Physical Security Attacks** refer to techniques that circumvent physical barriers or controls—such as locks, sensors, or tamper-proof enclosures—to gain unauthorized access to systems, data, or infrastructure. In cloud, mobile, and IoT ecosystems, these attacks can lead to device tampering, data exfiltration, firmware manipulation, and service disruption.

- **Cloud**: Attacks on data centers, edge nodes, or network hardware.
- **Mobile**: Device theft, SIM swapping, or USB-based exploits.
- **IoT**: Tampering with sensors, embedded systems, or smart appliances.

---

## Attack Categories

| Category                 | Description                                                                 | Target Ecosystem     |
|--------------------------|-----------------------------------------------------------------------------|-----------------------|
| **Lock Picking & Access**| Exploiting mechanical or electronic locks                                   | Cloud, IoT            |
| **Tamper Bypass**        | Removing or disabling tamper-evident seals or sensors                       | IoT                   |
| **Side-Channel Access**  | Using electromagnetic, acoustic, or thermal emissions to extract data       | IoT, Mobile           |
| **Port Injection**       | Using USB, JTAG, or debug ports to inject malicious code                    | Mobile, IoT           |
| **Insider Threats**      | Authorized personnel abusing physical access privileges                     | Cloud, Mobile         |

---

## Attack Mitigations

- **Hardware Hardening**: Use tamper-resistant enclosures and epoxy shielding.
- **Secure Boot & Firmware Signing**: Prevent unauthorized firmware modifications.
- **Access Control Systems**: Biometric, RFID, and multi-factor authentication for physical entry.
- **Port Disablement**: Disable unused debug or USB ports at firmware level.
- **Environmental Monitoring**: Sensors for intrusion, temperature, and vibration anomalies.
- **Personnel Vetting & Training**: Reduce insider risks through background checks and awareness.

---

## DREAD Risk Assessment

| DREAD Component     | Definition                                                                 | Score (1–10) | Assessment |
|---------------------|----------------------------------------------------------------------------|--------------|------------|
| **Damage Potential**| Extent of harm caused to systems and users                                 | 9            | High       |
| **Reproducibility** | Ease with which the attack can be repeated                                 | 7            | High       |
| **Exploitability**  | Effort required to launch the attack                                       | 8            | High       |
| **Affected Users**  | Number of users or systems impacted                                        | 7            | High       |
| **Discoverability** | Likelihood of the attack being detected or noticed                         | 5            | Medium     |

**Overall Risk Score:** 36/5 = 7.2; Rating: **High**

---

## References

1. Wurm, J., Jin, Y., Liu, Y., Hu, S., Heffner, K., Rahman, F., & Tehranipoor, M. (2016). Introduction to cyber-physical system security: A cross-layer perspective. *IEEE Transactions on Multi-Scale Computing Systems*, 3(3), 215-227.
2. Skorobogatov, S. (2011). Physical attacks and tamper resistance. In *Introduction to Hardware Security and Trust* (pp. 143-173). New York, NY: Springer New York.
3. Islam, S. N., Baig, Z., & Zeadally, S. (2019). Physical layer security for the smart grid: Vulnerabilities, threats, and countermeasures. *IEEE Transactions on Industrial Informatics*, 15(12), 6522-6530.

---


## Bypass Physical Security Attack Tree Diagram
