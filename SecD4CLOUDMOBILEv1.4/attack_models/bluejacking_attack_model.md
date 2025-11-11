# Bluejacking Attack Model

## Definition

Bluejacking is a type of attack where an attacker sends anonymous messages over Bluetooth to Bluetooth-enabled devices. Bluejacking attacks often involve malicious content, such as malicious links, malicious images, or malicious text. These messages can be sent from any device that can send Bluetooth signals, such as laptops, mobile phones, and even some home appliances.

## Attack Categories

| **Category**             | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **Unsolicited Messaging**| Sends anonymous messages to nearby devices via Bluetooth Object Exchange (OBEX).|
| **Social Engineering**   | Uses messages to trick users into clicking malicious links or installing apps.  |
| **Cloud Relay Exploits** | Messages may trigger cloud-based app actions (e.g., opening URLs, syncing data).|
| **IoT Disruption**       | Sends commands or spam to smart devices with Bluetooth interfaces (e.g., speakers, wearables). |
| **Mobile App Injection** | Malicious apps use Bluetooth APIs to send bluejacking payloads to nearby devices. |

---

## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **Device Level**     | Disable Bluetooth when not in use, set device to non-discoverable mode, restrict OBEX access. |
| **App Level**        | Limit Bluetooth permissions, validate incoming messages, block unsolicited triggers. |
| **Cloud Level**      | Authenticate Bluetooth-originated actions before syncing or executing cloud functions. |
| **IoT Firmware**     | Restrict Bluetooth profiles, enforce secure pairing, auto-expire open connections. |
| **User Behavior**    | Educate users to ignore unknown messages and avoid pairing in public spaces.     |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Typically low, but can escalate via phishing or app manipulation.               | **5**            |
| **Reproducibility**  | Easily repeatable with basic tools and open Bluetooth targets.                  | **8**            |
| **Exploitability**   | Requires minimal skill; tools like BTScanner and mobile apps can automate it.   | **7**            |
| **Affected Users**   | Any user with Bluetooth enabled and discoverable in public areas.               | **6**            |
| **Discoverability**  | Highly visible; messages appear on user screens, making detection immediate.    | **9**            |

**Total DREAD Score: 35 / 5 = 7**; Rating: **Moderate Risk**

---