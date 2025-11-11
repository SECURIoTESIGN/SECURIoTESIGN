# Bluejacking Attacks Model

D# Bluejacking & Bluesnarfing Attacks in Cloud-Based Mobile App and IoT Ecosystems

Bluetooth-based attacks like **Bluejacking** and **Bluesnarfing** pose unique risks in mobile and IoT environments, especially when devices are cloud-connected. These attacks exploit vulnerabilities in short-range wireless communication to disrupt services, steal data, or compromise user trust.

---

## Attack Categories

| **Attack Type**     | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Bluejacking**     | Sends unsolicited messages to nearby Bluetooth-enabled devices. Often harmless but can be used for phishing or social engineering. |
| **Bluesnarfing**    | Unauthorized access to data on a Bluetooth-enabled device (e.g., contacts, messages, files). More severe and stealthy. |
| **Cloud Relay Exploits** | Hijacked Bluetooth sessions can be relayed to cloud apps, enabling remote data exfiltration or session hijacking. |
| **IoT Device Hijacking** | Exploits weak Bluetooth pairing on smart devices (e.g., wearables, sensors) to inject commands or extract telemetry. |
| **Mobile App Injection** | Malicious apps use Bluetooth APIs to scan, connect, or manipulate nearby devices without user consent. |

---

## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **Device Level**     | Disable Bluetooth when not in use, enforce secure pairing, use device-level encryption. |
| **App Level**        | Restrict Bluetooth permissions, validate device identity, monitor API usage.   |
| **Cloud Level**      | Authenticate Bluetooth-originated data before syncing, apply anomaly detection on device telemetry. |
| **IoT Firmware**     | Enforce firmware signing, disable insecure Bluetooth profiles, auto-expire pairing sessions. |
| **User Behavior**    | Educate users to reject unknown pairing requests and avoid public Bluetooth zones. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Bluesnarfing can expose sensitive data; Bluejacking may lead to phishing or social engineering. | **7**            |
| **Reproducibility**  | Easily repeatable in open environments with basic tools.                        | **8**            |
| **Exploitability**   | Moderate skill required; tools like BTScanner and BlueSnarfer are widely available. | **7**            |
| **Affected Users**   | Any user with Bluetooth enabled in public or insecure zones.                    | **6**            |
| **Discoverability**  | Bluejacking is visible; Bluesnarfing is stealthy and harder to detect.          | **7**            |

**Total DREAD Score: 35 / 5 = 7**; Rating: **Moderate to High Risk**

---

## References
1. Patel, N., Wimmer, H., Rebman, C.M., 2021. Investigating bluetooth vulnerabilities to defend from attacks, in: 2021 5th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT), IEEE, Ankara, Turkey. pp. 549–554. doi:10.1109/ISMSIT52890.2021.9604655.
2. Attack and System Modeling Applied to IoT, Cloud, and Mobile Ecosystems .... https://dl.acm.org/doi/fullHtml/10.1145/3376123.
3. Secure cloud-based mobile apps: attack taxonomy, requirements .... https://link.springer.com/article/10.1007/s10207-023-00669-z.
4. Securing Cloud-Based Internet of Things: Challenges and Mitigations. https://arxiv.org/pdf/2402.00356.

---






