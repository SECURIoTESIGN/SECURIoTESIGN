# Wi-Fi Jamming Attacks Model

A **Wi-Fi Jamming Attack** is a type of **Denial of Service (DoS)** attack that aims to completely disrupt or significantly degrade the wireless communication capabilities of a target network. In the **Cloud-Mobile-IoT ecosystem**, a jamming attack severs the crucial connection between endpoint devices (IoT sensors, mobile users) and the cloud services, preventing data transmission, remote control, and system monitoring.

***

## Definition

A **Wi-Fi Jamming Attack** occurs when an attacker uses a device (a **jammer**) to broadcast a powerful radio frequency (RF) signal on the same frequency channels used by the target Wi-Fi network. This intentional, high-power interference effectively drowns out the legitimate, low-power Wi-Fi signals, causing severe **signal-to-noise ratio (SNR)** degradation. Devices attempting to communicate perceive the jammer noise as an insurmountable barrier, leading to communication failure and effectively stopping the flow of data.

This attack primarily targets the **availability** of the wireless network and, by extension, the availability of the cloud services relying on that connectivity. It does not steal or modify data but prevents it from reaching its destination.

***

## Attack Categories

Jamming attacks are categorized by the nature of the interference signal and the complexity of the jammer device.

### 1. Constant Jamming (Brute-Force DoS)
* **Mechanism:** The jammer continuously transmits a high-power, unmodulated (pure noise) signal on the target channel frequency band. This is the simplest and most effective form of jamming, ensuring that all legitimate Wi-Fi transmissions are completely masked.
* **Vulnerability:** Exploits the principle of electromagnetic interference. A jammer only needs to be close to the target access point or device with sufficient power to overwhelm the legitimate signal.
* **Target:** Small, local IoT deployments or mobile users confined to a specific geographic area.

### 2. Deauthentication/Disassociation Flooding (Protocol DoS)
* **Mechanism:** While technically not "jamming" the radio waves with noise, this is a highly effective **protocol-level DoS attack** that achieves the same result. The attacker constantly broadcasts spoofed **Deauthentication (Deauth)** or **Disassociation** frames to target clients, making them forcibly disconnect from the legitimate Wi-Fi access point (AP). Clients waste time attempting to reconnect, achieving a persistent DoS.
* **Vulnerability:** Exploits the lack of mandatory, cryptographic authentication for Deauth/Disassociation management frames in older Wi-Fi standards (WPA2).

### 3. Reactive Jamming (Smart DoS)
* **Mechanism:** A more stealthy and power-efficient technique. The jammer actively listens to the channel and only transmits interference when it detects a **legitimate signal transmission** is about to occur or is in progress.
* **Advantage:** Difficult to detect because the jamming signal is not constant, and it conserves the attacker power/battery life.
* **Target:** Critical, low-data-rate IoT links, where every transmission is vital.

***

## Mitigation Strategies

Mitigation focuses on physical security, frequency agility, and protocol hardening.

### 1. Physical and Environmental Controls
* **Physical Security:** For critical IoT devices and gateways, physical access must be restricted. Jammers are most effective when placed in close proximity to the target.
* **Wired Failover:** For mission-critical IoT systems (e.g., industrial control, medical monitoring), deploy **redundant, wired communication channels** (Ethernet, cellular 4G/5G) that automatically take over if the Wi-Fi link fails.
* **RF Spectrum Monitoring:** Deploy **Wireless Intrusion Prevention Systems (WIPS)** that constantly monitor the RF spectrum for high-power, continuous, or intermittent noise patterns indicative of jamming.

### 2. Frequency and Protocol Agility
* **Frequency Hopping/Channel Switching:** Configure Wi-Fi access points and IoT devices to automatically and rapidly switch to a **clear channel** when high interference is detected. This forces a constant jammer to attack the entire spectrum, increasing their power requirements and detection probability.
* **Spread Spectrum Techniques:** Use technologies that spread the signal across a wide frequency band, making it more resistant to jamming concentrated on a narrow band.
* **WPA3 Authentication:** Upgrade Wi-Fi networks to **WPA3**, which requires management frames (like Deauth/Disassociation) to be protected, thus mitigating protocol-level jamming attacks.

***

## DREAD Risk Assessment for Wi-Fi Jamming Attack

The DREAD framework is used to quantify the risk of a simple, constant Wi-Fi Jamming Attack.

| DREAD Factor | Assessment | Score (0-10) | Rationale for Wi-Fi Jamming Attack |
| :--- | :--- | :--- | :--- |
| **D**amage Potential | **High** | 9 | Causes total loss of **availability** for the entire local network, leading to data loss, monitoring gaps, and failure of remote control commands. |
| **R**eproducibility | **Very Easy** | 9 | Jamming hardware (or software defined radios) is readily available, cheap, and simple to operate. Deauth flooding requires only basic scripting/tools. |
| **E**xploitability | **Easy** | 8 | Requires little to no technical skill. The attacker only needs physical proximity and the ability to turn on a device. |
| **A**ffected Users | **Localized/Widespread** | 8 | All devices (IoT, mobile, compute) relying on the jammed network segment are affected, leading to a localized but complete outage. |
| **D**iscoverability | **Medium-High** | 7 | Constant jamming is easy to detect using basic spectrum analyzers. Protocol jamming is easily visible in network traffic logs (high rate of failed connections). |
| **Total Risk Score** | **High** | 41/5 (**Average: 8.2**) | A potent, easily executed, and difficult-to-defend DoS threat that severs the cloud-to-device link. |

***

## References

1. LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). Microsoft Press. (For the foundational DREAD model)
2. Mylonas, A., & Papanikolaou, E. (2018). **Security in the Internet of Things: A Review of Attacks and Countermeasures**. *Sensors*, *18*(9), 3121.
3. Pal, A., & Sanyal, S. (2020). **A Survey on Jamming Attacks and Countermeasures in Wireless Sensor Networks**. *Wireless Personal Communications*, *112*(3), 2005–2030.
4. Tinnirello, I. (2017). **Experimental Analysis of the Effectiveness of Jamming Attacks in IEEE 802.11 Networks**. *Ad Hoc Networks*, *57*, 46–55.
5. Zhang, Y., & Liu, X. (2021). **Mitigating Deauthentication Attacks in WPA3 Networks with Management Frame Protection**. *IEEE Transactions on Vehicular Technology*, *70*(6), 5940–5949.

***

## Wi-Fi Jamming Attack Tree Diagram
