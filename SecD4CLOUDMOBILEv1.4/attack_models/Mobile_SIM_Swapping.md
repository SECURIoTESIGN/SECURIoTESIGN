# Mobile SIM-Swapping Attack Model

## Definition

**SIM-swapping (SIM-jacking / SIM-porting)** is an account-takeover technique where an attacker convinces a mobile operator (or abuses operator processes) to transfer a victim’s phone number to a SIM card controlled by the attacker. With control of the number the attacker can intercept SMS/MFA codes, receive calls, reset passwords for cloud/mobile accounts, and abuse phone-bound authentication or device provisioning flows — impacting cloud apps and IoT services that rely on SMS, voice, or number-based identity.

---

## Attack categories (cloud / mobile app / IoT specifics)

* **Social-engineering at the carrier:** attacker uses stolen ID info, spoofed documents, or persuasive calls to convince support staff to port the number.
* **Insider-assisted porting:** collusion with or bribery of telecom employees who perform unauthorized porting.
* **SIM cloning / physical theft:** physical access to SIM card or use of cloned SIM/IMSI to receive messages (less common with modern SIM protections).
* **Port-out fraud / account recovery abuse:** attacker initiates number transfer (port out) to another carrier and triggers OTPs/password resets.
* **Supply-chain/provisioning automation abuse:** targeting automated provisioning or SMS gateways used by IoT device enrollment (e.g., devices registered via number).
* **Credential stuffing + SIM swap:** combine leaked credentials to pre-validate identity during porting process.
* **IoT device takeover via number control:** replacing SIMs in cellular IoT devices or hijacking phone numbers used as second factors for device management APIs.

---

## Mitigations & Defensive Controls

**Authentication & account design**

* **Avoid SMS/voice for primary 2FA** where possible; adopt stronger, phishing-resistant MFA (authenticator apps, FIDO2/WebAuthn, hardware tokens, mTLS).
* **Bind accounts to multiple strong factors** (device attestation, hardware keys) not just a phone number.

**Carrier & provisioning hardening**

* **Port-freeze / Number locking:** encourage users to enable carrier-provided port protection (port freeze, PIN/passphrase on account).
* **Out-of-band verification with carriers:** require in-person or documented ID checks for porting on high-risk accounts; use callback to a previously confirmed number.
* **Rate limits / alerts:** block rapid or multiple port requests and notify account owner via alternate channels (email, app push) when porting requested.

**Cloud & app controls**

* **Do not rely solely on SMS for password resets:** require additional proofs (device attestation, signed tokens, step-up authentication).
* **Bind long-lived credentials to device identity** and verify device fingerprints before sensitive changes.
* **Monitor for anomalous account recovery flows:** sudden MFA failures, new device registrations following SMS delivery, or unusual IPs following a port request.

**IoT / device lifecycle**

* **Do not use phone-number as sole device identity:** use certificate-based device identity, SIM eUICC with device certificates, or hardware-backed keys.
* **Protect provisioning channels:** require attestation/one-time provisioning tokens delivered out-of-band (printed labels, secure portal) rather than only SMS.
* **Inventory & alerts:** detect sudden loss of device telemetry coincident with SMS/voice failures for device numbers.

**Operational / detection**

* **Telemetry & logging:** correlate carrier porting events (where available), spikes in password reset attempts, unexpected MFA acceptances, and new device enrollments.
* **Incident playbooks:** rapid credential rotation, revoke sessions, require step-up re-authentication, and contact carrier fraud desks to reverse port if possible.
* **User education:** warn users about SIM swap risk and encourage port locks and non-SMS MFA.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score | Rationale                                                                                                                                          |
| ---------------- | :---: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential | **9** | Full account takeover (cloud apps, banking, device management); can lead to data loss, financial fraud, and IoT/control compromise.                |
| Reproducibility  | **8** | Social-engineering and automated porting techniques are well known; many carriers historically had weak processes.                                 |
| Exploitability   | **7** | Requires successful social engineering, insider help, or exploiting carrier process gaps — feasible at scale for determined attackers.             |
| Affected Users   | **8** | Individual users and entire fleets (cellular IoT) that use number-based auth or provisioning are at risk.                                          |
| Discoverability  | **6** | Porting actions and sudden loss of SMS are observable, but attackers often act quickly; detecting attempted social engineering beforehand is hard. |

**Digit-by-digit arithmetic:**

**Sum = 9 + 8 + 7 + 8 + 6 = 38**.
**Average = 38 / 5 = 7.6**; Rating: Rating: **High / Critical**

---

## References

1. Federal Trade Commission. (2022). *SIM swap scams: How scammers steal phone numbers to break into accounts.* Federal Trade Commission. [https://www.consumer.ftc.gov/articles/sim-swap-scam](https://www.consumer.ftc.gov/articles/sim-swap-scam)
2. U.S. Cybersecurity and Infrastructure Security Agency. (2021). *Account Takeover and SIM Swap Threats: Practices to mitigate account takeover and SIM swap fraud.* CISA. [https://www.cisa.gov](https://www.cisa.gov)
3. GSMA. (2018). *Guidelines on Securing Mobile Network Porting & SIM Swap Fraud Mitigation.* GSMA. [https://www.gsma.com](https://www.gsma.com)
4. NIST. (2017). *NIST Special Publication 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management.* National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.SP.800-63b](https://doi.org/10.6028/NIST.SP.800-63b)
5. Krebs, B. (2018). *SIM swapping — practically speaking.* KrebsOnSecurity. [https://krebsonsecurity.com](https://krebsonsecurity.com)
6. Verizon. (2024). *Verizon Data Breach Investigations Report 2024* (insights on account takeover trends). Verizon Business. [https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf](https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf)

---


## Mobile SIM Swapping Attacks Diagram
