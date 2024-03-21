# SQLi Attack 

Malicious QR Code attack is a form of cyber attack that takes advantage of Quick Response (QR) codes to perpetrate malicious activities. This type of attack works by embedding malicious code into QR codes that lead unsuspecting victims to malicious websites or applications when scanned. These malicious QR codes can be found in physical locations, such as on printed ads, posters, or packaging, or they can be sent electronically through email, text, or social media. If a victim unwittingly scans the malicious QR code, the malicious code embedded within it will be executed and could result in malicious activities such as data harvesting, installation of malware, or other malicious activities. Victims of malicious QR code attacks should always exercise caution when interacting with QR codes as they could lead to malicious websites and activities.

## Malicious SQLi Architectural Risk Analysis: 

### Arquitectural Risk Analysis of SQLi Vulnerability

**Common Vulnerability Scoring System v3.1:**

| Metric | Score | 
| :--- | :--- | 
| Attack Vector | Network (AV:N) | 
| Attack Complexity | Low (AC:L) | 
| Privileges Required | None (PR:N) | 
| User Interaction | None (UI:N) | 
| Scope | Changed (S:C) | 
| Confidentiality | High (C:H) | 
| Integrity | High (I:H) | 
| Availability | High (A:H) | 

**Overall Score: 9.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)**

SQLi Vulnerability presents a high risk arquitecture due to its potential negative consequences upoming from its exploitation, according to the [Common Vulnerability Scoring System v3.1](https://www.first.org/cvss/v3.1/), the impact of this vulnerability is rated as a 9.3. 

The Attack Vector score is Network (AV:N), meaning that the vulnerability exploit is deleivered through the network, such as Internet or an internal network, requiring no user interaction. The Attack Complexity score is Low (AC:L), implying that the vulnerability can be exlpoited with little effort and/or knowledge. The Privileges Required score is None (PR:N) so no privileged access is neccessary to exploit the vulnerability. The User Interaction score is None (UI:N), meaning that no user interaction is needed for the exploitation of this vulnerability. The Scope score is Changed (S:C), meaning that the risk affects other resources in the system due to the unauthorized access.

The Confidentiality score is High (C:H) because the attacker can find private information as a result of exploitation of SQLi Vulnerability, so providing access to confidential information could have a major impact. The Integrity score is High (I:H) because the attacker is able to modify or even delete private information which greatly impacts the integrity of the system. The Availability score is