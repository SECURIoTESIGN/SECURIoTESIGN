# NFC Payment Replay Attack Model

## Definition

An **NFC payment replay attack** is a form of fraud where a valid contactless transaction is captured and maliciously repeated to make unauthorized payments. It exploits weaknesses in how some NFC systems handle transaction uniqueness and session validation. In a replay attack, an attacker intercepts a legitimate data transmission and resends it to trick the system into accepting it again. 

---

## Attack Categories

* **Simple radio replay:** record the raw NFC exchange between a card/wallet and reader, then replay the raw signal to a reader to attempt duplicate authorization (works only against very weak readers/protocols).
* **Transaction-record replay (relay + store-and-forward):** attacker records the transaction data and attempts to reuse an intercepted message or mimic the message to another reader or backend.
* **Relay attack (mafia/fraud relay):** real-time forwarding between a victim’s device and a distant reader so the attacker can perform a live payment without proximity.
* **Offline replay against legacy/poorly-implemented terminals:** replaying EMV-like data to terminals that accept offline static data or that do not verify dynamic cryptograms properly.
* **Provisioning/rebinding abuse:** replaying provisioning QR/NFC token or activation data to provision an attacker-controlled device into the cloud account (attack on onboarding).
* **Chained attacks:** use replayed or relayed tokens to extract credentials, cause billing anomalies in cloud-side systems, or trigger inappropriate IoT actuation tied to payment confirmation.

---

## Mitigations & Defensive Controls

**Protocol & cryptographic**

* **Use dynamic transaction authentication:** EMV contactless uses dynamic cryptograms (ARQC/ARPC) and transaction counters—ensure terminals and issuers validate cryptograms and counters to prevent reuse.
* **Nonce / challenge-response:** every transaction must include a fresh challenge or nonce signed by secure element / HSM so recording and replay are invalid.
* **Limit offline acceptance & enforce online auth where feasible:** require online authorization for high-value or suspicious transactions so issuer can detect duplicates.

**Device & reader hardening**

* **Secure element / TEE / eSE:** store keys and perform cryptographic ops inside hardware-backed secure elements that never expose raw keys or reusable static data.
* **Relay-protection mechanisms:** distance bounding, secure channel establishment, and short time windows for valid responses where supported.
* **Terminal validation:** ensure POS/reader firmware enforces anti-replay checks, rejects duplicate transaction counters, and enforces strict protocol state machines.

**Cloud & backend**

* **Server-side duplicate detection:** maintain transaction identifiers, use nonces and per-transaction sequence numbers, detect and reject duplicate transaction IDs or reuse of cryptograms.
* **Rate-limits & anomaly detection:** flag rapid repeated attempts, geographic anomalies, or unusual device/terminal pairings; correlate logs from edge devices and cloud.
* **Secure provisioning:** prevent provisioning or activation simply by presenting an NFC token; require multi-factor or attestation-bound provisioning.

**Operational & user**

* **Patch, regular updates, and replace legacy terminals:** retire readers that accept static data or lack cryptogram verification.
* **Monitoring & logging:** log transaction cryptograms, counters and device attestation; enable quick rollbacks or blocking of suspect devices.
* **Education:** train staff to recognise suspicious equipment/relay devices at checkout and to use tamper-evident terminal housings.

---

## DREAD Risk Assessment (0-10)

|     DREAD Factor | Score (0-10) | Rationale                                                                                                                                              |
| ---------------: | :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Damage Potential |     **7**    | Duplicate payments, fraud losses, billing disputes and loss of customer trust; more severe when combined with provisioning abuse.                      |
|  Reproducibility |     **7**    | Replay and relay techniques are well-known; success depends on protocol/terminal weaknesses.                                                           |
|   Exploitability |     **6**    | Requires proximity for simple radio replay or moderate resources for relay/recording; mitigated by modern dynamic cryptography and secure elements.    |
|   Affected Users |     **7**    | Affects customers using contactless payments, wearables and fleets of payment-enabled IoT devices; localized but can scale if many terminals are weak. |
|  Discoverability |     **6**    | Vulnerable terminals/devices are discoverable, but detecting successful replay in logs requires careful correlation.                                   |

**Digit-by-digit arithmetic (explicit):**

**Sum = 7 + 7 + 6 + 7 + 6 = 33**.
**Average = 33 / 5 = 6.6**.

**DREAD average = 6.6**; Rating: **Medium–High risk.**

---

## References

1. EMVCo. (2018). *EMV Contactless Specifications for Payment Systems.* EMVCo. [https://www.emvco.com/specifications/](https://www.emvco.com/specifications/) (see Contactless and Kernel specifications)
2. PCI Security Standards Council. (2022). *PCI DSS and Contactless Payment Security Guidelines.* PCI SSC. [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/)
3. National Institute of Standards and Technology. (2013). *NIST SP 800-124 Revision 1: Guidelines for Managing the Security of Mobile Devices in the Enterprise.* NIST. [https://doi.org/10.6028/NIST.SP.800-124r1](https://doi.org/10.6028/NIST.SP.800-124r1)
4. GSMA. (2017). *GSMA Secure NFC and Mobile Payments: Best Practices.* GSMA. [https://www.gsma.com/](https://www.gsma.com/)
5. OWASP Foundation. (2023). *OWASP Mobile Top 10 and Mobile Security Cheat Sheets* (relevant guidance on secure payments and token handling). [https://owasp.org/](https://owasp.org/)
6. Njebiu, V., Kimwele, M., Rimiru, R., 2021. Secure contactless mobile payment system, in: 2021 IEEE Latin-American Conference on Communications (LATINCOM), IEEE, Santo Domingo, Dominican Republic. pp. 1–6. doi:10.1109/LATINCOM53176.2021.9647831.

---


## NFC Payment Replay Attacks Tree Diagram
