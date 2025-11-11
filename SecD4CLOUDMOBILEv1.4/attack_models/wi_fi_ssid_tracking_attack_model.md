# Wi-Fi SSID Tracking Attacks Model

A **Wi-Fi SSID Tracking Attack** exploits the process by which mobile and IoT devices actively search for familiar wireless networks. The attack targets **confidentiality** and **privacy** by leveraging these broadcast messages to locate, track, and profile individuals and their devices across different physical locations.

***

## Definition

A **Wi-Fi SSID Tracking Attack** involves an attacker passively or actively capturing **Probe Request frames** broadcast by client devices (smartphones, tablets, wearables, IoT sensors) searching for previously connected Wi-Fi networks. These probe requests often contain the **Service Set Identifier (SSID)**, the network name (e.g., "Home-WiFi" or "Starbucks Free Wi-Fi") in plaintext.

By correlating the device unique **MAC address** with the list of SSIDs it is probing for and the physical location where the probes are captured, an attacker can:

* **Track a Device Location:** Correlate the device MAC address across time and different physical locations.
* **Identify the User/Owner:** Infer the user home address, workplace, or frequented establishments based on the recognized SSIDs.
* **Profile Activities:** Determine when a user arrives at or leaves certain locations.

In the Cloud-Mobile-IoT ecosystem, this data can be combined with other publicly available information to create comprehensive behavioral profiles.

***

## Attack Categories

SSID tracking attacks are categorized by the method used to capture and analyze the broadcast probe requests.

### 1. Passive Scanning and Sniffing
* **Mechanism:** The attacker uses a Wi-Fi adapter in **monitor mode** and a packet sniffing tool (like Wireshark or Kismet) to continuously capture all probe request frames broadcast in the area. The attacker then logs the device MAC address and the list of requested SSIDs.
* **Vulnerability:** Exploits the default behavior of most client devices and older Wi-Fi standards, which require broadcasting the full list of preferred networks when they are not actively connected.
* **Target:** General mobile device users in public spaces (malls, airports, city streets).

### 2. Active Tracking and Geolocation
* **Mechanism:** The attacker sets up multiple, fixed Wi-Fi sniffing stations across a wide area (e.g., a city block or a large building). By measuring the signal strength (RSSI) and the time delay of probe requests received from a specific device at multiple sensor points, the attacker can **triangulate** or **trilaterate** the device precise real-time location.
* **Target:** Tracking the movements of specific individuals or high-value targets within a defined zone.

### 3. Rogue Access Point (AP) Deployment
* **Mechanism:** The attacker deploys a **Rogue AP** that listens for probe requests and actively attempts to connect to devices by impersonating a requested SSID. The successful connection reveals the device active presence and, potentially, its operating system/device type.
* **Vulnerability:** Exploits the client device tendency to automatically trust and connect to a known network once a signal is detected.

***

## Mitigation Strategies

Mitigation focuses on client-side privacy settings and the adoption of modern, privacy-preserving Wi-Fi protocols.

### 1. MAC Address Randomization (Hardware/OS Layer)
* **Client-Side Feature:** Modern mobile operating systems (iOS, Android, Windows) and newer hardware implement **MAC Address Randomization**. The device uses a randomized (or temporary) MAC address when probing for networks while disconnected, making it difficult for an attacker to correlate probes across time and location.
* **Enforcement:** Users should be educated to ensure this feature is enabled on their mobile and IoT devices.

### 2. Directed Probing and Privacy SSIDs (Protocol Layer)
* **Targeted Probes:** Configure devices to use **directed probing** instead of broadcasting. The device only sends a probe request for a specific SSID when it is reasonably sure that network is available (e.g., based on location data or previous connection history).
* **Hidden/Private SSIDs:** Use **"Hidden" SSIDs** on access points. While this is not a strong security measure, it prevents the AP from broadcasting the SSID, forcing clients to only send **directed probes** which can be a marginal privacy gain.

### 3. Network Segmentation and Control
* **Client Privacy Settings:** Implement network policies on public or shared Wi-Fi networks that block or ignore probe requests containing publicly known or private SSIDs, thus reducing the usefulness of the captured data.
* **VPN/TLS:** While not a direct defense against tracking, using **TLS/SSL** and **VPNs** ensures that even if an attacker attempts to infer activity based on IP address after connection, the actual data content remains private.

***

## DREAD Risk Assessment for Wi-Fi SSID Tracking Attack

The DREAD framework is used to quantify the risk of a Wi-Fi SSID Tracking Attack targeting user privacy.

| DREAD Factor | Assessment | Score (0-10) | Rationale for Wi-Fi SSID Tracking Attack |
| :--- | :--- | :--- | :--- |
| **D**amage Potential | **Medium-High** | 7 | Leads to severe loss of **privacy** and **confidentiality** of location and behavioral patterns, which can enable targeted attacks or profiling. |
| **R**eproducibility | **Very Easy** | 9 | The attack relies on an inherent broadcast feature of Wi-Fi. It requires only cheap, commodity hardware (Wi-Fi adapter) and free, open-source software. |
| **E**xploitability | **Easy** | 8 | Requires minimal technical skill. The tools are automated and widely used for network analysis and security testing. |
| **A**ffected Users | **Massive** | 10 | Every mobile phone, tablet, and many IoT devices within range of the sniffer are vulnerable when they are not actively connected to a network. |
| **D**iscoverability | **Low** | 3 | The attack is **passive**; the sniffer only listens and does not inject packets or cause network disruption, making it nearly invisible to standard network monitoring tools. |
| **Total Risk Score** | **High** | 37/5 (**Average: 7.4**) | A persistently high-risk privacy threat due to its simplicity, low cost, and massive scope. |

***

## References

1. LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). Microsoft Press. (For the foundational DREAD model)
2. Martinovic, M., & Papanikolaou, E. (2018). **Privacy Threats in Wi-Fi Networks: A Review of Probe Request Tracking and Countermeasures**. *Pervasive and Mobile Computing*, *44*, 25-42.
3. National Institute of Standards and Technology (NIST). (2017). **Special Publication 800-115: Technical Guide to Information Security Testing and Assessment**. (Relevant to wireless sniffing).
4. Pisharody, S., Naderi, Y., & Mohapatra, P. (2020). **A Survey on MAC Address Randomization and Probe Request Privacy in Wi-Fi**. *IEEE Communications Surveys & Tutorials*, *22*(4), 2139-2165.
5. Vanhoef, M., & Piessens, F. (2015). **On the Feasibility of Tracking Users in the Presence of MAC Address Randomization**. *Proceedings of the ACM Conference on Security and Privacy in Wireless and Mobile Networks (WiSec)*, 151-161.

***

## Wi-Fi SSID Tracking Attack Tree Diagram