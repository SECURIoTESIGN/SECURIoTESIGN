# VM Escape Attack 

VM (Virtual Machine) Escape attacks involve compromised VMs that act as an entry point for an intruder to gain access to the larger system. It occurs when attackers use vulnerabilities or misconfigurations to escape the confines of a virtual machine and gain access to the underlying physical server or network. Through this attack, attackers can gain control of the physical server and execute malicious activities such as stealing data, disrupting service, and deleting critical files.

These attacks are especially dangerous since they bypass security measures, including firewalls, that are typically in place to protect physical servers and networks. Therefore, it is important for organizations to be vigilant and implement measures to protect against VM escape attacks. One way of doing this is by keeping VMs updated and running the latest security patches. Additionally, limiting the access and privileges of VMs can also help to reduce the attack surface.

## VM Escape Architectural Risk Analysis: 

#### **VM Escape Vulnerability**

Common Vulnerability Scoring System (CVSS) v3.1 provides a way for users to objectively score and rank the severity of a vulnerability.

CVSS v3.1 Base Score: 8.1

CVSS v3.1 Vector: AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H

- **Attack Vector (AV):** Network (N)
- **Attack Complexity (AC)**: Low (L)
- **Privileges Required (PR)**: High (H)
- **User Interaction (UI)**: None (N)
- **Scope (S)**: Unchanged (U)
- **Confidentiality (C)**: High (H)
- **Integrity (I)**: High (H)
- **Availability (A)**: High (H)

This vulnerability has a high base score of 8.1, which indicates that if exploited, it could have a significant impact on the system. Additionally, there is no user interaction required, and the scope, confidentiality, integrity, and availability of the system would all be affected. All of these factors indicate that this vulnerability can have serious consequences and must be addressed.

## VM Escape Attack Tree