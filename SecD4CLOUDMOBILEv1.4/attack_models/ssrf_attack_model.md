# SSRF Attacks

In this type of attack, which aims to force the server to make a request to itself, to services running on the server's internal network, or to external third parties, an attacker exploits the validation of improper entries by submitting malicious entries created to a server-side target application.


## Definition

We are in the presence of a Server Side Request Forgery Attack (SSRF) as long as the web application is vulnerable and redirects the attacker's requests to the internal network and exposes local services to the remote attacker, which introduces different forms of risks. According~\cite{10.1145/3412841.3442036}, this type of attack can exploit internal services in different ways, from sending spam emails to remotely executing operating system commands on servers that are running web applications. In case the vulnerable server (i.e. the server running the vulnerable web application) is hosted on a remote server in the Cloud, SSRF attacks require less effort from attackers, causing a higher impact in terms of dangerousness in terms of data leakage or theft. 

## Mitigation

1. **Input Validation**: Validate all user inputs to ensure they meet the expected format, length, and type. Reject any input that does not meet these criteria.

2. **Block Unsafe Protocols**: Block protocols that are known to be unsafe, such as `file://` or `dict://`. Only allow protocols that are necessary for your application.

3. **Use Allowlists**: Use allowlists for IP addresses and domains that your application can communicate with. Reject any request that is not on the allowlist.

4. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules.

5. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers.

6. **User Education**: Educate users about the risks of SSRF attacks and how to recognize them. This includes not providing sensitive information to untrusted sources.

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission.

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.M

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.

## SSRF Vulnerability Risk Analysis 

| **Factor**                                   | **Description**                                                                                                                                                                                                     | **Value**                                                                         |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Attack   Vector (AV):                        | Network   (Exploiting the mobile application)                                                                                                                                                                       | Network   (N)                                                                     |
| Attack   Complexity (AC):                    | Varies   (Low for basic attacks, High for complex pivoting)                                                                                                                                                         |         Low (L) to High (H)                                                       |
| Privileges   Required (PR):                  | None   (Attacker doesn't need privileges on the application)                                                                                                                                                        | None   (N)                                                                        |
| User   Interaction (UI):                     | Required   (User provides the malicious input)                                                                                                                                                                      | Required   (R)                                                                    |
| Scope   (S):                                 | Varies   (Depends on attacker capability and server permissions)                                                                                                                                                    |         Information Disclosure (attacker might gain internal   information)       |
| Confidentiality   Impact (C):                | High   (Attacker might access sensitive internal data)                                                                                                                                                              | High   (H)                                                                        |
| Integrity   Impact (I):                      | High   (Attacker might manipulate internal resources)                                                                                                                                                               | High   (H)                                                                        |
| Availability   Impact (A):                   | High   (Attacker might disrupt internal services)                                                                                                                                                                   | High   (H)                                                                        |
| Base   Score (assuming High impact for all): | 0.85   * (AV:N/AC:V/PR:N/UI:R) * (S:ID/C:H/I:H/A:H)                                                                                                                                                                 | 9.0   (Critical)                                                                  |
| Temporal   Score (TS):                       | Public   exploit code available for specific vulnerabilities?                                                                                                                                                       |         Depends on exploit availability                                           |
| Environmental   Score (ES):                  | Depends   on security measures in mobile app (input validation & sanitization),   cloud server configuration (restricting outbound traffic, whitelisting   allowed domains), intrusion detection/prevention systems | Varies                                                                            |
| Overall   CVSS Score                         | Base   Score + TS + ES                                                                                                                                                                                              |         Varies (Depends on TS & ES)                                               |
| Risk   Rating                                | High   to Critical (Depends on TS & ES)                                                                                                                                                                             | High   to Critical                                                                |

**Overall, SSRF vulnerabilities pose a high to critical risk in a mobile cloud-based application. Secure coding practices, input validation, and robust cloud server configuration are essential to reduce the risk of unauthorized access to internal resources, data breaches, and system disruptions.**


## References
1. Jabiyev, B., et al., 2021. Preventing Server-Side Request Forgery Attacks. Association for Computing Machinery, New York, NY, USA. p. 1626–1635. URL: https://doi.org/10.1145/3412841.3442036.800-63-3.pdf, doi:https://doi.org/10.6028/NIST.SP.800-63-3.
2. [CAPEC-664: Server Side Request Forgery](https://capec.mitre.org/data/definitions/664.html).

## SSRF Attack Tree Diagram


