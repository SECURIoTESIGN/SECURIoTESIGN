# Rogue Access Point Attacks

This attack aims to access and steal sensitive data from legitimate users of a wireless network by redirecting them to a fake network (from a fake access point) using a stronger signal than that of the real network, which facilitates the authentication of the target mobile devices to the fraudulent network, given the fact that this authentication is automatic.

## Definition

 The Access Points (AP) in a Wi-Fi networks are subject to the attack of access point spoofing, usually called Rogue Access Point (RAP). This attack consists of cloning the Media Access Control (MAC) address and Service Set IDentifier (SSID) of an AP, giving rise to the emergence of a fake access point posing as a genuine one, leading users to connect to this new network as if they were connecting to the genuine network. After connection, an attack is able to eavesdrops on its communication to hijack client's communication, re-direct clients to malicious websites, steal credentials (session hijacking) of the clients connecting to it.

 ## Mitigation

1. **Wireless Intrusion Prevention Systems (WIPS)**: Implement WIPS to detect and neutralize rogue access points. These systems can continuously monitor the radio spectrum for unauthorized devices and can take pre-configured actions when they are detected.

2. **Regular Audits**: Conduct regular network audits to identify and remove any unauthorized devices. This includes physical inspections as well as the use of network scanning tools.

3. **Network Access Control (NAC)**: Implement NAC solutions to control the devices that can connect to your network. This can prevent unauthorized devices from gaining access to your network.

4. **MAC Address Filtering**: Use MAC address filtering to control which devices can connect to your network. This can prevent unauthorized devices from connecting to your network.

5. **Strong Encryption and Authentication**: Use strong encryption (like WPA3) and authentication methods for your wireless networks. This can prevent unauthorized access to your network.

6. **User Education**: Educate users about the risks of connecting to unauthorized wireless networks. Encourage them to only connect to trusted networks.

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission.

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.
 
## Rogue Access Point Vulnerability Risk Analysis 

Rogue access points (RAPs) mimic legitimate Wi-Fi networks, tricking users into connecting and potentially exposing their data. Here's a breakdown of the risk for a mobile cloud-based application.

| **Factor**                                                      | **Description**                                                                                                                                       | **Value**                              |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Attack   Vector (AV):                                           | Network   (Exploiting user trust and network connectivity)                                                                                            | Network   (N)                          |
| Attack   Complexity (AC):                                       | Low   (Setting up a rogue access point can be relatively simple)                                                                                      | Low   (L)                              |
| Privileges   Required (PR):                                     | None   (User initiates the connection)                                                                                                                | None   (N)                             |
| User   Interaction (UI):                                        | Required   (User chooses and connects to the Wi-Fi network)                                                                                           | Required   (R)                         |
| Scope   (S):                                                    | Varies   (Depends on attacker's capabilities on the RAP)                                                                                              |         Man-in-the-Middle (MitM)       |
| Confidentiality   Impact (C):                                   | High   (Attacker might intercept sensitive data like login credentials)                                                                               | High   (H)                             |
| Integrity   Impact (I):                                         | High   (Attacker might modify data in transit)                                                                                                        | High   (H)                             |
| Availability   Impact (A):                                      | Low   (Doesn't affect application functionality)                                                                                                      | Low   (L)                              |
| Base   Score (assuming High for Confidentiality and Integrity): | 0.85   * (AV:N/AC:L/PR:N/UI:R) * (S:MitM/C:H/I:H/A:L)                                                                                                 | 8.5   (High)                           |
| Temporal   Score (TS):                                          | Not   Applicable (N/A)                                                                                                                                | N/A                                    |
| Environmental   Score (ES):                                     | Depends   on user awareness training, application security measures (e.g., secure   communication protocols), Mobile Device Management (MDM) policies | Varies                                 |
| Overall   CVSS Score                                            | Base   Score + TS + ES                                                                                                                                |         Varies (Depends on ES)         |
| Risk   Rating                                                   | High   to Critical (Depends on ES)                                                                                                                    | High   to Critical                     |

**Overall, rogue access points pose a high to critical risk for mobile cloud-based applications that hold user's confidential data. A layered approach with user education, application security measures, and MDM policies can significantly reduce the risk.**

## References
1. [CAPEC-175: Code Inclusion](https://capec.mitre.org/data/definitions/175.html).

## Rogue Access Point Attack Tree Diagram


