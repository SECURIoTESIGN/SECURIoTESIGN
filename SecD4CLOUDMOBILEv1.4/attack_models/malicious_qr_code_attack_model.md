# Malicious QR Code Attack Model

## Definition

**Malicious QR code attack** - the use of QR (Quick Response) codes to deliver or enable malicious actions: directing users to phishing websites, triggering unintended actions (Wi‑Fi configuration, payment initiation), downloading malware, or leaking device/cloud credentials. In cloud, mobile and IoT contexts, malicious QR codes can be used to provision rogue devices, falsify onboarding flows, or redirect telemetry to attacker-controlled endpoints.

## Attack Categories

* **Phishing / credential harvesting:** QR codes direct users to cloned cloud login pages to capture credentials or MFA tokens.
* **Malicious provisioning / onboarding abuse:** attacker-supplied QR codes provision devices with attacker-controlled endpoints, SSH keys, or misconfigured IoT settings.
* **Drive-by payloads / malware delivery:** QR points to downloadable payloads (malicious apps, configuration files) which, when installed on mobile or edge devices, compromise devices or cloud credentials.
* **Payment / transaction fraud:** QR codes trigger fraudulent payment URIs or redirect to manipulated payment flows.
* **Network misconfiguration:** QR encodes rogue Wi‑Fi SSID/password or VPN settings that cause devices to join attacker-controlled networks for interception.
* **Supply-chain and labeling attacks:** tampered product labels or stickers with replaced legitimate QR codes (logistics/asset mgmt manipulation) that cause mis-tagging or data injection into cloud systems.

---

## Mitigations & Defensive Controls

**UI/UX & user controls**

* Display destination URL preview with domain highlighting and certificate checks before opening; warn users about non-HTTPS or foreign domains.
* Limit automatic execution of actions from QR scans (require user confirmation for provisioning, Wi‑Fi join, app install, or payments).

**Provisioning & onboarding hardening**

* Out-of-band verification for device provisioning (compare serials, use manufacturer-signed manifests, or one-time pairing codes).
* Use device attestation and mutual auth during onboarding so scanning a QR alone cannot provision full access.

**Mobile / endpoint protections**

* Enforce app-store-only installs and block sideloading on managed devices; verify app signatures and use MDM policies.
* Endpoint detection: block automatic handling of URI schemes that can trigger privileged actions without user consent.

**Cloud & backend controls**

* Validate provisioning tokens and pairings on server-side (short-lived tokens, binding to device identity).
* Monitor for anomalous provisioning events, sudden new device registrations, or unexpected endpoints receiving telemetry.

**Operational & physical controls**

* Protect physical QR deployments: tamper-evident labels, regular inspection of public posters/labels, use secure placement (inside kiosks), and logging of printed QR batch IDs.
* Training & awareness: educate staff and customers about QR risks and safe scanning practices.

---

## DREAD risk assessment (0-10)

| Factor           | Score | Rationale                                                                                                                                           |
| ---------------- | ----: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential | **7** | Can lead to credential theft, device compromise, fraudulent transactions or rogue provisioning—impact ranges moderate to high depending on context. |
| Reproducibility  | **9** | Creating malicious QR codes is trivial and inexpensive; wide distribution (stickering, posters, digital images) is easy.                            |
| Exploitability   | **7** | Requires human interaction (scan) but social engineering and ubiquity of QR use make exploitation likely.                                           |
| Affected Users   | **7** | Can impact many users if placed in public locations or distributed via popular channels; provisioning abuse can affect entire device fleets.        |
| Discoverability  | **8** | Targets and vectors are easy to discover (public posters, product labels, onboarding flows); malicious QR codes are visible and can be tested.      |

**Digit-by-digit DREAD arithmetic (explicit):**
Sum = 7 + 9 + 7 + 7 + 8 = 38.
Average = 38 / 5 = 7.6.

**DREAD average = 7.6**; Rating: **High priority** (recommend immediate UX/endpoint mitigations and hardening of provisioning flows).

---

## References

1. Krombholz, K., Hobel, H., Huber, M., & Weippl, E. (2014). *QR code security: A survey of attacks and countermeasures.* In Proceedings of the International Conference on Availability, Reliability and Security (ARES). [https://doi.org/10.1109/ARES.2014.34](https://doi.org/10.1109/ARES.2014.34)
2. OWASP Foundation. (2023). *OWASP Mobile Top Ten and QR code considerations.* OWASP. [https://owasp.org/](https://owasp.org/)
3. National Institute of Standards and Technology. (2021). *NIST Special Publication 800-163: Vetting the Security of Mobile Applications.* NIST. [https://doi.org/10.6028/NIST.SP.800-163](https://doi.org/10.6028/NIST.SP.800-163)
4. ENISA. (2020). *Threat Landscape for Phishing and Social Engineering.* European Union Agency for Cybersecurity. [https://www.enisa.europa.eu/](https://www.enisa.europa.eu/)
5. Zhang, Y., & Yu, S. (2019). *Attacks on QR code-based payment systems and mitigations.* IEEE Communications Surveys & Tutorials (Selected articles).

---
                                     |

## Malicious QR Code Attack Tree Diagram