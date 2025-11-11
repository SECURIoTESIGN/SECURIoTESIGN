# Node Tampering Attack Model

## Definition

**Node tampering** is the physical or logical manipulation of an IoT/edge node (sensor, gateway, wearable, or embedded controller) to alter its behaviour, extract secrets, inject malicious firmware, or create a persistent backdoor into the device and its cloud ecosystem. Tampering includes opening enclosures, modifying connectors, attaching debug probes, replacing components, or using software-level tamper techniques after local compromise.

---

## Attack Categories

* **Physical tamper & implant:** opening device, soldering/modifying PCB, inserting hardware implants (malicious MCU/FPGAs) or interceptors that steal keys or alter telemetry.
* **Debug-interface abuse:** exploiting exposed JTAG/SWD/UART to read memory, dump keys, or flash malicious firmware.
* **Firmware/boot-chain replacement:** replacing/rewriting bootloader, BMC, or main firmware to introduce persistence that survives factory resets.
* **Firmware config/parameter tamper:** modifying configuration (Wi-Fi credentials, server endpoints) so device reports to attacker-controlled backends or discloses data.
* **Sensor spoofing / actuator manipulation:** physically altering sensors (magnet, light, vibration) or injecting signals so device reports false data or actuators are triggered incorrectly.
* **Side-channel / fault-induced tamper:** using fault injection (voltage/clock glitching), heat, or EM to extract secrets or skip security checks.
* **Supply-chain tampering:** device altered during manufacturing/distribution so units arrive pre-compromised and authenticate to cloud as legitimate devices.

---

## Mitigations & Defensive Controls

**Physical & hardware**

* Tamper-evident and tamper-resistant enclosures (seals, conformal coating, epoxy) for fielded devices.
* Tamper sensors and switches that trigger secure wipe/lockdown or alert the cloud when enclosure is opened.
* Use secure elements / TPMs / hardware root-of-trust to store keys so private keys cannot be trivially read even if flash is dumped.

**Interfaces & firmware**

* Disable or password-protect debug interfaces in production; implement JTAG/SWD lock or fuse options.
* Secure Boot + measured boot: chain of trust from immutable ROM → signed bootloader → signed firmware; verify on every boot.
* Anti-rollback and signed updates with strong revocation/rollout controls; MFA and M-of-N signing for critical releases.

**Supply-chain & procurement**

* Supplier vetting, secure manufacturing processes, sealed packaging, and acceptance testing (randomized device checks, firmware/manifest verification).
* Component provenance tracking (serials, signatures) and inventory reconciliation before provisioning.

**Operational & cloud**

* Require device attestation before granting cloud provisioning, and bind device identity to hardware-backed keys.
* Limit device privileges in cloud (least privilege), segment device groups, and apply per-device rate/command limits.
* Monitor device health signals and attestation trends; alert on abrupt changes (firmware mismatch, new endpoints).

**Detection & incident response**

* Continuous monitoring of firmware hashes, boot measurements, unexpected reboots, abnormal telemetry, and anomalous outbound connections.
* Strong playbooks: isolate device, revoke its credentials, capture forensic image (where possible), and reprovision replacement devices.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                                 |
| ---------------- | -----------: | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Tampering can yield persistent backdoors, stolen keys, false telemetry leading to wrong decisions, or direct physical harm via actuators. |
| Reproducibility  |        **7** | Many cheap devices are similar; basic tampering (open case, read UART) is easy; high-skill implants are harder but feasible.              |
| Exploitability   |        **7** | Requires physical access or supply-chain access; logical tampering possible via exposed debug/OTA channels if poorly protected.           |
| Affected Users   |        **8** | Compromised node classes (gateways/sensors) can affect entire fleets or cloud trust relationships, amplifying impact.                     |
| Discoverability  |        **6** | Surface tamper signs may be visible (seals broken), but implants and firmware backdoors can be stealthy without attestation/forensics.    |

**Digit-by-digit arithmetic:**
Sum = 8 + 7 + 7 + 8 + 6 = **36**.
Average = 36 / 5 = **7.2**.

**DREAD average = 7.2**; Rating: **High Risk** (address promptly with hardware, supply-chain and attestation controls).

---

## References

1. National Institute of Standards and Technology. (2020). *NISTIR 8259: Foundational Cybersecurity Activities for IoT Device Manufacturers.* NIST. [https://doi.org/10.6028/NIST.IR.8259](https://doi.org/10.6028/NIST.IR.8259)
2. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/publications/baseline-security-recommendations-for-iot](https://www.enisa.europa.eu/publications/baseline-security-recommendations-for-iot)
3. OWASP Foundation. (2023). *OWASP IoT Top Ten.* OWASP. [https://owasp.org/www-project-internet-of-things/](https://owasp.org/www-project-internet-of-things/)
4. Grand, J., & Smith, R. (2019). *Hardware Security: Principles and Practice* (selected chapters on tamper resistance and secure elements). (Publisher/DOI as appropriate)
5. Carnegie Mellon University, Software Engineering Institute. (2022). *Secure supply chain and firmware integrity guidance.* CERT/SEI. [https://insights.sei.cmu.edu](https://insights.sei.cmu.edu)

---
