# Phishing Attack Model

## Definition

**Phishing** is a **social engineering attack** that deceives users or devices into revealing sensitive information (e.g., credentials, tokens, financial data) or executing malicious actions by impersonating legitimate entities. Unlike pharming, phishing depends on **user interaction or device trust**—through fake emails, SMS (smishing), voice calls (vishing), QR codes (quishing), or in-app prompts that trick users or automated clients into connecting to malicious endpoints or approving attacker-initiated actions.

In **cloud-based mobile and IoT ecosystems**, phishing can lead to unauthorized access to cloud accounts, IoT device hijacking, API key theft, and lateral compromise across multi-tenant systems.

---

## Attack Categories

* **Email / credential phishing:** fraudulent cloud login or SSO pages used to capture credentials and MFA tokens.
* **Smishing & vishing:** SMS or calls with malicious links or OTP requests targeting mobile users and IoT administrators.
* **OAuth & SSO token theft:** consent phishing attacks using fake OAuth app authorizations to gain access to cloud data or device control APIs.
* **Malicious QR code (Quishing):** deceptive QR codes in IoT dashboards or printed labels redirect to attacker sites.
* **Mobile app phishing:** trojanized mobile apps or fake updates prompting credential entry.
* **In-app / push notification phishing:** fake MFA prompts or admin access requests used to trick operators.
* **IoT management portal impersonation:** forged cloud dashboards or provisioning servers intercept device registration and telemetry.

---

## Mitigations & Defensive Controls

**User & identity protection**

* **Phishing-resistant authentication:** adopt **FIDO2/WebAuthn** or hardware-backed MFA to eliminate credential reuse.
* **Token binding & short-lived credentials:** use OAuth tokens with narrow scopes and expiry to reduce damage if stolen.
* **Behavioral analytics:** detect anomalies in login patterns, device fingerprints, and geolocation.
* **Security awareness & simulation:** continuous phishing training and simulated campaigns for administrators and operators.

**Technical & infrastructure controls**

* **Email and content filtering:** enable DMARC, DKIM, SPF and advanced threat protection (ATP) for cloud email.
* **Browser & app hardening:** implement Safe Browsing APIs, URL reputation checks, and certificate pinning in mobile apps.
* **Cloud identity protections:** enforce conditional access (risk-based login policies) and continuous verification (Zero Trust).
* **IoT provisioning integrity:** require signed manifests and device attestation for onboarding.
* **API key rotation & least privilege:** store secrets securely, avoid embedding credentials in code, and rotate keys automatically.

**Detection & response**

* **Monitor login anomalies:** detect impossible travel, device changes, and repeated failed logins.
* **Threat intelligence integration:** ingest feeds of known phishing domains, lookalike hostnames, and attacker infrastructure.
* **User reporting:** simple in-app or email report phishing buttons connected to SOC workflow.
* **Incident automation:** automated account lock, token revocation, and password reset for compromised identities.

---

## 4) DREAD Risk Assessment

| DREAD Factor         | Score | Rationale                                                                                                 |
| -------------------- | :---: | --------------------------------------------------------------------------------------------------------- |
| **Damage Potential** | **9** | Credential or token theft can grant access to cloud systems, IoT control layers, and sensitive user data. |
| **Reproducibility**  | **9** | Highly repeatable; attackers reuse templates, kits, and phishing-as-a-service platforms.                  |
| **Exploitability**   | **8** | Low cost and easily automated via email, SMS, or fake apps; success depends on human error.               |
| **Affected Users**   | **8** | Large-scale impact—users, admins, or fleets of IoT devices tied to shared credentials.                    |
| **Discoverability**  | **6** | Attack pages often transient; detection possible via filtering and domain analysis but reactive.          |

**Digit-by-digit arithmetic:**
**Sum = 9 + 9 + 8 + 8 + 6 = 40**
**Average = 40 / 5 = 8.0** ; Rating: **High / Critical**

---

## References

1. National Institute of Standards and Technology. (2020). *NIST SP 800-63B: Digital Identity Guidelines – Authentication and Lifecycle Management.* NIST. [https://doi.org/10.6028/NIST.SP.800-63b](https://doi.org/10.6028/NIST.SP.800-63b)
2. OWASP Foundation. (2023). *OWASP Phishing Defense Cheat Sheet.* OWASP. [https://owasp.org/](https://owasp.org/)
3. ENISA. (2022). *Phishing – Threat Landscape and Mitigation Guidelines.* European Union Agency for Cybersecurity. [https://www.enisa.europa.eu/](https://www.enisa.europa.eu/)
4. Microsoft. (2024). *Phishing-resistant MFA and identity protection in cloud environments.* Microsoft Security Blog. [https://www.microsoft.com/security/blog/](https://www.microsoft.com/security/blog/)
5. Anti-Phishing Working Group. (2025). *Phishing Activity Trends Report.* APWG. [https://apwg.org/](https://apwg.org/)


---


## Phishing Attack Tree Diagram