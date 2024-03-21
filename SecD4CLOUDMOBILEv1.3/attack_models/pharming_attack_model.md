# Pharming Attacks

A pharming attack is a form of cyberattack that redirects victims to fake websites, often without their knowledge. Let’s explore the details:

## Overview

* **Objective**: Trick users into visiting malicious websites that resemble legitimate ones.
* **Method**: Exploits the Domain Name System (DNS) to redirect users to spoofed sites.
* **Impact**: Can lead to data theft, credential harvesting, and financial fraud.

## How Pharming Works
1. **Malware-Based Pharming**:
* Users unknowingly acquire malware (e.g., Trojan horse or virus) via malicious emails or software downloads.
* The malware modifies locally hosted files and changes stored IP addresses.
* Victims are automatically redirected to the attacker’s fraudulent website when accessing the legitimate site.
2. DNS Server Poisoning:
* Corrupts DNS servers to direct website requests to alternate or fake IP addresses.
* Exploits vulnerabilities at the DNS server level.
* Users visit spoofed sites, believing they are legitimate.

## Consequences

1. Communication Disruption:
* Interrupts access to legitimate websites.
* Impacts online services, including banking and e-commerce.
1. Data Theft and Credential Harvesting:
* Attackers collect personal data, login credentials, and financial information.
* Victims unwittingly provide sensitive details on fake sites.

## Mitigation Strategies

1. Regular Security Updates:
* Keep software, browsers, and security tools up to date.
* Patch vulnerabilities to prevent exploitation.
2. DNS Security Measures:
* Implement DNSSEC (DNS Security Extensions) to verify DNS responses.
* Monitor DNS traffic for anomalies.
3. User Education:
* Train users to recognize phishing attempts and suspicious URLs.
* Encourage caution when clicking links or entering credentials.

## Architectural Risk Analysis of Pharming Vulnerability

The pharming attack targets users by redirecting them to fraudulent websites, often without their knowledge. Let’s assess the risk using the Common Vulnerability Scoring System (CVSS) v3.1:

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

### Mitigation Strategies

1. **DNS Security Measures**:
 * Implement DNSSEC (DNS Security Extensions) to verify DNS responses.
 * Monitor DNS traffic for anomalies.
2. **User Education**:
 * Train users to recognize phishing attempts and suspicious URL.
 * Encourage caution when clicking links or entering credentials.

*Remember, vigilance and proactive measures are essential to protect against pharming attacks.*
 
## Pharming Attack Tree