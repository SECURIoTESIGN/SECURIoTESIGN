# Cross Site Request Forgery Attacks

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to perform unwanted actions in an application in which they are currently authenticated.

## Definition
The purpose of this type of attack is to change state and not to steal data, since the attacker is prevented from seeing the response to the falsified request. The necessary for this type of attack to succeed is the existence of permission to make changes via GET requests.

## Mitigation Strategies

Strict measures should be taken to ensure that the web application is not vulnerable to the CSRF attack. The following approaches can be taken for protecting against CSRF attack:

1. **Use of Anti-CSRF Tokens**: Implement anti-CSRF tokens in your application. These tokens can be added to forms and AJAX calls and validated on the server. Since the token is unique for each session, it makes it difficult for an attacker to forge a request.

2. **Same-Site Cookies**: Use SameSite cookie attribute which allows you to declare if your cookie should be restricted to a first-party or same-site context. This can help to prevent CSRF attacks by making it impossible for a browser to send a cookie along with cross-site requests.

3. **Checking HTTP Headers**: Many CSRF attacks are done via AJAX from a different domain, which typically don't include certain headers that are included in same-domain requests. Checking for these headers on the server can be a good way to block CSRF attacks.

4. **User Interaction**: Require user interaction for sensitive actions. For example, you could require the user to re-enter their password or use a CAPTCHA.

5. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers.

6. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules.

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission.

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.

## CSRF Arquitectural Risk Analysis: 

In accordance with Common Vulnerability Scoring System (CVSS) v3.1, the arquitectural risk analysis of cross site request forgery (CSRF) vulnerability will focus on the following metrics:

| **Factor**                  | **Description**                                                                                                    | **Value**                           |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Attack Vector (AV):         | Network                                                                | Network (N)                         |
| Attack Complexity (AC):     | Low                                                                | Low (L)                             |
| Privileges Required (PR):   | None                                                                   | None (N)                            |
| User Interaction (UI):      | Required                                            | Required (R)                        |
| Scope (S):                  | Unchanged                                     | Unauthorized Access (U)             |
| Confidentiality Impact (C): | High                                                            | High (H)                            |
| Integrity Impact (I):       | High                                                                              | High (H)                            |
| Availability Impact (A):    | Medium                                   | Medium (M)                          |
| Base Score:                 | High                                                                   | 7.1 (High) |
| Risk Rating                 | Based on Overall CVSS Score                                                                                        | High (Depends on TS & ES) |
 
The high vector severity indicates that the vulnerability has a high potential for exploitation and should be addressed with an urgency. 
This risk should be remediated immediately, as exploiting the vulnerability may result in malicious code execution, data manipulation/corruption, and other undesired system behaviors. It is recommended to implement mitigating technologies, such as input and output validation, content security policies, and request tokens to reduce the risk associated with this vulnerability.

## CSRF Attack Tree Diagram