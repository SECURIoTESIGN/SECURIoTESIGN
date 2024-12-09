# Wi-Fi SSID Tracking Attack 

Wi-Fi SSID tracking attack is an attack in which malicious actors use techniques such as tracking the Media Access Control (MAC) addresses or the Service Set Identifier (SSID) of a device to capture user data transmitted through a wireless network. This type of attack has become increasingly popular due to its simplicity and the fact that it can be used to target multiple devices in a network. The attack can be used to steal sensitive data such as credit card information and other personal details that are sent through the network. It can also be used to launch Distributed Denial of Service (DDoS) attacks.  

Overall, Wi-Fi SSID tracking attack is a threat that should be taken seriously as it can have serious implications on user security.

## Mitigation

1. **Disable SSID Broadcasting**: Disabling SSID broadcasting can make your network invisible to devices that are not already connected. This can prevent an attacker from discovering your network through SSID tracking;

2. **Randomize MAC Addresses**: Many modern devices support MAC address randomization, which can prevent your device from being tracked using its MAC address;

3. **Use of VPNs**: Virtual Private Networks (VPNs) can encrypt your internet connection and hide your online activities from eavesdroppers;

4. **Network Security**: Use strong encryption (like WPA3) for your Wi-Fi network to prevent unauthorized access;

5. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers;

6. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules;

7. **Secure Cloud Configurations**: Ensure that your cloud configurations are secure and that all data is encrypted during transmission;

8. **IoT Security Measures**: Implement IoT-specific security measures such as device authentication, secure booting, and hardware-based security solutions.

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.

## Wi-Fi SSID Tracking Risk Analysis

| **Factor**                    | **Description**                                                                | **Value**                                                                      |
|-------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Attack   Vector (AV):         | Network   (Tracking SSIDs and exploiting network weaknesses)                   | Network   (N)                                                                  |
| Attack   Complexity (AC):     | Varies   (Depends on the complexity of subsequent attacks after tracking)      |         Low (L) to High (H)                                                    |
| Privileges   Required (PR):   | Varies   (Depends on the subsequent attack)                                    |         None (N) to High (H)                                                   |
| User   Interaction (UI):      | None   (SSID tracking might not require interaction, subsequent attacks might) | Varies   (N to H)                                                              |
| Scope   (S):                  | Varies   (Depends on the subsequent attack)                                    |         Can range from Information Disclosure (ID) to Data   Breach (DB)       |
| Confidentiality   Impact (C): | Varies   (Depends on the subsequent attack)                                    |         Low (L) to High (H)                                                    |
| Integrity   Impact (I):       | Varies   (Depends on the subsequent attack)                                    |         Low (L) to High (H)                                                    |
| Availability   Impact (A):    | Varies   (Depends on the subsequent attack)                                    |         Low (L) to High (H)                                                    |
| Base Score | 3.3 (Low) | Low (Low) | 
|Overall Rating| Base Score + TS + ES | Varies (Depends on TS, ES, and the specific subsequent attack)| 
|Risk Rating | Low to Critical (Depends on ES and the subsequent attack) |  Low (H) to Critical (C) |

**Overall, Wi-Fi SSID tracking combined with potential subsequent attacks can pose a low to critical risk depending on the specific attack scenario and the security measures in place. A layered security approach across the mobile app, cloud infrastructure, and user behavior is essential to mitigate these risks.**

## Wi-Fi SSID Tracking Attack Tree Diagram