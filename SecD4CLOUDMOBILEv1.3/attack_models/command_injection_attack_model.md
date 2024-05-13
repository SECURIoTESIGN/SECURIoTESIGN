# Command Injection Attacks

This type of attack targets unvalidated and not properly sanitised user input, aiming to compromise the normal execution of a web application by causing an unintended exit. E.g., "an SQL Command injection attack occurs when a malicious user, through specifically crafted input, causes a web application to generate and send a query that functions differently than the programmer intended".


## Definition

This is a class of attacks to which web applications are susceptible, resulting from the semantic gap existing between database interpretation and web application interpretation, as well as from the inappropriate handling of user input. The negative technical impact of this type of attack is the execution of unauthorised commands, thus affecting the confidentiality, integrity and availability of the system. There are several variants of this type of attack:

* LDAP Injection;
* IMAP/SMTP Command Injection;
* XML Injection;
* Manipulating Writeable Terminal Devices;
* SQL Injectio; 
* NoSQL Injection;
* OS Command Injection. 
 
## Technical Impact or Attack Powers

* Modify and Read Data;
* Gain Privileges;
* Bypass Protection Mechanism;
* Unreliable Execution; 
* Execute Unauthorized Commands.

## Risk Architectural Analysis: Command Injection Vulnerability

### CVSS v3.1 Metrics

| **Factor**                    | **Description**                                                                                          | **Value**                                     |
|-------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Attack   Vector (AV):         | Network   (Exploiting application logic)                                                                 | Network   (N)                                 |
| Attack   Complexity (AC):     | Medium   (Requires crafting malicious input)                                                             | Medium   (M)                                  |
| Privileges   Required (PR):   | Low   (Requires some privilege to execute commands)                                                      | Low   (L)                                     |
| User   Interaction (UI):      | Required   (User needs to provide malicious input)                                                       | Required   (R)                                |
| Scope   (S):                  | Unauthorized   Access (attacker gains access to system)                                                  |         Unauthorized Access (U)               |
| Confidentiality   Impact (C): | High   (access to confidential data on the server)                                                       | High   (H)                                    |
| Integrity   Impact (I):       | High   (attacker can modify system files)                                                                | High   (H)                                    |
| Availability   Impact (A):    | High   (attacker can disrupt system functionality)                                                       | High   (H)                                    |
| Base   Score:                 | 0.85   * (AV:N/AC:M/PR:L/UI:R) * (S:U/C:H/I:H/A:H)                                                       | 9.0   (Critical)                              |
| Temporal   Score (TS):        | Public   exploit code available?                                                                         |         Depends on exploit availability       |
| Environmental   Score (ES):   | Depends   on application permissions (access to sensitive systems), user awareness,   patching practices | Varies                                        |
| Overall   CVSS Score          | Base   Score + TS + ES                                                                                   |         Varies (Depends on TS & ES)           |

## Impact
Command Injection vulnerabilities can have a significant impact on the confidentiality, integrity, and availability of the system. An attacker could potentially execute arbitrary commands, leading to unauthorized access to sensitive data, modification of data, or disruption of the service.

## Mitigation
Mitigation strategies for Command Injection vulnerabilities typically include input validation, use of secure APIs, and least privilege principle.

Please consult with a security professional to get accurate risk and mitigation strategies for your specific context.
 
## Recommendations

In order to ensure that the mobile application is resilient or immune to the Command Injection attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. Su, Z., Wassermann, G., 2006. The essence of command injection attacks in web applications, in: Conference Record of the 33rd ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, Association for Computing Machinery, New York, NY, USA. p. 372–382. URL: https://doi.org/10.1145/1111037.1111070, doi:10.1145/1111037.1111070.
2. [CAPEC-248: Command Injection](https://capec.mitre.org/data/definitions/248.html).

## Command Injection Attacks Diagram


