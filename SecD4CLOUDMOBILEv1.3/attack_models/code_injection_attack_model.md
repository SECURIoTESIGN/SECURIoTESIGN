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

| **Factor**                    | **Description**                                                                                | **Value**                                                                           |
|-------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Attack   Vector (AV):         | Network   (Exploiting application logic)                                                       | Network   (N)                                                                       |
| Attack   Complexity (AC):     | Medium   (Requires crafting malicious input)                                                   | Medium   (M)                                                                        |
| Privileges   Required (PR):   | None   (if vulnerability is user-facing)                                                       |         None (N) or Low (L) (if vulnerability requires some   user privilege)       |
| User   Interaction (UI):      | Required   (User needs to provide malicious input)                                             | Required   (R)                                                                      |
| Scope   (S):                  | Unauthorized   Access (attacker gains access to system)                                        |         Unauthorized Access (U)                                                     |
| Confidentiality   Impact (C): | High   (access to confidential data)                                                           | High   (H)                                                                          |
| Integrity   Impact (I):       | High   (attacker can modify data)                                                              | High   (H)                                                                          |
| Availability   Impact (A):    | High   (attacker can disrupt application functionality)                                        | High   (H)                                                                          |
| Base   Score:                 | 0.85   * (AV:N/AC:M/PR:N/UI:R) * (S:U/C:H/I:H/A:H)                                             | 9.0   (Critical)                                                                    |
| Temporal   Score (TS):        | Public   exploit code available?                                                               |         Depends on exploit availability                                             |
| Environmental   Score (ES):   | Depends   on application deployment (cloud vs on-device), user awareness, patching   practices | Varies                                                                              |
| Overall   CVSS Score          | Base   Score + TS + ES                                                                         |         Varies (Depends on TS & ES)                                                 |
| Risk   Rating                 | Based   on Overall CVSS Score                                                                  |         High to Critical (Depends on TS & ES)                                       |

### Mitigation
Mitigation strategies for Code Injection vulnerabilities typically include input validation, use of parameterized queries, and least privilege principle.


## References
1. O.S., J.N., Mary Saira Bhanu, S., 2018. A survey on code injection attacks in mobile cloud computing environment, in: 2018 8th International Conference on Cloud Computing, Data Science Engineering (Confluence)IEEE, Noida, India. pp. 1–6. doi:10.1109/CONFLUENCE.2018.8443032.

## Code Injection Attacks Diagram
