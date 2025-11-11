# RFID Unauthorized Access Attack

## Definition

**RFID unauthorized access** occurs when an attacker leverages weaknesses in RFID systems (tags, readers, middleware, or cloud integration) to gain unauthorized entry, execute privileged operations, or control devices/services. In cloud/mobile/IoT ecosystems this can mean bypassing physical access controls, authorizing fraudulent payments, enrolling rogue devices, or invoking actuator commands by abusing tag-read authentication flows or management-plane trust.

---

## Attack Categories

* **Static-ID bypass / badge cloning:** using copied static UIDs to pass access control checks when systems accept UID alone.
* **Credential theft from readers/gateways:** extracting stored keys, session tokens or cached credentials from compromised edge devices and reusing them to authorize actions in cloud APIs.
* **Provisioning/Onboarding compromise:** attacker injects rogue tags or manipulates provisioning flows (QR/NFC/RFID) to enroll fraudulent devices into cloud fleets.
* **Privilege escalation via API abuse:** stolen or misused reader credentials or weak API auth permit attackers to mark reads as *authorized* or to push synthetic events to cloud systems.
* **Reader spoofing / rogue reader attacks:** fake readers issue authorization confirmations or trick mobile apps into approving actions (e.g., relay or push-based approvals).
* **Replay & replay-with-modification:** capturing legitimate auth exchanges and replaying (or replaying with small modifications) where freshness/nonces are not enforced.
* **Business-logic abuse / chaining:** combine RFID read fraud with other attacks (phishing, SIM-swap, cloned mobile wallets) to perform account takeover or payment fraud.

---

## Mitigations & Defensive Controls

**Authentication & protocol**

* **Do not rely on static identifiers alone**—use mutual challenge–response, per-transaction cryptograms, and per-tag keys.
* **Require freshness:** nonces, ATC/transaction counters, or signed timestamps validated server-side to prevent replay.
* **Use hardware-backed secure elements** (SE/eSE/TPM) for keys on tags, readers and mobile devices.

**Reader & edge security**

* **Secure transport:** mTLS between readers/gateways and cloud; authenticate and authorize each reader.
* **Protect stored secrets:** store keys in HSM/TPM on gateways; rotate keys regularly and limit local caching.
* **Harden readers:** signed firmware, secure boot, JTAG/SWD disabled or locked, intrusion/tamper detection on devices.

**Cloud & application**

* **Attestation-based provisioning:** require device attestation and one-time provisioning tokens for onboarding.
* **Server-side validation:** verify cryptograms, check counters, and reject duplicate/old transactions before granting access or action.
* **Least privilege & segmentation:** grant minimal capabilities per reader/device; enforce per-device rate and action limits.
* **Anomaly detection & correlation:** flag impossible travel for badges, duplicate IDs across locations, or unusual patterns of authorization.

**Operational & process**

* **Multi-factor confirmation for critical actions:** require mobile confirmation, biometric, PIN, or secondary factor (not just a tag read) for high-risk operations.
* **Supply-chain & procurement controls:** vet tag and reader vendors, sign manifests, and perform random batch verification.
* **Incident readiness:** maintain rapid revocation procedures for compromised readers/tokens and playbooks for physical security incidents.

---

## DREAD Risk Assessment (0-10)


| DREAD Factor     | Score (0-10) | Rationale                                                                                                                  |
| ---------------- | -----------: | -------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Unauthorized entry, fraudulent payments, or actuator misuse can cause safety, reputational, regulatory and financial harm. |
| Reproducibility  |        **8** | Many legacy deployments accept static IDs or weak auth; cloning and replay are easily reproduced.                          |
| Exploitability   |        **7** | Varies by deployment: trivial for static-ID systems, moderate when cryptography or reader hardening exists.                |
| Affected Users   |        **8** | Affects physical security zones, customers, warehouses, and cloud services reliant on RFID-authenticated actions.          |
| Discoverability  |        **6** | Some attacks are obvious (duplicate badge use), but credential theft and API-level injection can be stealthy.              |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 8 + 6 = **37**.
**Average = 37 / 5 = 7.4**;  Rating: **High priority**.

---

## 7) References

1. Karygiannis, T., Eydt, B., Barber, G., Bunn, L., & Phillips, T. (2007). *Guidelines for Securing Radio Frequency Identification (RFID) Systems* (NIST Special Publication 800-98). National Institute of Standards and Technology. [https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf)
2. EMVCo. (2018). *EMV Contactless Specifications for Payment Systems.* EMVCo. [https://www.emvco.com/specifications/](https://www.emvco.com/specifications/)
3. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
4. OWASP Foundation. (2023). *OWASP IoT Top Ten & Mobile Application Security Verification Standard (MASVS).* OWASP. [https://owasp.org/](https://owasp.org/)

---

## RFID Unauthorized Access Attack Tree Diagram