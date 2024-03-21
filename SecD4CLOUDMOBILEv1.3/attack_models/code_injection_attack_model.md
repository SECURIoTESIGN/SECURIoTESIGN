# Code Injection Attacks

This type of attack targets injecting malicious code into user inputs from the interface (web application forms or hybrid mobile applications) of applications written in HTML5.


## Definition

These types of applications are vulnerable to code injection attacks because of the possibility of merging the application's data and implementation code. In case of hybrid mobile applications based on HTLM5, it has increased the attack vectors or channels such as, Contacts, SMS, Wi-Fi, NFC, QR Code, etc. This allows the attacker to inject malicious code to exhaust all the victim's resources. A clear example of such an attack is XSS, already described in Subsection. 

 * Embedding Scripts within Scripts;
 * File Content Injection;
 * Using Meta-characters in E-mail Headers to Inject Malicious Payloads;
 * Cross-Site Scripting (XSS);
 * Cross-Browser Cross-Domain Theft.
 
## Risk Architectural Analysis: Code Injection Vulnerability

### CVSS v3.1 Metrics

#### Attack Vector (AV)
Network (N)

#### Attack Complexity (AC)
Low (L)

#### Privileges Required (PR)
None (N)

#### User Interaction (UI)
Required (R)

#### Scope (S)
Unchanged (U)

#### Confidentiality (C)
High (H)

#### Integrity (I)
High (H)

#### Availability (A)
High (H)

### CVSS v3.1 Base Score
The base score is calculated based on the above metrics. For a Code Injection vulnerability with these metrics, the base score would typically be high.

### Impact
Code Injection vulnerabilities can have a significant impact on the confidentiality, integrity, and availability of the system. An attacker could potentially execute arbitrary code, leading to unauthorized access to sensitive data, modification of data, or disruption of the service.

### Mitigation
Mitigation strategies for Code Injection vulnerabilities typically include input validation, use of parameterized queries, and least privilege principle.


## References
1. O.S., J.N., Mary Saira Bhanu, S., 2018. A survey on code injection attacks in mobile cloud computing environment, in: 2018 8th International Conference on Cloud Computing, Data Science Engineering (Confluence)IEEE, Noida, India. pp. 1–6. doi:10.1109/CONFLUENCE.2018.8443032.

## Code Injection Attacks Diagram


