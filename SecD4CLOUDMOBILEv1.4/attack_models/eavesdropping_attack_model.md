# Eavesdropping Attack Model

## Definition

Eavesdropping attack is a type of network attack in which the attacker listens to the conversations taking place among two or more authorized users or devices on the same network. This attack allows attackers to collect valuable information, including private data and confidential messages, without being detected. 

Once the attacker gains access to the network, they eavesdrop on the conversations taking place on the network. By monitoring the data packets being sent over the network, the attacker can gain access to sensitive information and data that they can then use for malicious purposes.

---

## Attack Categories

| **Category**               | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Passive Network Sniffing** | Monitors unencrypted traffic over Wi-Fi, cellular, or Bluetooth connections.     |
| **Man-in-the-Middle (MitM)** | Intercepts and possibly alters communications between endpoints.                 |
| **IoT Telemetry Interception** | Captures sensor data or device commands sent to cloud platforms.               |
| **Mobile App API Listening** | Monitors insecure API calls made by mobile apps to backend services.            |
| **Cloud Sync Eavesdropping** | Intercepts data during synchronization between devices and cloud storage.        |

---

## Mitigation

1. **Use Secure Communication Protocols:** Always use secure communication protocols such as HTTPS (Hypertext Transfer Protocol Secure) for data in transit. This ensures that the data is encrypted and cannot be easily intercepted by eavesdroppers.
2. **Data Encryption:** Encrypt sensitive data at rest and in transit. Use strong encryption algorithms and manage encryption keys securely (e.g. TLS/SSL, SSH);
3. **Secure Wi-Fi Networks:** Encourage users to only use secure and trusted Wi-Fi networks. Public Wi-Fi networks can be a hotbed for eavesdropping attacks;
4. **VPN:** Use a Virtual Private Network (VPN) for a more secure connection. A VPN can provide a secure tunnel for all data being sent and received;
5. **Regularly Update and Patch:** Ensure that the cloud and mobile applications are regularly updated and patched. This helps to fix any known vulnerabilities that could be exploited by attackers;
5. **Access Controls:** Implement strict access controls. Only authorized users should have access to sensitive data. Verify certificates, keys, and digital signatures;
6. **Security Headers:** Implement security headers like HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), etc. These headers add an extra layer of protection against eavesdropping attacks;
7. **Security Testing:** Regularly conduct security testing such as penetration testing and vulnerability assessments to identify and fix any security loopholes;
8. **User Awareness:** Educate users about the risks of eavesdropping attacks and how they can protect themselves. This includes not opening suspicious emails or clicking on unknown links, and only downloading apps from trusted sources;
9. **Incident Response Plan:** Have an incident response plan in place. This will ensure that you are prepared to respond effectively in case an eavesdropping attack does occur;
10. **Network Security**: Segment networks, use switch port security, and monitor ARP/DNS anomalies.

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can expose credentials, personal data, and device control commands.             | **8**            |
| **Reproducibility**  | Easily repeatable in open or poorly secured networks.                           | **8**            |
| **Exploitability**   | Low to moderate skill required; tools like Wireshark and mitmproxy are widely available. | **7**            |
| **Affected Users**   | Any user or device transmitting data over insecure channels.                    | **8**            |
| **Discoverability**  | Often undetected unless traffic is actively monitored or anomalies are flagged. | **7**            |

**Total DREAD Score: 38 / 5; Rating: High Risk**

---

## References

1. [OWASP Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html).
2. NIST SP 800-52: Guidelines for TLS Implementations.
3. ENISA Threat Landscape Report 2023 – [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications).
4. IEEE Internet of Things Journal: Securing IoT Communications Against Eavesdropping (2022).
5. [Mitre ATT&CK Framework – Network Sniffing](https://attack.mitre.org/techniques/T1040/).
5. SANS Institute: Network Security and Eavesdropping Defense Whitepapers.

---

## Eavesdropping Attack Tree Diagram