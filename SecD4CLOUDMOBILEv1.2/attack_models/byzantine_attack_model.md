# Byzantine Attack 

### Byzantine Attack

A Byzantine attack is a type of cyber attack wherein the malicious attacker attempts to corrupt or disrupt normal operations within a network by broadcasting false messages throughout the system. The aim of the attack is to cause confusion and possible system failure by introducing messages that appear to be coming from genuine sources, but in reality are not. Such attacks are often employed in distributed computer networks, such as those used by banks, military organizations, and other critical systems.

## Byzantine Architectural Risk Analysis: 

# Architectural Risk Analysis of Byzantine Attack Vulnerability, according to Common Vulnerability Scoring System v3.1

| Metric | Value |
| --- | --- |
| Base Score | 7.2 |
| Attack Vector | Network (N) |
| Attack Complexity | Low (L) |
| Privileges Required | None (N) |
| User Interaction | None (N) |
| Scope | Unchanged (U) |
| Confidentiality Impact | High (H) |
| Integrity Impact | High (H) |
| Availability Impact | High (H) |
| Severity | Critical (CR) |

Byzantine attacks are among the most dangerous security risks and are caused by malicious nodes that cause a distributed system to malfunction. In such a system, malicious nodes can send contradictory data or messages to other nodes, thus resulting in a denial of service, or can propagate incorrect information to cause the system to behave maliciously. This can lead to data integrity issues, compromising confidential information as well as disrupting services. The Common Vulnerability Scoring System (CVSS) v3.1 assigns a Base Score of 7.2 to a Byzantine attack vulnerability. This score is determined by the parameters listed in the table above.

Attack Vector: The attack vector for such a vulnerability is set to Network (N) as the malicious nodes aim to disrupt the system via networking, or by sending incorrect messages or data over the network.

Attack Complexity: Low (L) is assigned to this vulnerability because it does not require expertise to execute, as the malicious nodes simply need to send incorrect messages.

Privileges Required: Since the malicious nodes do not require any special privileges to propagate incorrect data, the value is set to None (N).

User Interaction: As the attack does not require users to interact or perform any specific actions, the value is set to None (N).

Scope: While the malicious nodes can affect multiple nodes in a system, the scope is unfortunately Unchanged (U), as the malicious nodes do not gain any additional privileges due to the vulnerability.

Confidentiality Impact, Integrity Impact, and Availability Impact: Since these attacks can lead to data integrity issues, confidential information being disclosed, and services being disrupted, the scores for these three parameters are set to High (H).

Severity