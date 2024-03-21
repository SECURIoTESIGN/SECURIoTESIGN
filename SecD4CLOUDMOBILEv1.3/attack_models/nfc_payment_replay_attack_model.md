# NFC Payment Replay Attacks

In such an attack scenario, the attacker aims to steal or steal sensitive data from the target user, such as banking or financial data, including monetary values. This type of attack targets the data exchanged between the payment device (smart card or mobile software) and the payment terminal via NFC wireless network technology.

## Definition

 This type of attack targets the exploitation of vulnerabilities in the European Visa and Mastercad (EMV) wireless communication protocol between the smartcard and the payment terminal, namely, the authenticity of the payment terminal is not guaranteed to the customer's payment device and the banking data exchanged between the customer's payment device (smartcard) and the point of sale terminal are not encrypted and are transferred in clear text. Such an attack occurs when an attacker retransmits authentication-related communication between a payment device, VISA smartcard or Mastercard (RFID) and an automated payment terminal.
 
## Overview

* **Objective**: To manipulate NFC transactions and replay them to deceive payment systems.
* **Method**: Attackers intercept legitimate NFC payment data and replay it later.
* **Impact**: Can lead to unauthorized transactions, financial losses, and compromised user trust.

## Mitigation Strategies

* Cryptographic Protections;
* Transaction Verification;
* User Awareness.


## Architectural Risk Analysis of NFC Payment Replay Vulnerability

The NFC Payment Replay Attack threatens the trust and security of digital wallets and contactless payment systems. Let’s assess this vulnerability using the Common Vulnerability Scoring System (CVSS) v3.1:

### CVSS Metrics
1. **Base Score**:
* **Attack Vector (AV)**: Network (N)
* **Attack Complexity (AC)**: Low (L)
* **Privileges Required (PR)**: None (N)
* **User Interaction (UI)**: None (N)
* **Scope (S)**: Unchanged (U)
* **Confidentiality Impact ©**: High (H)
* **Integrity Impact (I)**: Low (L)
* **Availability Impact (A)**: None (N)
* **Base Score**: 7.5 (High)
2. **Temporal Score**:
* **Exploit Code Maturity (E)**: Unproven (U)
* **Remediation Level (RL)**: Official Fix (O)
* **Report Confidence (RC)**: Confirmed ©
* **Temporal Score**: 7.5 (High)
3. **Environmental Score**:
* **Modified Attack Vector (MAV)**: Network (N)
* **Modified Attack Complexity (MAC)**: Low (L)
* **Modified Privileges Required (MPR)**: None (N)
* **Modified User Interaction (MUI)**: None (N)
* **Modified Scope (MS)**: Unchanged (U)
* **Modified Confidentiality (MC)**: High (H)
* **Modified Integrity (MI)**: Low (L)
* **Modified Availability (MA)**: None (N)
* **Environmental Score**: 7.5 (High)
### Risk Assessment
* **Severity**: High
* **Impact**: Data theft, credential compromise
* **Exploitability**: Low
* **Remediation Level**: Official Fix
* **Report Confidence**: Confirmed


*Remember, securing NFC payments requires a combination of technical safeguards and user vigilance*. 📲💳


## References

1. Njebiu, V., Kimwele, M., Rimiru, R., 2021. Secure contactless mobile payment system, in: 2021 IEEE Latin-American Conference on Communications (LATINCOM), IEEE, Santo Domingo, Dominican Republic. pp. 1–6. doi:10.1109/LATINCOM53176.2021.9647831.

## NFC Payment Replay Attacks Tree
