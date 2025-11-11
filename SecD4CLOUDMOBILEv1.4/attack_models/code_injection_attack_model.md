# Code Injection Attacks Model

This type of attack targets injecting malicious code into user inputs from the interface (web application forms or hybrid mobile applications) of applications written in HTML5.

---

## Definition

These types of applications are vulnerable to code injection attacks because of the possibility of merging the application data and implementation code. In case of hybrid mobile applications based on HTLM5, it has increased the attack vectors or channels such as, Contacts, SMS, Wi-Fi, NFC, QR Code, etc. This allows the attacker to inject malicious code to exhaust all the victim resources. A clear example of such an attack is XSS, already described in Subsection. 

---

## Attack Categories

 * Embedding Scripts within Scripts;
 * File Content Injection;
 * Using Meta-characters in E-mail Headers to Inject Malicious Payloads;
 * Cross-Site Scripting (XSS);
 * Cross-Browser Cross-Domain Theft.
 
---

## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **App Level**        | Validate and sanitize all user inputs, use allowlists, avoid dynamic code execution. |
| **Cloud Services**   | Restrict execution privileges, isolate runtime environments, monitor for anomalous behavior. |
| **Mobile APIs**      | Enforce strict input schemas, use parameterized calls, apply rate limiting.     |
| **IoT Firmware**     | Disable remote code execution features unless essential, validate firmware updates, use signed binaries. |
| **Security Testing** | Conduct static and dynamic code analysis, fuzz testing, and penetration testing. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to full system compromise, data exfiltration, and persistent backdoors. | **9**            |
| **Reproducibility**  | Easily repeatable once vulnerability is discovered.                             | **8**            |
| **Exploitability**   | Moderate skill required; many known vectors and tools exist.                    | **7**            |
| **Affected Users**   | All users interacting with the compromised service or device.                   | **8**            |
| **Discoverability**  | Detectable with proper logging and monitoring, but often missed in early stages. | **8**            |

**Total DREAD Score: 40 / 5**; Rating: **High Risk**

---

## References
1. O.S., J.N., Mary Saira Bhanu, S., 2018. A survey on code injection attacks in mobile cloud computing environment, in: 2018 8th International Conference on Cloud Computing, Data Science Engineering (Confluence)IEEE, Noida, India. pp. 1–6. doi:10.1109/CONFLUENCE.2018.8443032.
2. [OWASP Code Injection Guide](https://owasp.org/www-community/attacks/Code_Injection)
3. NIST SP 800-53: Security and Privacy Controls for Information Systems
4. ENISA Threat Landscape Report 2023 – [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
5. IEEE Security & Privacy: Code Injection in Cloud and Mobile Systems (2022)
6. [Mitre ATT&CK Framework – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
7. SANS Institute: Injection Attacks and Secure Coding Practices Whitepapers

---

## Code Injection Attacks Diagram
