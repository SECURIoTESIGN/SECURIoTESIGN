# Hardware Integrity Attack Model

## Definition

A **hardware integrity attack** targets the trustworthiness of physical components and firmware in cloud and mobile ecosystem or IoT systems. Attackers may insert malicious chips, alter firmware, exploit debug interfaces, or tamper with devices in the supply chain—ultimately compromising data integrity, device control, and cloud authentication.

---

## Attack Categories

* **Supply-chain insertion:** malicious implants or counterfeit components during manufacturing.
* **Firmware compromise:** unauthorized firmware flashing or persistent BIOS/BMC malware.
* **Rollback/Update abuse:** reintroducing vulnerable firmware to regain control.
* **Physical tampering:** JTAG, probing, or invasive modification of chips.
* **Side-channel/fault injection:** extracting secrets via power, EM, or timing analysis.
* **Hardware Trojan/Management controller compromise:** persistent backdoors and root-of-trust subversion.

---

## Mitigation

* **Hardware root-of-trust:** TPM, secure boot, and attestation.
* **Signed firmware and anti-rollback protections.**
* **Trusted supply chain:** vendor vetting, provenance records, and hardware attestation.
* **Physical security:** tamper detection, enclosure protection, and JTAG lockdown.
* **Cloud integration controls:** device identity verification before provisioning.
* **Continuous monitoring:** firmware hash validation, anomaly detection, and centralized alerts.

---

## DREAD Risk Assessment

| Factor           | Score | Justification                                                   |
| ---------------- | :---: | --------------------------------------------------------------- |
| Damage Potential |   9   | Could expose cryptographic keys or enable persistent backdoors. |
| Reproducibility  |   6   | Moderate—depends on sophistication of attack.                   |
| Exploitability   |   7   | Some devices expose easy entry points (unsigned OTA, debug).    |
| Affected Users   |   8   | Compromise of one component class affects many systems.         |
| Discoverability  |   6   | Physical or firmware trojans difficult to detect.               |

**Average DREAD = (9+6+7+8+6)/5 = 7.2**; Rating: **High Risk**.

---

## References

1. European Union Agency for Cybersecurity. (2022). *ENISA Threat Landscape for Supply Chain Attacks.* ENISA. [https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks](https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks)
2. National Institute of Standards and Technology. (2020). *NIST SP 800-193: Platform Firmware Resiliency Guidelines.* NIST. [https://doi.org/10.6028/NIST.SP.800-193](https://doi.org/10.6028/NIST.SP.800-193)
3. National Institute of Standards and Technology. (2018). *NIST SP 800-161: Supply Chain Risk Management Practices for Federal Information Systems and Organizations.* NIST. [https://doi.org/10.6028/NIST.SP.800-161](https://doi.org/10.6028/NIST.SP.800-161)
4. ETSI. (2019). *ETSI EN 303 645 V2.1.1 — Cyber Security for Consumer Internet of Things: Baseline Requirements.* ETSI. [https://www.etsi.org/standards](https://www.etsi.org/standards)
5. OWASP Foundation. (2023). *OWASP IoT Security Verification Standard (ISVS) & IoT Top 10.* [https://owasp.org/www-project-internet-of-things](https://owasp.org/www-project-internet-of-things)
6. GSM Association. (2021). *GSMA IoT Security Guidelines & Assessment Checklist.* GSMA. [https://www.gsma.com/security/iot-security-guidelines/](https://www.gsma.com/security/iot-security-guidelines/)

---

## Hardware Integrity Attack Tree 

