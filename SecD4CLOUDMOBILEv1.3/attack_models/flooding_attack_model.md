# Flooding Attack 

Flooding attacks are attempts to inundate a resource with an overwhelming amount of data or requests in order to overwhelm or crash it. Flooding attacks are often effective when the target resource is limited in bandwidth or processing power, such as a server, and is unable to handle so much data or requests, resulting in performance degradation or service disruption.

Examples of flooding attacks include Denial-of-Service (DoS) attacks, which send an extremely large amount of requests/traffic to the victim’s server or network in order to saturate it and make it incapable of responding to legitimate requests. Additionally, there is also the Distributed Denial-of-Service (DDoS) attack, which uses more than one computer or device to send the traffic, making it even more of a challenge to defend against.

Flooding attacks can be difficult to detect and stop as they often involve huge volumes of data. However, some steps to help mitigate the effects of flooding attacks include:

* Utilizing firewalls and other security measures to detect and block suspicious traffic.
* Deploying load balancers to distribute the amount of requests over multiple servers or resources.
* Monitoring network and server performance to detect anomalies.
* Limiting connection requests from a single source.

## Flooding Architectural Risk Analysis: 

**Common Vulnerability Scoring System (CVSS) v3.1 - Risk Analysis of Flooding Vulnerability**

Base Score: 7.2

Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H

|Sub-metrics|Value|Weight|Score|
|---|---|---|---|
|Attack Vector | Local (AV:L) | 04.7 | 0.2 |
|Attack Complexity | Low (AC:L) | 03.9 | 0.2 |
|Privileges Required | Low (PR:L) | 05.2 | 0.2 |
|User Interaction | None (UI:N) | 0 | 0 |
|Scope | Changed (S:C) | 07.7 | 0.3 |
|Confidentiality | High (C:H) | 06.4 | 0.3 |
|Integrity | High (I:H) | 05.9 | 0.3 |
|Availability | High (A:H) | 05.9 | 0.3 |

**Impact Score:** 7.2

**Exploitability Score**: 4.7

**CVSS v3.1 Risk Rating:** High (Priority Level 3)