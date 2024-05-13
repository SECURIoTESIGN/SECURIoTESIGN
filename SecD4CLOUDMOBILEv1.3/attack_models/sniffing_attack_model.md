# Sniffing Attack 

Sniffing attack is a type of cyber attack in which attackers gain unauthorized access to a network by using methods to capture, monitor, and control data packets in a network. In this attack, malicious users capture data that is being transmitted over the network, such as usernames, passwords, and other sensitive information. This is done by sniffing or intercepting packets of data as they pass through the network and capturing them for further analysis. The attackers can then use the data gathered to gain access to networks or to commit data theft.

## Mitigation

1. **Encryption**: Use encryption for all data in transit. Protocols such as HTTPS, SSL, and TLS can provide secure communication channels and prevent sniffing;

2. **Virtual Private Networks (VPNs)**: Use VPNs for secure communication over the internet. VPNs create an encrypted tunnel for data transmission, which is difficult for sniffers to penetrate;

3. **Secure Wi-Fi**: Use secure Wi-Fi protocols such as WPA2 or WPA3. Avoid using WEP as it is outdated and vulnerable to sniffing attacks;

4. **Firewalls**: Implement firewalls to block unauthorized access to your network. Firewalls can also be used to block ports that are commonly used for sniffing;

5. **Intrusion Detection Systems (IDS)**: Use IDS to detect unusual network traffic patterns. IDS can help in identifying potential sniffing attacks;

6. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers;

7. **User Education**: Educate users about the risks of connecting to unsecured networks where sniffing attacks are more likely to occur;

8. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission;

9. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.


## Sniffing Architectural Risk Analysis: 

| **Factor**                                                      | **Description**                                                                                                 | **Value**                            |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Attack   Vector (AV):                                           | Network   (Exploiting weaknesses in network security)                                                           | Network   (N)                        |
| Attack   Complexity (AC):                                       | Low   (Relatively simple tools can be used to sniff unencrypted traffic)                                        | Low   (L)                            |
| Privileges   Required (PR):                                     | Varies   (Physical proximity for some networks, but could be remote for misconfigured   cloud environments)     |         None (N) to Low (L)          |
| User   Interaction (UI):                                        | None   (Attack might not require user interaction)                                                              | None   (N)                           |
| Scope   (S):                                                    | Varies   (Depends on the data being sniffed)                                                                    |         Confidentiality (C)          |
| Confidentiality   Impact (C):                                   | High   (Sniffed data might contain confidential information like login credentials)                             | High   (H)                           |
| Integrity   Impact (I):                                         | High   (Intercepted data could be modified during sniffing)                                                     | High   (H)                           |
| Availability   Impact (A):                                      | Low   (Doesn't affect overall system functionality)                                                             | Low   (L)                            |
| Base   Score (assuming High for Confidentiality and Integrity): | 0.85   * (AV:N/AC:L/PR:N/UI:N) * (S:C/C:H/I:H/A:L)                                                              | 8.5   (High)                         |
| Temporal   Score (TS):                                          | Not   Applicable (N/A)                                                                                          | N/A                                  |
| Environmental   Score (ES):                                     | Depends   on security measures across Mobile App, Cloud, and IoT (encryption protocols,   network segmentation) | Varies                               |
| Overall   CVSS Score                                            | Base   Score + TS + ES                                                                                          |         Varies (Depends on ES)       |
| Risk   Rating                                                   | High   to Critical (Depends on ES)                                                                              | High   to Critical                   |

**Overall, sniffing vulnerabilities pose a high to critical risk in a mobile-cloud-IoT ecosystem. Encrypting communication channels across all components and implementing network security best practices are essential to reduce the risk of data breaches and unauthorized data access.**

## Sniffing Attack Tree Diagram