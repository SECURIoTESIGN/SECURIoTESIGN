# Sniffing Attacks Model

A **Sniffing Attack** (or eavesdropping attack) in the Cloud-Mobile-IoT ecosystem involves an attacker intercepting, reading, and interpreting network traffic data as it travels between interconnected devices and the cloud infrastructure. The goal is to capture sensitive information, particularly when it is transmitted without encryption.

***

## Definition

A **Sniffing Attack** utilizes network monitoring tools, often referred to as "sniffers" or "packet analyzers," to passively capture data packets traversing a network segment. The attacker places a network interface into **promiscuous mode**, allowing it to capture all traffic, regardless of its intended recipient.

In the context of the Cloud-Mobile-IoT ecosystem, a successful sniffing attack exposes:

* **Authentication Credentials:** Usernames, passwords, session tokens, or API keys used by mobile applications or IoT devices to access the cloud.
* **Sensitive Data:** Raw IoT sensor readings (e.g., location, health metrics, industrial telemetry) and private user data from mobile applications.
* **Operational Commands:** Unencrypted commands sent from the cloud or mobile app to control an IoT device (e.g., "unlock door," "raise temperature").

***

## Attack Categories

Sniffing attacks are categorized based on the method used to gain access to the network traffic.

### 1. Passive Sniffing (Wireless Networks)
* **Mechanism:** The simplest form, primarily targeting wireless media (Wi-Fi, Bluetooth, Zigbee). The attacker merely listens to traffic being broadcast over the air.
* **Vulnerability:** Exploits the nature of wireless signals, where any device within range can intercept the transmission. If the network uses **WEP** or an open **Wi-Fi** standard, all data is immediately readable. Even with weak **WPA/WPA2-PSK** encryption, a sniffer can capture the initial handshake and, given sufficient time, attempt to crack the password offline to decrypt all subsequent traffic.

### 2. Active Sniffing (Wired Networks)
* **Mechanism:** Used on wired networks (e.g., corporate LAN, home router) where traffic is generally switched (sent only to the intended recipient port). The attacker must actively introduce techniques to divert traffic to their interface.
* **ARP Poisoning:** The attacker sends falsified **ARP (Address Resolution Protocol)** messages to devices on the network, associating their own MAC address with the IP address of the router or cloud gateway. This forces all traffic intended for the cloud to pass through the attacker machine first.
* **MAC Flooding:** The attacker overloads a network switch MAC address table, forcing the switch to fail and revert to a **hub-like behavior**, broadcasting all traffic to all ports, allowing the sniffer to capture it.

### 3. DNS/Protocol Spoofing
* **Mechanism:** The attacker sets up a machine (often via a **Rogue AP** or **ARP Poisoning**) to intercept **DNS requests** and reply with a forged IP address, directing the client traffic to an attacker-controlled server instead of the legitimate cloud service. This allows the sniffer to act as a proxy and fully intercept and often modify the data.

***

## Mitigation Strategies

Mitigation for sniffing attacks focuses heavily on mandatory encryption and network segmentation.

### 1. Mandatory Encryption (Network/Cloud Layer)
* **End-to-End TLS/SSL:** The single most effective countermeasure. All communication from **IoT devices** and **mobile applications** to the cloud server must be secured using robust **TLS 1.2 or 1.3**. Even if the traffic is sniffed, it remains incomprehensible due to strong encryption.
* **Secure IoT Protocols:** Use security-enhanced protocols like **MQTT over TLS/SSL (MQTTS)** and **CoAP over DTLS (CoAPS)** for low-power IoT communication.
* **Strong Wi-Fi Security:** Enforce modern Wi-Fi encryption standards like **WPA3**, which makes sniffing the initial handshake and cracking the password significantly harder.

### 2. Network and Architectural Controls
* **Network Segmentation:** Use VLANs or firewalls to logically separate IoT devices, mobile users, and core servers. If a segment is compromised by sniffing, the attack cannot easily spread to other critical parts of the infrastructure.
* **ARP Monitoring:** Implement tools and switches that monitor for suspicious **ARP traffic** and detect **ARP poisoning** attempts.
* **Use of Switches over Hubs:** Ensure the underlying network infrastructure uses modern network switches, which isolate traffic to specific ports, preventing passive sniffing on wired segments.

***

## DREAD Risk Assessment for Sniffing Attack

The DREAD framework is used to quantify the risk of a Sniffing Attack, assuming the system is vulnerable (e.g., using unencrypted HTTP or weak WEP/WPA).

| DREAD Factor | Assessment | Score (0-10) | Rationale for Sniffing Attack |
| :--- | :--- | :--- | :--- |
| **D**amage Potential | **High** | 8 | Leads to loss of data **confidentiality** (exposure of credentials/sensitive data) and often compromise of data **integrity** if the sniffer also acts as a proxy for injection. |
| **R**eproducibility | **Very Easy** | 9 | Passive sniffing on an unencrypted wireless network is trivial. Active sniffing (ARP poisoning) is also easily automated with open-source tools. |
| **E**xploitability | **Easy** | 8 | Requires minimal technical knowledge and low-cost COTS hardware (a laptop and a compatible wireless adapter). The tools are freely available and user-friendly. |
| **A**ffected Users | **Many** | 8 | A single sniffer can capture data from every vulnerable IoT device or mobile user operating on the compromised network segment. |
| **D**iscoverability | **High** | 7 | Wireless traffic is easily detectable via standard network scanning. Active attacks like ARP poisoning can be detected by monitoring tools, but the basic vulnerability (lack of encryption) is easily found. |
| **Total Risk Score** | **High** | 40/5 (**Average: 8.0**) | This represents a severe, easy-to-execute threat that fundamentally undermines data confidentiality. |

***

## References

1. LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). Microsoft Press. (For the foundational DREAD model)
2. Moustafa, S., & Shuman, M. (2021). **Wireless Sniffing Attacks and Defense Mechanisms for IoT Ecosystems**. *International Journal of Computer Networks and Applications*, *8*(3), 45-56.
3. NIST. (2014). **Special Publication 800-52 Revision 2: Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations**. National Institute of Standards and Technology.
4. Rhee, Y. J., & Lee, B. H. (2018). **A Study on the Vulnerability of ARP Protocol and Countermeasures**. *International Journal of Advanced Smart Convergence*, *7*(1), 1-10.
5. Singh, S., & Agrawal, A. (2019). **A Comprehensive Study on Various Network Sniffing Techniques and Their Mitigation**. *International Journal of Computer Applications*, *177*(46), 1-6.

***

## Sniffing Attack Tree Diagram