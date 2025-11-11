# Bluesnarfing Attack Model

Bluesnarfing attack is a type of wireless attack that allows attackers to gain unauthorized access to data stored on a Bluetooth-enabled device. Unlike Bluejacking, which is mostly disruptive, Bluesnarfing is stealthy and can lead to serious data breaches—especially in cloud-connected mobile apps and IoT devices.

---

## Attack Categories

| **Category**               | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Unauthorized Data Access** | Attacker connects to a device and extracts contacts, messages, files, or credentials. |
| **Cloud Sync Exploits**     | Stolen data may be synced to cloud apps, escalating the breach beyond the local device. |
| **IoT Device Exploitation** | Targets Bluetooth-enabled smart devices (e.g., wearables, sensors) to extract telemetry or control functions. |
| **Session Hijacking**       | Captures session tokens or authentication credentials for cloud services.     |
| **Silent Surveillance**     | Attacker remains undetected while continuously extracting or monitoring data. |

---

## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **Device Level**     | Disable Bluetooth when not in use, enforce secure pairing, use strong PINs or passkeys. |
| **App Level**        | Restrict Bluetooth API access, validate device identity, encrypt sensitive data before sync. |
| **Cloud Level**      | Authenticate all Bluetooth-originated data, monitor for anomalous sync patterns, enforce session expiration. |
| **IoT Firmware**     | Disable insecure Bluetooth profiles, enforce firmware signing, auto-expire pairing sessions. |
| **User Behavior**    | Educate users to avoid pairing in public spaces and reject unknown connection requests. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1–10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can lead to full data compromise, identity theft, and cloud account infiltration. | **9**            |
| **Reproducibility**  | Easily repeatable with tools like BlueSnarfer or BTScanner in open environments. | **8**            |
| **Exploitability**   | Moderate skill required; tools are widely available and documented.             | **7**            |
| **Affected Users**   | Any user with discoverable Bluetooth devices, especially in public or enterprise settings. | **8**            |
| **Discoverability**  | Difficult to detect; attack is silent and leaves minimal traces.                | **7**            |

**Total DREAD Score: 39 / 5 = 7.8**; Rating: **High Risk**

---

## Reference

1. [Bluesnarfing: What is it and how to prevent it | NordVPN](https://nordvpn.com/blog/bluesnarfing/).
2. [Attack and System Modeling Applied to IoT, Cloud, and Mobile Ecosystems](https://dl.acm.org/doi/fullHtml/10.1145/3376123).
3. [Securing Cloud-Based Internet of Things: Challenges and Mitigations](https://arxiv.org/pdf/2402.00356).
4. Patel, N., Wimmer, H., Rebman, C.M., 2021. Investigating bluetooth vulnerabilities to defend from attacks, in: 2021 5th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT), IEEE, Ankara, Turkey. pp. 549–554. doi:10.1109/ISMSIT52890.2021.9604655.

## Bluetooth Attack Tree Diagram