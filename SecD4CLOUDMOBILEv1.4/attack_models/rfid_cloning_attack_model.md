# RFID Cloning & Injection Attack

## Definition

**RFID cloning & injection** is the creation of counterfeit RFID tags/cards or the injection of fabricated tag reads so that an attacker can impersonate a legitimate tag (clone) or insert forged tag data into a reader/cloud pipeline (injection). Impacts include fraudulent access, fake inventory, unauthorized payments, supply-chain manipulation, or feeding false telemetry into cloud/IoT systems.

---

## Attack Categories

* **Simple tag cloning:** reading a tag static identifier (UID / static data) and programming a blank/tag emulator to present the same ID (works against tags that use plaintext IDs).
* **Crypto-protocol break & key recovery:** exploiting weak/tag-specific crypto (e.g., broken proprietary cipher or weak key management) to extract keys and produce fully functional cloned tags (MIFARE Classic-style attacks).
* **Relay & emulation (live cloning):** proximate relay of tag/reader exchange to a remote reader (relay attack) or emulation using mobile devices to act as a genuine tag in real time.
* **Injection via compromised readers/gateways:** attacker inserts forged tag read events into reader firmware or cloud ingestion pipeline (bypassing physical cloning entirely).
* **Replay of captured transactions:** capture tag→reader exchanges and replay them to perform duplicate actions where protocols lack freshness (nonces/counters).
* **Supply-chain / provisioning forgery:** manufacturing or provisioning counterfeit tags that carry valid credentials (fraudulent provisioning or stolen signing keys) and register in cloud systems as legitimate devices.

---

## Mitigations & Defensive Controls

**Tag & protocol security**

* Prefer tags with **secure elements / hardware-backed cryptography** (mutual challenge-response, per-tag keys, rolling codes).
* Use **dynamic authentication** (per-transaction nonces, one-time tokens, transaction counters) so recorded data cannot be replayed.
* Avoid reliance on static UIDs for authorization; pair tag reads with contextual checks (reader identity, time, location).

**Reader & edge hardening**

* Enforce **reader-side validation**: verify cryptograms, check transaction counters, and reject duplicate/older counters.
* Secure readers: signed firmware, authenticated boot, and encrypted transport (mTLS) from reader → cloud to prevent injection.
* Use multi-reader confirmation and anti-relay techniques (distance bounding, time-of-flight checks) for high-risk actions (payments, access).

**Cloud & application**

* Implement **server-side duplicate detection** (transaction IDs, counters), anomaly scoring (sudden new tag IDs, geographic mismatch), and attestation for provisioning flows.
* Bind tag authorization to **device attestation** or multi-factor signals (mobile app confirmation, biometric/pin) for sensitive transactions.
* Maintain SBOM/asset registry mapping valid tag batches and expected provisioning metadata.

**Operational & supply-chain**

* Vet tag suppliers, sign and verify provisioning manifests, use tamper-evident labeling, and perform random lot testing for counterfeit tags.
* Roll keys and invalidate compromised batches; monitor telemetry for coordinated anomalies suggesting cloned fleets.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                            |
| ---------------- | -----------: | -------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Cloning can enable fraud (payments, access), theft, supply-chain manipulation, and large-scale false telemetry.      |
| Reproducibility  |        **8** | Simple cloning/replay is easy on many legacy systems; protocol attacks are reproducible where weak crypto is used.   |
| Exploitability   |        **7** | Varies: UID cloning is trivial; crypto/key extraction requires tools/skill but is widely demonstrated.               |
| Affected Users   |        **8** | Affects customers using contactless access/payment, warehouses, logistics, and cloud services trusting tag identity. |
| Discoverability  |        **6** | Unauthorised clones and injected reads can be stealthy—detection requires cross-correlation and instrumentation.     |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 8 + 6 = **37**.
**Average = 37 / 5 = 7.4**; Rating: **High risk**.

---

## References

1. National Institute of Standards and Technology. (2007). *Guidelines for Securing Radio Frequency Identification (RFID) Systems* (NIST Special Publication 800-98). NIST. [https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-98.pdf)
2. International Organization for Standardization / International Electrotechnical Commission. (2013). *ISO/IEC 14443 — Identification cards — Contactless integrated circuit cards — Proximity cards.* ISO.
3. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
4. OWASP Foundation. (2023). *OWASP IoT Top Ten & IoT Security Guidance.* OWASP. [https://owasp.org/](https://owasp.org/)
5. EMVCo. (2018). *EMV Contactless Specifications for Payment Systems* (for dynamic authentication and cryptogram use in contactless payments). EMVCo. [https://www.emvco.com/specifications](https://www.emvco.com/specifications)

---


## RFID Cloning Injection Attack 