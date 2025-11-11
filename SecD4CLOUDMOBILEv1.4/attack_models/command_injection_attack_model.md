# Command Injection Attacks Model

This type of attack targets unvalidated and not properly sanitised user input, aiming to compromise the normal execution of a web application by causing an unintended exit. E.g., "an SQL Command injection attack occurs when a malicious user, through specifically crafted input, causes a web application to generate and send a query that functions differently than the programmer intended".

---

## Definition

This is a class of attacks to which web applications are susceptible, resulting from the semantic gap existing between database interpretation and web application interpretation, as well as from the inappropriate handling of user input. The negative technical impact of this type of attack is the execution of unauthorised commands, thus affecting the confidentiality, integrity and availability of the system. 

---

## Attack Categories

There are several variants of this type of attack:

* LDAP Injection;
* IMAP/SMTP Command Injection;
* XML Injection;
* Manipulating Writeable Terminal Devices;
* SQL Injectio; 
* NoSQL Injection;
* OS Command Injection.

--- 
 
## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **App Level**        | Avoid passing user input to system shells, use parameterized functions, validate and sanitize inputs. |
| **Cloud Services**   | Restrict shell access, isolate execution environments, monitor for anomalous command patterns. |
| **Mobile APIs**      | Enforce strict input validation, use allowlists, avoid dynamic command construction. |
| **IoT Firmware**     | Disable shell access unless essential, validate configuration inputs, encrypt telemetry. |
| **Security Testing** | Perform static and dynamic code analysis, fuzz testing, and penetration testing. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1–10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to full system compromise, data theft, and persistent backdoors.       | **9**            |
| **Reproducibility**  | Easily repeatable once vulnerability is discovered.                             | **8**            |
| **Exploitability**   | Moderate skill required; many known vectors and tools exist.                    | **7**            |
| **Affected Users**   | All users interacting with the compromised service or device.                   | **8**            |
| **Discoverability**  | Detectable with proper logging and monitoring, but often missed in early stages. | **8**            |

**Total DREAD Score: 40 / 5**; Rating: **High Risk**

---

## References

1. Su, Z., Wassermann, G., 2006. The essence of command injection attacks in web applications, in: Conference Record of the 33rd ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, Association for Computing Machinery, New York, NY, USA. p. 372–382. URL: https://doi.org/10.1145/1111037.1111070, doi:10.1145/1111037.1111070.
2. [CAPEC-248: Command Injection](https://capec.mitre.org/data/definitions/248.html).
3. [Mitre ATT&CK Framework – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
4. SANS Institute: Injection Attacks and Secure Coding Practices Whitepapers.
5. [OWASP Command Injection Guide](https://owasp.org/www-community/attacks/Command_Injection).

---

## Command Injection Attacks Diagram


