# Tampering Attacks Model

A **Tampering Attack** is a security threat that involves the **unauthorized modification** of data, code, configuration, or physical devices within an information system. In the **Cloud-Mobile-IoT ecosystem**, tampering compromises the **integrity** of data, software, and hardware, leading to corrupted decisions, system malfunction, or unauthorized control.

***

## Definition

A **Tampering Attack** is any malicious act intended to alter an entity or its processes without authorization. Unlike sniffing (which targets confidentiality) or spoofing (which targets authenticity), tampering directly targets **data integrity**.

In the context of this ecosystem, tampering can occur at multiple layers:

* **Data Tampering:** Modifying sensor readings in transit or at rest on a server.
* **Code/Software Tampering:** Injecting malicious code into a mobile application, IoT device firmware, or cloud function.
* **Hardware/Physical Tampering:** Physically modifying an IoT device to alter its function or extract secrets.

A successful tampering attack leads the system to operate on false premises, resulting in incorrect actions (e.g., an industrial sensor reports a safe temperature when the value was tampered with to hide an actual overheat).

***

## Attack Categories

Tampering attacks are categorized based on the entity being modified.

### 1. Data Tampering (Communication & Cloud Layer)

* **Man-in-the-Middle (MITM) Modification:** An attacker intercepts the data stream between an IoT device and the cloud (e.g., via a compromised gateway or network proxy) and alters the content of the data packets before forwarding them. This is often the primary goal of session hijacking or MITM attacks.
* **Database/Storage Tampering:** An attacker compromises the cloud database or storage system and directly modifies data at rest. This could be changing financial records, user profiles, or historical IoT sensor logs.
* **Log Tampering:** An attacker modifies system logs on a mobile device, an IoT gateway, or a cloud server to erase evidence of a previous malicious activity or to frame another user/system component.

### 2. Code/Software Tampering (Mobile & IoT Layer)

* **Mobile Application Tampering:** An attacker reverse-engineers a mobile application, inserts malicious code (e.g., to steal credentials or change API endpoints), and re-packages it for distribution. Users installing the tampered app compromise their session security.
* **Firmware Tampering:** An attacker modifies the software that runs on an **IoT device** (the firmware). This can involve injecting a backdoor, disabling security checks, or reprogramming the device to send false data or obey unauthorized commands from a separate channel.
* **Configuration Tampering:** An attacker alters critical system configuration files (e.g., firewall rules, access control lists, environment variables) on a cloud server or IoT gateway, reducing the system security posture.

### 3. Physical Tampering (IoT Layer)

* **Hardware Modification:** An attacker physically accesses a device (e.g., a smart meter, a critical sensor) and attaches probes to alter sensor output, bypass authentication checks, or use techniques like **fault injection** (glitching) to force the chip to reveal cryptographic keys.
* **Sensor Bypass:** An attacker physically isolates a sensor from the system and substitutes it with a different component that reports falsified, safe data, while the critical condition is allowed to persist (e.g., replacing a door-closed sensor with a simple resistor).

***

## Mitigation Strategies

Mitigation focuses on cryptographic validation of data and code, along with physical security measures for devices.

### 1. Data Integrity Controls

* **Digital Signatures and HMACs:** All critical data packets (especially IoT sensor readings and command signals) sent between the device and the cloud must be secured with **digital signatures** or **Hash-based Message Authentication Codes (HMACs)**. The recipient must verify this signature/hash to confirm that the data has not been altered in transit. 
* **End-to-End Encryption (E2EE) with Integrity:** Use robust protocols like **TLS 1.3**, which provides strong encryption *and* message integrity checking, making silent modification of data in transit nearly impossible.
* **Immutable Logs:** Implement logging systems that prevent modification of logs *after* they are written (e.g., using blockchain or append-only storage mechanisms) to counter log tampering.

### 2. Code and Software Integrity

* **Code Signing:** All mobile applications and IoT firmware updates must be cryptographically signed by the legitimate developer. Devices/users should **verify the signature** before installing or running the code to detect any unauthorized modification.
* **Runtime Integrity Checking:** Mobile applications and critical IoT devices should incorporate mechanisms to continuously check their own code integrity during execution and shut down or alert if tampering is detected (**Self-Healing/Guarding**).
* **Secure Boot:** Implement a **Hardware Root of Trust** and a **Secure Boot** process on IoT devices to ensure that only cryptographically signed and trusted firmware can be loaded upon startup.

### 3. Physical and Hardware Security

* **Tamper-Evident/Tamper-Resistant Casing:** Design IoT devices with physical casings that show clear evidence if they have been opened (tamper-evident) or use materials and seals that actively destroy secret keys if intrusion is attempted (tamper-resistant). 
* **Auditing and Monitoring:** For critical infrastructure, perform regular physical audits and use environmental monitoring (e.g., security cameras, internal temperature sensors) to detect unauthorized physical access to devices.

***

## DREAD Risk Assessment

The DREAD framework is used to quantify the risk of a typical Tampering Attack on a critical IoT sensor data stream.

| DREAD Factor | Assessment | Score (0-10) | Rationale for Tampering Attack |
| :--- | :--- | :--- | :--- |
| **D**amage Potential | **Catastrophic** | 10 | Directly compromises data integrity, leading to erroneous control decisions, financial loss, system failure, or physical danger (e.g., manipulating safety readings). |
| **R**eproducibility | **Medium-High** | 7 | Depends on the defense: Easy if data is unencrypted/unsigned (9); Hard if strong cryptography is used (4). Many IoT deployments lack strong E2E integrity checks. |
| **E**xploitability | **Medium** | 6 | Requires moderate skill to set up a MITM or to reverse-engineer and resign an application/firmware, but necessary tools are widely available. |
| **A**ffected Users | **Widespread** | 8 | Tampering with core data or code can lead to incorrect behavior for all users and systems relying on that corrupted source. |
| **D**iscoverability | **Medium-Low** | 5 | Data or code that is tampered with can be difficult to detect if the integrity check is not performed correctly. Log tampering makes detection harder. |
| **Total Risk Score** | **High** | 36/5 (**Average: 7.2**) | A fundamental and dangerous threat that undermines the reliability and trustworthiness of the entire system. |

***

## References

1. LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). Microsoft Press. (For the foundational DREAD model)
2. Mylonas, A., & Papanikolaou, E. (2018). **Security in the Internet of Things: A Review of Attacks and Countermeasures**. *Sensors*, *18*(9), 3121.
3. NIST. (2014). **Special Publication 800-52 Revision 2: Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations**. National Institute of Standards and Technology.
4. Rhee, J., & Lee, B. H. (2020). **A Survey on Integrity Attacks and Countermeasures in Industrial IoT**. *Sensors*, *20*(2), 481.
5. Shimon, C., & Green, A. (2021). **Securing Firmware Updates with Digital Signatures in Resource-Constrained IoT Devices**. *IEEE Internet of Things Journal*, *8*(12), 9781–9790.

***

## Tampering Attack Tree Diagram


