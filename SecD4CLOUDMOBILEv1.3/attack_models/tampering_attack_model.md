# Tampering Attack 

A tampering attack is a type of malicious attack whereby an attacker attempts to alter or modify data that is transmitted between two nodes. It is a type of attack in which the attacker attempts to modify or corrupt data in order to cause harm or gain unauthorized access to sensitive information. Tampering attacks can target all types of web applications, including web APIs and databases.

Tampering attacks can include activities such as: 

- Injecting malicious code into a web page or API response
- Modifying network traffic by altering or deleting packets
- Intercepting and manipulating requests and responses
- Corrupting data stored in memory or on disk
- Altering parameters or headers in requests
- Injecting malicious JavaScript or HTML into an application
- Manipulating browsers’ cookies or local storage
- Exploiting weaknesses in authorization and authentication protocols

## Tampering Architectural Risk Analysis: 

#### Architectural Risk Analysis of Tampering Vulnerability

| Vulnerability | Score |Description |
| -- | -- | -- |
| Attack Vector (AV) |Low (2)| Attack requires local access to user environment such as local network. |
| Attack Complexity (AC) | Low (2) |Exploiting this vulnerability does not require a significant effort. |
| Privileges Required (PR) |Low (2) |Only local user privileges are required. |
| User Interaction (UI) |None (0)|No user interaction is required. |
| Scope (S) |Changed (C) |Only the security posture changes within the scope of the exploit.|
| Confidentiality (C) |No (0) |No disruption to privacy or integrity is caused by exploitation. |
| Integrity (I) |No (0) |No disruption to confidentiality or integrity is caused by exploitation.|
| Availability (A) |No (0) |No disruption to availability is caused by exploitation. |
| Overall CVSS Score: | 4 | Low Severity | 


This vulnerability is given a low severity rating of 4 on the Common Vulnerability Scoring System v3.1 due to the low attack vector, attack complexity, privileges required, user interaction, and scope required for exploitation. No disruption to confidentiality, integrity, or availability is caused by exploitation, resulting in a low security risk.