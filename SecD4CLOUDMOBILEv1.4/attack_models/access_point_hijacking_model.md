# Access Point Hijacking Attack Model

In a scenario of this type of attack, which targets the wireless network, the attacker aims to take control of the wireless network by hijacking the access point (administration hijacking). 

## Definition

 This type of attack is a variant of the session hijacking attack and targets the AP access credentials of legitimate administrators. These credentials can be extracted through a sniffing, brute force or MiTM attack. After this, the attacker is able to carry out other types of attacks, such as DoS and Rogue Access Point. In cloud-connected mobile environments, this attack can compromise data confidentiality, session integrity, and service availability.

 
---

## Attack Categories

| **Category**              | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **Rogue Access Point**   | Attacker sets up a fake Wi-Fi hotspot mimicking a trusted network.             |
| **Evil Twin Attack**     | A clone of a legitimate access point with stronger signal to lure users.       |
| **Man-in-the-Middle (MitM)** | Hijacked AP intercepts and possibly alters communication between user and cloud. |
| **Session Hijacking**    | Captures session tokens or credentials to impersonate users.                   |
| **DNS Spoofing/Redirection** | Redirects traffic to malicious servers or phishing sites.                      |

---

## Mitigation Strategies

| **Layer**         | **Mitigation**                                                                 |
|-------------------|--------------------------------------------------------------------------------|
| **Device Level**  | Use VPN, disable auto-connect to open networks, prefer mobile data when possible. |
| **Network Level** | Use WPA3 encryption, MAC filtering, and disable SSID broadcast for sensitive APs. |
| **Cloud Level**   | Enforce HTTPS/TLS, implement certificate pinning, monitor for anomalous traffic. |
| **User Behavior** | Educate users about fake hotspots, encourage use of trusted networks only.       |
| **Security Tools**| Deploy mobile threat defense (MTD), intrusion detection systems (IDS), and endpoint protection. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to full session compromise, credential theft, and data interception.   | **8**            |
| **Reproducibility**  | Easily repeatable with basic tools like Wi-Fi Pineapple or custom AP scripts.   | **9**            |
| **Exploitability**   | Requires moderate skill; tools are widely available and affordable.             | **8**            |
| **Affected Users**   | Any mobile user connecting to public or untrusted Wi-Fi networks.               | **7**            |
| **Discoverability**  | Highly discoverable in open environments; difficult to detect without monitoring. | **8**            |

**Total DREAD Score: 40 / 5 = 8**; Rating: **High Risk**

---

## References

1. [OWASP Mobile Security Project](https://owasp.org/www-project-mobile-security/)
2. NIST SP 800-153: Guidelines for Securing Wireless Local Area Networks (WLANs)
3. [ENISA Threat Landscape Report 2023](https://www.enisa.europa.eu/publications)
4. IEEE Access: Security Challenges in Mobile Cloud Computing (2022)
5. [Mitre ATT&CK Framework](https://attack.mitre.org)
6. [SANS Institute Whitepapers](https://www.sans.org/white-papers/)

---

## Access Point Hijacking Attacks Tree
