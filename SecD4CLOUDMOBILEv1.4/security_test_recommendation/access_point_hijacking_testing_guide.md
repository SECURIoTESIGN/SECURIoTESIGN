# Security Testing Setup for Access Point Hijacking Attacks

## 1. Overview

A detailed security testing setup for **Access Point (AP) Hijacking Attacks** requires simulating the malicious environment to test the defensive capabilities of client devices (Mobile and IoT) against traffic interception and manipulation. The focus is on validating the implementation of **Certificate Pinning** and **secure authentication protocols**.

---

## 2. Detailed Testing Setup and Procedures

The testing process is divided into simulating the attack and verifying the client defenses.

### Rogue AP Simulation and Connection Testing (Black-box)

* **Procedure:** Set up a laptop running a Linux distribution like **Kali Linux** with an external Wi-Fi adapter. Use tools like `hostapd` or `airbase-ng` to create an **Evil Twin** AP with the exact same SSID and security settings as a trusted network (e.g., a corporate or home Wi-Fi).
* **Goal:** Observe whether the mobile/IoT client automatically connects to the rogue AP. Once connected, confirm if the client attempts to transmit any data (especially credentials or initial authentication tokens) before TLS handshaking is completed.

### MITM and Certificate Pinning Validation (Gray-box/White-box)

* **Procedure:** Route all client traffic through a tool like **Burp Suite Professional** or **mitmproxy** running in transparent proxy mode. The proxy is configured to intercept and forge the SSL/TLS certificate used by the target cloud service (acting as the MITM).
* **Goal (Gray-box/DAST):** If the client is successfully connected to the rogue AP, attempt to access the cloud API. A secure client implementing **Certificate Pinning** should immediately **terminate the connection** and fail with a certificate error (e.g., `SSLHandshakeException`), preventing the MITM from capturing or altering data.
* **Goal (White-box/SAST):** Use **SonarQube** or manual review to inspect the source code. Verify that the client application network library is configured to perform explicit pinning (i.e., comparing the server public key or certificate hash against a hardcoded value) and that the exception handling for a pinning failure is secure (e.g., stops execution, does not fall back to unencrypted communication).

### Protocol Downgrade and DNS Hijacking Testing (Black-box)

* **Procedure:**
    * **Downgrade:** Use **mitmproxy** to actively strip the HTTPS connection, forcing the client to communicate over unencrypted HTTP.
    * **DNS Hijacking:** Configure the rogue AP DHCP server to issue a malicious DNS server address (using **DNSMasq**). This malicious DNS server is set to redirect the target domain (e.g., `api.cloudservice.com`) to the attacker server IP address.
* **Goal:** Ensure the client application **refuses to communicate** over the downgraded (HTTP) protocol. Verify that even when the client resolves the API domain to the attacker IP (via the malicious DNS), the subsequent secure connection attempt fails due to **Certificate Pinning** rejecting the attacker forged TLS certificate.

### IoT Firmware and Gateway Vetting (White-box/DAST)

* **Procedure:** Directly scan the IP address of the target IoT gateway (AP) using a comprehensive **vulnerability scanner** like **Nessus**.
* **Goal:** Identify default credentials, unpatched firmware vulnerabilities, or open management ports that an attacker could exploit to gain administrative control over the legitimate AP. This models the initial compromise phase of a DNS Hijacking attack on the router itself.

---

## 3. Security Testing Approach & Tools



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
      <td style="border: 1px solid #000; padding: 8px;">Rogue AP/Evil Twin Simulation</td>
      <td style="border: 1px solid #000; padding: 8px;">Kali Linux (using <code>airbase-ng</code> or <code>hostapd</code>)</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://www.kali.org/" target="_blank" rel="noopener">Kali Linux</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Gray-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">MITM Traffic Interception/Validation</td>
      <td style="border: 1px solid #000; padding: 8px;">Burp Suite Professional</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://portswigger.net/burp/pro" target="_blank" rel="noopener">Burp Suite Pro</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">White-box</td>
      <td style="border: 1px solid #000; padding: 8px;">SAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Code Review (Certificate Pinning Enforcement)</td>
      <td style="border: 1px solid #000; padding: 8px;">SonarQube</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://www.sonarsource.com/products/sonarqube/" target="_blank" rel="noopener">SonarQube</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Android, iOS</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Black-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Protocol Downgrade Testing (SSL Stripping)</td>
      <td style="border: 1px solid #000; padding: 8px;">mitmproxy</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://mitmproxy.org/" target="_blank" rel="noopener">mitmproxy</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Black-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">DNS Hijacking Testing</td>
      <td style="border: 1px solid #000; padding: 8px;">DNSMasq</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="http://www.thekelleys.org.uk/dnsmasq/doc.html" target="_blank" rel="noopener">DNSMasq</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">White-box</td>
      <td style="border: 1px solid #000; padding: 8px;">SAST/DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Firmware Vulnerability Scanning (IoT APs)</td>
      <td style="border: 1px solid #000; padding: 8px;">Nessus</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://www.tenable.com/products/nessus" target="_blank" rel="noopener">Nessus</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">IoT Gateway/Router</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;">Gray-box</td>
      <td style="border: 1px solid #000; padding: 8px;">DAST</td>
      <td style="border: 1px solid #000; padding: 8px;">Session Integrity Check (Post-MITM)</td>
      <td style="border: 1px solid #000; padding: 8px;">Wireshark</td>
      <td style="border: 1px solid #000; padding: 8px;">
        <a href="https://www.wireshark.org/" target="_blank" rel="noopener">Wireshark</a>
      </td>
      <td style="border: 1px solid #000; padding: 8px;">Both</td>
    </tr>
  </tbody>
</table>


---

## 4. References

1.  LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). *Microsoft Press*.
2. Xia, H., Brustoloni, J. (2004). Detecting and Blocking Unauthorized Access in Wi-Fi Networks. In: Mitrou, N., Kontovasilis, K., Rouskas, G.N., Iliadis, I., Merakos, L. (eds) Networking 2004. NETWORKING 2004. *Lecture Notes in Computer Science*, vol 3042. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-540-24693-0_65](https://doi.org/10.1007/978-3-540-24693-0_65).
3. Golightly, L., Chang, V., Xu, Q.A. (2021). Towards Ethical Hacking—The Performance of Hacking a Router. In: Jahankhani, H., Kendzierskyj, S., Akhgar, B. (eds) Information Security Technologies for Controlling Pandemics. Advanced Sciences and Technologies for Security Applications. Springer, Cham. [https://doi.org/10.1007/978-3-030-72120-6_17](https://doi.org/10.1007/978-3-030-72120-6_17).
