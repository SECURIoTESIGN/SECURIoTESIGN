# RFID Spoofing & Injection Attack

## Definition

**RFID spoofing & injection** is the act of forging or fabricating RFID tag responses or injected reader events so that a system (reader, gateway, mobile app, or cloud backend) accepts false identities, transactions or telemetry. Attackers may emulate legitimate tags, inject synthetic reads into reader firmware or network pipelines, or tamper with reader→cloud messages to cause fraudulent access, fake inventory, incorrect billing, or malicious actuator commands in IoT ecosystems.

---

## Attack Categories

* **Static-ID spoofing:** replay or emulate tags that expose static identifiers (UIDs) to impersonate devices or users.
* **Cryptographic-protocol spoofing:** emulate or forge challenge/response flows by breaking weak crypto, capturing session data, or using stolen keys.
* **Reader-side injection:** compromise reader firmware, middleware or gateway to inject fabricated read events or modify payloads before cloud ingestion.
* **Network/ingest injection:** attacker inserts synthetic tag events directly into cloud ingestion APIs (via stolen API keys, misconfigured endpoints, or compromised gateways).
* **Relay-assisted spoofing:** relay a legitimate tag’s response across distance or into a remote reader to bypass proximity controls.
* **Combined supply-chain spoofing:** provision counterfeit tags during manufacture with forged credentials that pass provisioning checks and register in cloud systems.

---

## Mitigations & Controls

**Tag & protocol**

* Prefer tags implementing mutual challenge–response and per-transaction cryptograms (no reliance on static UID for authorization).
* Use transaction nonces, rolling counters and sequence numbers to detect replays.

**Reader & edge**

* Enforce signed reader firmware and secure boot; implement transport security (mTLS) from reader → cloud to prevent injection in transit.
* Validate cryptograms at the edge and reject reads that fail authenticity or counter checks.
* Apply anti-relay measures (time-of-flight / distance checks) for proximity-sensitive use-cases.

**Cloud & application**

* Server-side duplicate detection (transaction IDs, counters), multi-reader confirmation for critical events, and attestation-based provisioning (require device proof before accepting provisioning or high-risk commands).
* Bind provisioning tokens to device identity, and require multi-factor confirmation (mobile app confirmation, operator PIN) for sensitive ops (payments, actuator commands).
* Enforce strict API authentication and rotate credentials; use allowlists and per-reader credentials.

**Operational & supply-chain**

* Vet tag and reader vendors; require signed manifests and per-batch keying; perform random sampling and verify tag cryptograms during acceptance.
* Roll keys and invalidate compromised batches; maintain incident playbooks and firmware provenance checks.

**Detection & anomaly**

* Correlate spatial/temporal patterns: identical tag IDs at distant gates, improbable read rates, or mismatched reader IDs; deploy edge anomaly detectors and cloud analytics.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                                 |
| ---------------- | -----------: | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Successful spoof/injection enables fraud (access/payment), supply-chain manipulation, or false telemetry with business/safety impact.     |
| Reproducibility  |        **8** | Toolkit and techniques for UID spoofing, relay, and network injection are broadly known and inexpensive to enact for many systems.        |
| Exploitability   |        **7** | Varies by system: trivial for static-ID deployments; requires skill/tools to break cryptographic protections or to compromise readers/GW. |
| Affected Users   |        **8** | Affects customers, physical security zones, warehouses, payment endpoints, and IoT fleets trusting tag identity.                          |
| Discoverability  |        **7** | Injection is detectable with correlation and counters, but sophisticated injected events or supply-chain forgeries can be stealthy.       |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 8 + 7 = **38**.
**Average = 38 / 5 = 7.6**; Rating: **High / Critical**.

---

## References

1. Karygiannis, T., Eydt, B., Barber, G., Bunn, L., & Phillips, T. (2007). *Guidelines for Securing Radio Frequency Identification (RFID) Systems* (NIST Special Publication 800-98). National Institute of Standards and Technology. [https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf)
2. EMVCo. (2018). *EMV Contactless Specifications for Payment Systems.* EMVCo. [https://www.emvco.com/specifications/](https://www.emvco.com/specifications/)
3. International Organization for Standardization. (2013). *ISO/IEC 14443 — Identification cards — Contactless integrated circuit cards — Proximity cards.* ISO. [https://www.iso.org/standard/77388.html](https://www.iso.org/standard/77388.html)
4. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
5. OWASP Foundation. (2023). *OWASP IoT Top Ten & Mobile Security Verification Standard (MASVS).* OWASP. [https://owasp.org/](https://owasp.org/)

---

## RFID Spoofing Injection Attack Diagram