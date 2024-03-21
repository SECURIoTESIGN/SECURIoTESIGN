# SSRF Attacks

In this type of attack, which aims to force the server to make a request to itself, to services running on the server's internal network, or to external third parties, an attacker exploits the validation of improper entries by submitting malicious entries created to a server-side target application.


## Definition

We are in the presence of a Server Side Request Forgery Attack (SSRF) as long as the web application is vulnerable and redirects the attacker's requests to the internal network and exposes local services to the remote attacker, which introduces different forms of risks. According~\cite{10.1145/3412841.3442036}, this type of attack can exploit internal services in different ways, from sending spam emails to remotely executing operating system commands on servers that are running web applications. In case the vulnerable server (i.e. the server running the vulnerable web application) is hosted on a remote server in the Cloud, SSRF attacks require less effort from attackers, causing a higher impact in terms of dangerousness in terms of data leakage or theft. 

 ## Risk Architectural Analysis: SSRF Vulnerability

### CVSS v3.1 Metrics

#### Attack Vector (AV)
Network (N)

#### Attack Complexity (AC)
Low (L)

#### Privileges Required (PR)
None (N)

#### User Interaction (UI)
None (N)

#### Scope (S)
Changed (C)

#### Confidentiality (C)
High (H)

#### Integrity (I)
High (H)

#### Availability (A)
Low (L)

### CVSS v3.1 Base Score
The base score is calculated based on the above metrics. For an SSRF vulnerability with these metrics, the base score would typically be high.

### Impact
SSRF vulnerabilities can have a significant impact on the confidentiality and integrity of the system. An attacker could potentially make requests to internal resources, leading to unauthorized access to sensitive data or modification of data.

### Mitigation
Mitigation strategies for SSRF vulnerabilities typically include input validation, use of allow-lists for outbound connections, and least privilege principle.


## References
1. Jabiyev, B., et al., 2021. Preventing Server-Side Request Forgery Attacks. Association for Computing Machinery, New York, NY, USA. p. 1626–1635. URL: https://doi.org/10.1145/3412841.3442036.800-63-3.pdf, doi:https://doi.org/10.6028/NIST.SP.800-63-3.
2. [CAPEC-664: Server Side Request Forgery](https://capec.mitre.org/data/definitions/664.html).

## SSRF Attacks Diagram


