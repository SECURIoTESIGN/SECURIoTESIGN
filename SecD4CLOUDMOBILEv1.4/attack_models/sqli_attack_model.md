# SQL Injection Attacks Model

In this type of attack, an attacker could provide malicious input with a clever mix of characters and meta characters from a form (e.g., login form) to alter the logic of the SQL command.

---

## Definition

Structured Query Language (SQL) Injection Attack is a code injection technique commonly used to attack web applications where an attacker enters SQL characters or keywords into an SQL statement through superuser input parameters for the purpose to change the logic of the desired query.

---

## Attack Categories

| **Category**               | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Classic SQL Injection**  | Injects malicious SQL via input fields to manipulate database queries.          |
| **Blind SQL Injection**    | Exploits queries that do not return data directly, using timing or Boolean logic.|
| **Out-of-Band Injection**  | Uses external channels (e.g., DNS, HTTP) to extract data when direct responses are blocked. |
| **Mobile API Injection**   | Targets insecure mobile endpoints that pass user input directly to SQL queries. |
| **IoT Telemetry Injection**| Injects SQL via telemetry or device metadata fields to compromise backend systems. |

---

## Mitigation

1. **Input Validation**: Validate input data thoroughly. Use a whitelist of accepted characters, and reject any input that contains characters not on the list;

2. **Parameterized Queries**: Use parameterized queries or prepared statements to ensure that input data is treated as literal values and not executable code;

3. **Least Privilege Principle**: Limit the privileges of database accounts used by web applications. Do not use the database root account, and do not grant more privileges than necessary to a user account;

4. **Regular Software Updates**: Keep all software, including operating systems, databases, and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers;

5. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules;

6. **User Education**: Educate users about the risks of SQL Injection attacks and how to recognize them. This includes not providing sensitive information to untrusted sources;

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission;

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions;
9. Conduct regular security audits and penetration testing.

---

## SQL Injection Risk Assessment (DREAD Model)

SQL Injection is a critical vulnerability that allows attackers to manipulate backend SQL queries through unsanitized user input. Below is a risk assessment using the DREAD framework.

| **Category**         | **Description**                                                                                     | **Score (1-10)** |
|----------------------|-----------------------------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to full database compromise, data theft, deletion, or remote code execution.               | **9**            |
| **Reproducibility**  | Easily repeatable once discovered; attack patterns are well-known and widely documented.            | **8**            |
| **Exploitability**   | Requires minimal skill; automated tools like sqlmap make exploitation trivial.                      | **9**            |
| **Affected Users**   | Can impact all users whose data resides in the compromised database.                                | **8**            |
| **Discoverability**  | Highly discoverable via manual testing or automated scanners; common in public-facing applications. | **9**            |

**Total DREAD Score: 43 / 5 = 8.6**.

This places SQL Injection in the **high-risk category**, requiring immediate mitigation.

---

## References

1. [OWASP SQL Injection Guide](https://owasp.org/www-community/attacks/SQL_Injection)
2. NIST SP 800-53: Security and Privacy Controls for Information Systems
3. ENISA Threat Landscape Report 2023 – [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
4. IEEE Security & Privacy: SQL Injection in Cloud-Native Applications (2022)
5. [Mitre ATT&CK Framework - SQL Injection](https://attack.mitre.org/techniques/T1505/)
6. SANS Institute: Database Security and Injection Attacks Whitepapers

---

## SQLi Attack Tree Diagram
