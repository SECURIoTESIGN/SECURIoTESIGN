# NFC Payment Replay Attacks

In such an attack scenario, the attacker aims to steal or steal sensitive data from the target user, such as banking or financial data, including monetary values. This type of attack targets the data exchanged between the payment device (smart card or mobile software) and the payment terminal via NFC wireless network technology.

## Definition

 This type of attack targets the exploitation of vulnerabilities in the European Visa and Mastercad (EMV) wireless communication protocol between the smartcard and the payment terminal, namely, the authenticity of the payment terminal is not guaranteed to the customer's payment device and the banking data exchanged between the customer's payment device (smartcard) and the point of sale terminal are not encrypted and are transferred in clear text. Such an attack occurs when an attacker retransmits authentication-related communication between a payment device, VISA smartcard or Mastercard (RFID) and an automated payment terminal.
 
## Overview

* **Objective**: To manipulate NFC transactions and replay them to deceive payment systems.
* **Method**: Attackers intercept legitimate NFC payment data and replay it later.
* **Impact**: Can lead to unauthorized transactions, financial losses, and compromised user trust.

## Mitigation

1. **Unique Transaction IDs:** Each transaction should have a unique ID that is used only once. This can prevent an attacker from replaying a previous transaction;
2. **Time Stamping:** Implement time stamping of transactions. If the timestamp is too old, the transaction can be rejected.
Secure Communication: Use secure communication protocols such as Secure NFC, which provides encryption and message integrity checks;
3. **Payment Tokenization:** Use payment tokenization to replace sensitive card data with a non-sensitive equivalent, known as a token. The token is unique to each transaction and has no value if stolen;
4. **User Confirmation:** Always ask for user confirmation before processing a payment. This can prevent unauthorized transactions;
5. **Regular Updates and Patches:** Keep your systems and software up-to-date. Regular updates and patches can fix known vulnerabilities that could be exploited by NFC Payment Replay attacks.

## Architectural Risk Analysis of NFC Payment Replay Vulnerability


| **Factor**                                  | **Description**                                                                    | **Value**                        |
|---------------------------------------------|------------------------------------------------------------------------------------|----------------------------------|
| Attack   Vector (AV):                       | Physical   (Requires physical proximity to capture and replay data)                | Physical   (L)                   |
| Attack   Complexity (AC):                   | Medium   (Requires specialized tools and knowledge to capture and replay data)     | Medium   (M)                     |
| Privileges   Required (PR):                 | None   (Attacker needs to be near the user during transaction)                     | None   (N)                       |
| User   Interaction (UI):                    | None   (User interaction initiates the vulnerable transaction)                     | None   (N)                       |
| Scope   (S):                                | Fraudulent   Transaction (attacker can potentially initiate unauthorized payments) |         Financial Loss (F)       |
| Confidentiality   Impact (C):               | Low   (Payment data itself might be anonymized tokens)                             | Low   (L)                        |
| Integrity   Impact (I):                     | High   (Attacker can potentially manipulate transaction data)                      | High   (H)                       |
| Availability   Impact (A):                  | Low   (Doesn't affect overall application functionality)                           | Low   (L)                        |
| Base   Score (assuming High for Integrity): | 0.85   * (AV:L/AC:M/PR:N/UI:N) * (S:F/C:L/I:H/A:L)                                 | 5.9   (Medium)                   |


## References

1. Njebiu, V., Kimwele, M., Rimiru, R., 2021. Secure contactless mobile payment system, in: 2021 IEEE Latin-American Conference on Communications (LATINCOM), IEEE, Santo Domingo, Dominican Republic. pp. 1–6. doi:10.1109/LATINCOM53176.2021.9647831.

## NFC Payment Replay Attacks Tree Diagram
