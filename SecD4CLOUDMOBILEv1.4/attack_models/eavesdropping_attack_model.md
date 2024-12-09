# Eavesdropping Attack 

Eavesdropping attack is a type of network attack in which the attacker listens to the conversations taking place among two or more authorized users or devices on the same network. This attack allows attackers to collect valuable information, including private data and confidential messages, without being detected. 

In this attack, the attacker uses various tools to gain access to the target computer's network, such as sniffers, which are essentially network-based packet sniffers that extract data from the network, and Trojan horses, malicious programs that are secretly installed on the system. The attacker can also use other methods to access the network, such as phishing emails, rogue Wi-Fi access points, and man-in-the-middle attacks.

Once the attacker gains access to the network, they eavesdrop on the conversations taking place on the network. By monitoring the data packets being sent over the network, the attacker can gain access to sensitive information and data that they can then use for malicious purposes.

## Mitigation

1. **Use Secure Communication Protocols:** Always use secure communication protocols such as HTTPS (Hypertext Transfer Protocol Secure) for data in transit. This ensures that the data is encrypted and cannot be easily intercepted by eavesdroppers.
2. **Data Encryption:** Encrypt sensitive data at rest and in transit. Use strong encryption algorithms and manage encryption keys securely;
3. **Secure Wi-Fi Networks:** Encourage users to only use secure and trusted Wi-Fi networks. Public Wi-Fi networks can be a hotbed for eavesdropping attacks;
4. **VPN:** Use a Virtual Private Network (VPN) for a more secure connection. A VPN can provide a secure tunnel for all data being sent and received;
5. **Regularly Update and Patch:** Ensure that the cloud and mobile applications are regularly updated and patched. This helps to fix any known vulnerabilities that could be exploited by attackers;
5. **Access Controls:** Implement strict access controls. Only authorized users should have access to sensitive data;
6. **Security Headers:** Implement security headers like HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), etc. These headers add an extra layer of protection against eavesdropping attacks;
7. **Security Testing:** Regularly conduct security testing such as penetration testing and vulnerability assessments to identify and fix any security loopholes;
8. **User Awareness:** Educate users about the risks of eavesdropping attacks and how they can protect themselves. This includes not opening suspicious emails or clicking on unknown links, and only downloading apps from trusted sources;
9. **Incident Response Plan:** Have an incident response plan in place. This will ensure that you are prepared to respond effectively in case an eavesdropping attack does occur.

## Eavesdropping Architectural Risk Analysis: 

Common Vulnerability Scoring System (CVSS) v3.1 score for Eavesdropping Vulnerability is 4.8, categorized under 'High' severity.

| **Factor**                                    | **Description**                                                          | **Value**                                                       |
|-----------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| Attack   Vector (AV):                         | Network                                                                  | Network   (N)                                                   |
| Attack   Complexity (AC):                     | Low                                                                      | Low   (L)                                                       |
| Privileges   Required (PR):                   | None                                                                     | None   (N)                                                      |
| User   Interaction (UI):                      | None                                                                     | None   (N)                                                      |
| Scope   (S):                                  | Confidentiality   Impact (attacker can intercept communication)          |         Confidentiality (C)                                     |
| Confidentiality   Impact (C):                 | High   (if unencrypted data is transmitted)                              | High   (H)                                                      |
| Confidentiality   Impact (C):                 | Low   (if data is strongly encrypted in transit)                         | Low   (L)                                                       |
| Integrity   Impact (I):                       | Low   (unless eavesdropping allows data manipulation)                    | Low   (L)                                                       |
| Availability   Impact (A):                    | None                                                                     | None   (N)                                                      |
| Base   Score (assuming High Confidentiality): | High   (if unencrypted data is transmitted)                              |         3.5 (Medium) or 1.0 (Low) depending on Encryption       |
| Temporal   Score (TS):                        | Not   applicable                                                         | N/A                                                             |
| Environmental   Score (ES):                   | Depends   on network security measures, data sensitivity, user awareness | Varies                                                          |
| Overall   CVSS Score                          | Base   Score + TS + ES                                                   |         High (H)                                                |
| Risk   Rating                                 | Based   on Overall CVSS Score                                            |         High (H)                                                |


Eavesdropping Vulnerability poses a high risk to the confidentiality of the data traveling within a network as it allows attackers to intercept and potentially access sensitive information. Without any user interaction, an attacker can intercept information and potentially gain unrestricted access to the confidential data, thus leaving the users’ online operations prone to manipulation. Moreover, the integrity and availability of the network can be impacted to a low extent.
 
Therefore, organizations need to put in place an effective counter-measures strategy which focuses on enhancing data security measures, including the adoption of strong authentication protocols and encryption technologies, to mitigate and reduce the risk of eavesdropping attacks.

## Eavesdropping Attack Tree Diagram