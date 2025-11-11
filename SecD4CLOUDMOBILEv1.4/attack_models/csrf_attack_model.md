# Cross-Site Request Forgery Attacks Model

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to perform unwanted actions in an application in which they are currently authenticated.

## Definition
The purpose of this type of attack is to change state and not to steal data, since the attacker is prevented from seeing the response to the falsified request. The necessary for this type of attack to succeed is the existence of permission to make changes via GET requests.

---

## Mitigation Strategies

Strict measures should be taken to ensure that the web application is not vulnerable to the CSRF attack. The following approaches can be taken for protecting against CSRF attack:

1. **Use of Anti-CSRF Tokens**: Implement anti-CSRF tokens in your application. These tokens can be added to forms and AJAX calls and validated on the server. Since the token is unique for each session, it makes it difficult for an attacker to forge a request.

2. **Same-Site Cookies**: Use SameSite cookie attribute which allows you to declare if your cookie should be restricted to a first-party or same-site context. This can help to prevent CSRF attacks by making it impossible for a browser to send a cookie along with cross-site requests.

3. **Checking HTTP Headers**: Many CSRF attacks are done via AJAX from a different domain, which typically do not include certain headers that are included in same-domain requests. Checking for these headers on the server can be a good way to block CSRF attacks.

4. **User Interaction**: Require user interaction for sensitive actions. For example, you could require the user to re-enter their password or use a CAPTCHA.

5. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers.

6. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules.

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission.

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.


---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to unauthorized actions, data loss, or device manipulation.            | **8**            |
| **Reproducibility**  | Easily repeatable with crafted links or forms.                                 | **8**            |
| **Exploitability**   | Low to moderate skill required; many tools and templates exist.                 | **7**            |
| **Affected Users**   | Any authenticated user interacting with vulnerable services.                    | **7**            |
| **Discoverability**  | Often undetected unless logs are reviewed or user reports anomalies.            | **7**            |

**Total DREAD Score: 37 / 5 = 7.4**; Rating: **High Risk**.

---

## References

1. [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).
2. NIST SP 800-63B: Digital Identity Guidelines.
3. ENISA Threat Landscape Report 2023 - [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications).
4. IEEE Security & Privacy: CSRF in Mobile and Cloud Applications (2022).
5. [Mitre ATT&CK Framework - Web Session Manipulation](https://attack.mitre.org).
6. SANS Institute: Web Application Security and CSRF Defense Whitepapers.

---

## CSRF Attack Tree Diagram