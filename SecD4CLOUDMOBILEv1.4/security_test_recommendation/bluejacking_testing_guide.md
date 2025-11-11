# Security Testing for Bluejacking Attacks
The **Bluejacking attack** is a non-exploitative security vulnerability that uses the Bluetooth protocol to send unsolicited messages (text or images, often spam or advertisements) to nearby Bluetooth-enabled devices. It typically operates within a limited range (around 10–100 meters).

In the **Cloud-Mobile-IoT ecosystem**, Bluejacking is less of a data theft threat and more of an **annoyance** and a **Denial of Service (DoS) vulnerability** that can drain battery life or be used for social engineering (phishing). Security testing focuses on verifying the default settings and the ability of the device's operating system or application to properly handle incoming Bluetooth messages from unknown sources.

***

## 1. Detailed Testing Setup and Procedures

The testing process focuses on client configuration, battery resilience, and social engineering risk.

### 1.1. Message Sending Simulation (Black-box)
* **Procedure:** Use a Bluetooth-enabled laptop running **Bluez** (a Linux Bluetooth stack tool) or similar specialized mobile apps to scan for discoverable devices and send an unsolicited object/message (e.g., a vCard, note, or image) to a target mobile phone or IoT peripheral.
* **Goal:** Verify that devices with default settings are **not set to discoverable mode** permanently. If a device receives the message, ensure the operating system (OS) forces a **prompt for user approval** before any data transfer or notification occurs. This confirms the device is resistant to unauthorized push attacks.

### 1.2. Device Discoverability and Information Leakage (Black-box)
* **Procedure:** Use Bluetooth scanning tools like **hcitool** or **Kismet** to passively monitor the testing environment for devices advertising their presence via Bluetooth Low Energy (BLE) beacons or Classic Bluetooth.
* **Goal:**
    * Confirm that the device's advertised name (**Bluetooth Device Name**) does not contain personally identifiable information (PII).
    * Verify that any associated **IoT application** running on the mobile phone does not force the phone's Bluetooth to remain 'Always Discoverable' or 'Always On' when the application is in the background.

### 1.3. Denial of Service (DoS) and Battery Drain Testing (Gray-box)
* **Procedure:** Use **Custom Scripts** built with a tool like **Scapy** to rapidly flood the target device with continuous Bluetooth connection requests (pairing attempts or Service Discovery Protocol queries).
* **Goal:** Determine if the constant handling of unsolicited requests causes a significant **battery drain** or a noticeable **performance slowdown** (DoS) on the target mobile or IoT device. A resilient device should throttle connection attempts from the same source after a few failures.

### 1.4. Bluetooth Permission Review (White-box)
* **Procedure:** Conduct a **Manual Code Review** of the mobile application's manifest files and source code.
* **Goal:** Ensure that the application only requests the minimum necessary Bluetooth permissions (`BLUETOOTH`, `BLUETOOTH_ADMIN`, etc.) and does not attempt to enable discoverability or accept connections without the explicit, user-initiated intent. This prevents the application from inadvertently making the user vulnerable to Bluejacking.

## 2. Security Testing Approach & Tools

The testing setup involves simulating a Bluejacking attacker and monitoring how the client device (mobile phone or IoT peripheral) processes the unsolicited data and whether it exposes sensitive information through the Bluetooth stack.

<table style="border-collapse: collapse; width: 100%; border: 1px solid #000;">
  <thead>
    <tr>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Test Approach</th>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Analysis Type</th>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Approach Name</th>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Testing Tool</th>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Hyperlink for Tool</th>
      <th style="border: 1px solid #000; padding: 8px; text-align: left;">Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Black-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Message Sending Simulation</td>
      <td style="border: 1px solid #000; padding: 8px;">Bluejacking Tools (e.g., Bluez, BlueDump), Mobile Apps (Android/iOS)</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="http://www.bluez.org/" target="_blank" rel="noopener">Bluez</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Black-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Device Discoverability/Exposure</td>
      <td style="border: 1px solid #000; padding: 8px;">Bluetooth Scanners (e.g., hcitool, kismet/BTLE)</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="http://www.bluez.org/" target="_blank" rel="noopener">hcitool (BlueZ)</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Gray-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Denial of Service (DoS) Testing</td>
      <td style="border: 1px solid #000; padding: 8px;">Custom Scripts (Python/Scapy) for flooding the device with connection attempts</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://scapy.net/" target="_blank" rel="noopener">Scapy</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">White-box</td>
      <td style="border: 1px solid #000; padding: 8px;">SAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Bluetooth Permission Review</td>
      <td style="border: 1px solid #000; padding: 8px;">Manual Code Review</td>
      <td style="border: 1px solid #000; padding: 8px;">N/A (Manual process)</td>
      <td style="border: 1px solid #000; padding: 8px;">Android, iOS</td>
    </tr>
  </tbody>
</table>


---

## 3. References

1. Blancaflor, E., Purificacion, P. M. G., Atienza, R. B., Yao, J. J. M., & Alvarez, D. A. C. (2023). Exploring the depths of Bluetooth attacks: A critical analysis of Bluetooth exploitation and awareness of users. In *2023 6th International Conference on Computing and Big Data (ICCBD)* (pp. 52-59). IEEE.
2. Rohith, R., Moharir, M., & Shobha, G. (2018). SCAPY-A powerful interactive packet manipulation program. In *2018 international conference on networking, embedded and wireless systems (ICNEWS)* (pp. 1-5). IEEE.
3. Blancaflor, E., Billo, H. K., Dignadice, J. M., Domondon, P., Linco, M. R., & Valero, C. (2024). Bluetooth Simulated Reconnaissance Attack Through the Use of HCITool: A Case Study. In International Conference on Cloud Computing and Computer Networks (pp. 133-143). Cham: Springer Nature Switzerland.