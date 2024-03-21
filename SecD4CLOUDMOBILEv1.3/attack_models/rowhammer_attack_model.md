# Rowhammer Attack 

Rowhammer is a security exploit that takes advantage of a hardware weakness in some modern computer memory chips. It is a side-channel attack wherein a malicious program can cause a targeted memory cell to change its content, resulting in data corruption or a system crash. In recent years, Rowhammer attacks have become increasingly popular, as attackers can exploit them to gain access to otherwise secure systems or networks.

## Rowhammer Architectural Risk Analysis 

## Architectural Risk Analysis of Rowhammer Attack Vulnerability

The Common Vulnerability Scoring System (CVSS) v3.1 is used to provide an architectural risk analysis of the Rowhammer attack vulnerability.

| Base Vector | Metrics | Details | Value |
| --- | --- | --- | --- |
| Access Vector | AV:N | Local | 0.85 | 
| Access Complexity | AC:L | Low | 0.77 | 
| Privileges Required | PR:N | None | 0.85 | 
| User Interaction | UI:N | None | 0.85 | 
| Scope | S:U | Unchanged | 0.00 |  
| Confidentiality Impact | C:H | High | 0.56 | 
| Integrity Impact | I:N | None | 0.85 | 
| Availability Impact | A:N | None | 0.85 |
| Exploit Code Maturity | E:F | Functional | 0.96 | 
| Remediation Level | RL: OF | Official Fix | 0.90 |
| Report Confidence | RC: UC | Unknown Confidence | 0.90 |

Therefore, the CVSS v3.1 Base Score is **6.5** which is considered medium severity risk.

## Rowhammer Attack Tree 