# Malicious Insider Attack Model

## Definition

**Malicious insider attack** — an action by a trusted person (employee, contractor, vendor) who intentionally misuses authorized access to harm confidentiality, integrity or availability of systems, data or services. In cloud and IoT contexts this includes exfiltrating telemetry/keys from edge devices, abusing cloud management consoles, inserting malicious firmware/labels, or manipulating provisioning to create backdoors. ([NIST Computer Security Resource Center][1]) 

---

## Attack categories

* **Credential abuse / privilege misuse:** using legitimate credentials to access sensitive cloud projects, data buckets, IoT device fleets or management APIs.
* **Data exfiltration / stealth export:** staged retrieval of telemetry, keys, ML models or PII from cloud storage or edge devices (often slowly to avoid detection).
* **Provisioning / configuration sabotage:** altering IaC/automation, introducing malicious images, or misconfiguring ACLs to create persistent access.
* **Malicious firmware/OTA insertion:** swapping or pushing signed-but-malicious firmware to IoT fleets (requires signing compromise or rogue signer).
* **Lateral movement / cloud escalation:** pivoting from an edge device or local network to cloud consoles or other high-value targets.
* **Collusion with external actors:** insider cooperates with external attackers (ransom/espionage) to amplify impact. ([sei.cmu.edu][2])

---

## Mitigations & practical controls

The malicious insider threat is one of the most difficult threats to detect because the insider has legitimate access and is part of the organization which makes it hard to identify the malicious activity. Some of the most preventative measures organizations can take to mitigate against malicious insider attacks are:

* **Least privilege & just-in-time access:** enforce minimal roles, time-limited elevation (temporary credentials, ephemeral keys). ([NIST Computer Security Resource Center][3])
* **Strong authentication & session control:** MFA (phishing-resistant), session monitoring, anomaly-based re-authentication for sensitive ops.
* **Cloud-native controls:** enforce resource tagging, IAM policies, org-level guardrails, separation of duties, and logging of management-plane actions. ([enisa.europa.eu][4])
* **Device attestation & hardware-backed keys:** require attestation before provisioning; keep private keys in HSM/TPM rather than firmware.
* **Data-loss prevention (DLP) & exfiltration controls:** egress filtering, content inspection, staged-data thresholds and abnormal-volume alerts.
* **Behavioral analytics & insider program:** combine technical telemetry (IAM logs, API call patterns, firmware/OTA history) with HR/operational signals in an insider-threat program. ([sei.cmu.edu][2])
* **Secure CI/CD & supply chain:** protect signing keys, implement multi-party signing (M-of-N) for releases, immutable artifacts and automated integrity checks.
* **Response playbooks:** revoke credentials, isolate effected devices/projects, forensically preserve logs and coordinate legal/HR actions.

---

## DREAD Risk Assessment (0-10)

> **Context:** enterprise cloud app with integrated IoT fleet (sensors/gateways). Scores reflect combined impact when an insider acts intentionally.

| Factor           | Score | Short rationale                                                                                                                             |
| ---------------- | ----: | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential | **9** | Insiders can cause data breaches, persistent backdoors, or cloud-account takeover with large business impact.                               |
| Reproducibility  | **6** | Some attacks require unique conditions (signing keys, privileged roles); others (credential abuse) are easy to repeat.                      |
| Exploitability   | **7** | Depends on access: exploited when policies/controls are weak (no MFA, wide roles, exposed keys).                                            |
| Affected Users   | **8** | Can affect entire tenant, many customers, or large IoT fleets.                                                                              |
| Discoverability  | **7** | Stealthy exfiltration and insider collusion make detection non-trivial but centered logging and analytics improve discovery. ([Verizon][5]) |

**Digit-by-digit DREAD arithmetic (explicit):**
Sum = 9 + 6 + 7 + 8 + 7 = 37.
Average = 37 / 5 = 7.4.

**DREAD average = 7.4**; Rating: **High (prioritise technical controls, monitoring & HR/process measures).**

---

## References

1. Carnegie Mellon University, Software Engineering Institute. (2022). *Common Sense Guide to Mitigating Insider Threats* (7th ed.). CERT/SEI. [https://insights.sei.cmu.edu/library/whitepapers](https://insights.sei.cmu.edu/library/whitepapers)
  ([sei.cmu.edu][2])
2. National Institute of Standards and Technology. (2020). *NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations* (Rev. 5). NIST. [https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
  ([NIST Computer Security Resource Center][3])
3. Cybersecurity and Infrastructure Security Agency. (n.d.). *Insider Threat Mitigation Guide.* CISA. [https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide)
  ([CISA][6])
4. National Institute of Standards and Technology. (n.d.). *Insider threat — NIST Computer Security Resource Center (glossary).* NIST. [https://csrc.nist.gov/glossary/term/insider_threat](https://csrc.nist.gov/glossary/term/insider_threat)
  ([NIST Computer Security Resource Center][1])
5. Verizon. (2024). *Data Breach Investigations Report 2024.* Verizon Business. [https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf](https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf)
  ([Verizon][5])

---

## Malicious Insider Attack Tree Diagram