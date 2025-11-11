# Security Testing for Man-in-the-Middle Attacks

## 1. Overview

Man-in-the-Middle (MiTM) attacks allow an adversary to intercept, modify or inject communications between endpoints. In a combined cloud-mobile-IoT environment, the breadth of endpoints (IoT sensors, mobile clients, gateways, cloud APIs) increases the attack surface, especially when devices use weak protocols, unverified certificates, or are on untrusted networks. For example, many IoT clouds accept weak TLS versions, making MiTM easier. 

---

## 2. High-level Testing Workflow / Setup

1. **Scope & threat modelling**

   * Map all communication channels: IoT devices &rarr; gateways &rarr; cloud, mobile apps &harr; cloud, mobile apps &harr; IoT/gateway.
   * Identify susceptible protocols/network segments: e.g., WiFi, MQTT, HTTP/HTTPS, Bluetooth, cellular.
   * Identify trust boundaries and certificate/identity management across devices, mobile apps and cloud.
   * Define possible MiTM vectors: rogue access points, ARP/DNS spoofing on IoT/edge networks, Proxy apps on mobile, compromised gateway, unsecured mobile hotspot, weak-TLS IoT cloud endpoint.

2. **Baseline behaviour capture**

   * Record normal traffic flows: device registration, telemetry sends, mobile &harr; cloud API calls, IoT &harr; gateway communications.
   * Check certificate validation behaviour, handshake protocols, TLS versions, whether devices accept self-signed certs or skip validation.

3. **Static analysis (SAST) & configuration review**

   * Examine firmware/mobile app/cloud backend source/config: verify certificate pinning, TLS protocol enforcement, secure defaults, verification of server identity.
   * Check IoT device firmware for insecure fallback (plaintext, weak encryption), check mobile app network libraries, cloud API endpoints for insecure defaults.

4. **Dynamic testing (DAST) / MiTM simulation**

   * Set up a rogue network (e.g., WiFi access point) to simulate mobile MiTM: mobile connects, attacker intercepts traffic, tries SSL stripping, DNS spoofing, proxying mobile traffic (e.g., mitmproxy).
   * For IoT/gateway: use ARP spoofing, DNS redirect, downgrade TLS, intercept MQTT or CoAP traffic between device and cloud/gateway. See if device accepts compromised cert or unverified endpoint.
   * On cloud side: intercept mobile/gateway requests, attempt injection/modification of telemetry or commands, test if backend validates identity of source.

5. **Network & telemetry monitoring tests**

   * Capture network traffic (Wireshark, Zeek) from devices/gateway/mobile while under MiTM to see if anomalies are logged.
   * Use monitoring/alerting to check for certificate mismatches, repeated TLS renegotiation, unusual endpoints, or decrypted traffic being forwarded.

6. **Mobile & IoT integration tests**

   * Mobile: Install a proxy certificate or set up a custom CA on device to simulate MiTM; test mobile app response.
   * IoT: Insert a test rogue gateway or rogue device that captures/intercepts device ↔ cloud communications; test device’s behavior when gateway is malicious.

7. **Reporting & remediation**

   * Identify weak points: unverified certificates, weak TLS versions, lack of certificate pinning on mobile, insecure IoT protocol, network segments lacking encryption or authentication, lack of detection/alerts for MiTM.
   * Recommend controls: enforce TLS 1.2/1.3, certificate pinning/mobile secure libraries, mutual authentication for IoT devices and gateways, network segmentation, monitoring/UEBA for unusual flows, mobile/hotspot policy enforcement.
   * Validate by retesting after mitigation.

---

## 3. Security Test Approach & tools


<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Test approach</th>
      <th>Analysis Type</th>
      <th>Approach name</th>
      <th>Testing Tool</th>
      <th>Tool Hyperlink</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Network packet sniffing & MiTM traffic intercept</td>
      <td>Wireshark / Zeek</td>
      <td><a href="https://www.wireshark.org/">Wireshark</a> / <a href="https://www.zeek.org/">Zeek</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Proxying mobile traffic / SSL-strip simulation</td>
      <td>mitmproxy</td>
      <td><a href="https://mitmproxy.org/">Proxying</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Mobile app / IoT firmware review for certificate validation</td>
      <td>Ghidra / Binwalk (firmware) / Static code analysis</td>
      <td><a href="https://ghidra-sre.org/">Ghidra</a> / <a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a></td>
      <td>Android, IoT</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Rogue access point / ARP-spoof/ DNS-spoof tests on IoT/gateway network</td>
      <td>ettercap / ARP-poison scripts</td>
      <td><a href="https://github.com/Ettercap/ettercap">ettercap</a></td>
      <td>IoT/gateway network</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile app instrumentation for certificate pinning & trust issues</td>
      <td>Frida</td>
      <td><a href="https://frida.re/">Frida</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud backend API review for TLS enforcement / mutual auth</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Cloud</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Monitoring & anomaly detection of MiTM behaviour in IoT/mobile network flows</td>
      <td>Elastic Stack (beats + SIEM) / Splunk</td>
      <td><a href="https://www.elastic.co/elastic-stack/">Elastic Stack</a> / <a href="https://www.splunk.com/">Splunk</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>IoT device firmware review of insecure network protocol usage</td>
      <td>Binwalk + radare2</td>
      <td><a href="https://rada.re/n/">radare2</a></td>
      <td>IoT</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Mobile hotspot MiTM simulation (rogue AP) for mobile–cloud traffic</td>
      <td>Hostapd + WiFi pineapple</td>
      <td><a href="https://github.com/PeterBuss/hostapd-wpe">Hostapd</a></td>
      <td>Android, iOS</td>
    </tr>
  </tbody>
</table>

---

## 4. Practical Testbed / Setup Checklist

* **Network lab environment**: Set up IoT devices, gateways, mobile clients, cloud backend connections. Include typical device↔gateway↔cloud flows.
* **Rogue network equipment**: Use a WiFi Pineapple or hostapd-WPE (wireless rogue AP), or a switch-span port + ARP-spoof tool to act as intermediary.
* **Traffic capture & analysis**: Place span port/mirror in gateway network; capture IoT device ↔ gateway, mobile ↔ cloud traffic using Wireshark/Zeek.
* **Mobile device instrumentation**: Use Android (rooted/emulated) and iOS (developer mode) devices. Install a custom CA certificate for interception. Use mitmproxy to inspect mobile app outbound traffic.
* **IoT device firmware inspection**: Extract firmware (Binwalk), analyze for usage of plain-text protocols, unverified TLS, insecure fallback. Simulate MiTM by intercepting device ↔ cloud traffic and attempt injection/modification of commands/data.
* **Backend/cloud API review**: Check TLS enforcement, certificate validation, mutual authentication, endpoint whitelist, monitoring of new client IPs, new device registrations.
* **Detection & logging setup**: Configure SIEM/UEBA on cloud and network segments to alert on anomalies: e.g., device connecting from unexpected MAC, IoT device sending commands with altered payloads, mobile app sessions with invalid cert chain.
* **Simulation of MiTM attacks**:

  * Mobile: Connect to rogue AP, intercept mobile app communications, attempt injection/modification of requests, observe backend and mobile app behaviour.
  * IoT/gateway: ARP spoof gateway, redirect IoT device communications to malicious gateway, alter telemetry or commands, observe device authentication failures or backend detection.
  * Cloud: Insert proxy between mobile/gateway and cloud API, modify TLS handshake or downgrade TLS version, see if cloud logs detect certificate anomalies.
* **Reporting and remediation**: Document vulnerable device types, network segments, apps lacking certificate pinning, backend APIs allowing weak TLS. Recommend mitigation: enforce TLS1.2+, certificate pinning on mobile, mutual auth for IoT devices, network segmentation, anomaly detection for MiTM. Retest after applying fixes.

---

## 5. References

1. Fereidouni, H., Fadeitcheva, O., & Zalai, M. (2025). IoT and man‐in‐the‐middle attacks. *Security and Privacy*, 8(2), e70016.
2. Aoueileyine, M. O. E., Karmous, N., Bouallegue, R., Youssef, N., & Yazidi, A. (2024, April). Detecting and mitigating MiTM attack on IOT devices using SDN. In *International Conference on Advanced Information Networking and Applications* (pp. 320-330). Cham: Springer Nature Switzerland.
3. Thankappan, M., et al. (2023). Multi-channel Man-in-the-Middle Attacks Against Protected Wi-Fi Networks and Their Attack Signatures. In: Mercier-Laurent, E., Fernando, X., Chandrabose, A. (eds) Computer, Communication, and Signal Processing. AI, Knowledge Engineering and IoT for Smart Systems. ICCCSP 2023. IFIP Advances in Information and Communication Technology, vol 670. Springer, Cham. https://doi.org/10.1007/978-3-031-39811-7_22.
4. Alrubayyi, H., Alshareef, M. S., Nadeem, Z., Abdelmoniem, A. M., & Jaber, M. (2024). Security threats and promising solutions arising from the intersection of AI and IoT: a study of IoMT and IoET applications. *Future Internet*, 16(3), 85.