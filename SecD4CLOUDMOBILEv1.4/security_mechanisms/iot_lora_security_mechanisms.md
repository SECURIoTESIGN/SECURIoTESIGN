# IoT and LoRa Security Mechanisms

The IoT ecosystem offers a flexible approach to organizing smart applications and constructing consumer-oriented infrastructure. However, several issues affect the security and privacy of the parties involved, particularly concerning low-power IoT devices. Often, there is a trade-off between implementing cybersecurity measures and maintaining operational efficiency within established tolerances. Consequently, the implementation of data protection and cyber defense mechanisms tends to be prioritized last.

Below is a summary of the security mechanisms to be implemented for the IoT and LoRa/NB-IoT ecosystem.


<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="border: 1px solid gray; padding: 8px;">Security Requirement</th>
      <th style="border: 1px solid gray; padding: 8px;">Mobile Platform</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism Name</th>
      <th style="border: 1px solid gray; padding: 8px;">Description</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism Example</th>
      <th style="border: 1px solid gray; padding: 8px;">OSI Model Layer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Data Confidentiality</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">End-to-End Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures that only authorized parties can access data in transit.</td>
      <td style="border: 1px solid gray; padding: 8px;">TLS 1.3 for HTTPS communication between app and cloud</td>
      <td style="border: 1px solid gray; padding: 8px;">Transport, Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">AES Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Encrypts sensitive data stored on devices and in the cloud.</td>
      <td style="border: 1px solid gray; padding: 8px;">AES-256 for local storage and cloud databases</td>
      <td style="border: 1px solid gray; padding: 8px;">Application, Presentation</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Data Integrity</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Data Integrity Checks</td>
      <td style="border: 1px solid gray; padding: 8px;">Validates that data is not altered during transmission or storage.</td>
      <td style="border: 1px solid gray; padding: 8px;">HMAC-SHA256 for message authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Transport, Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Digital Signatures</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures authenticity and integrity of data sent between devices and servers.</td>
      <td style="border: 1px solid gray; padding: 8px;">RSA/ECC signatures for sensitive data exchange</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td rowspan="3" style="border: 1px solid gray; padding: 8px;">User Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">OAuth 2.0 / OpenID Connect</td>
      <td style="border: 1px solid gray; padding: 8px;">Secure user authentication to access cloud services.</td>
      <td style="border: 1px solid gray; padding: 8px;">Firebase Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Biometric Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures only authorized users can access the app.</td>
      <td style="border: 1px solid gray; padding: 8px;">Face ID / Touch ID</td>
      <td style="border: 1px solid gray; padding: 8px;">Application, Presentation</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Multi-Factor Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Adds an extra layer of security by combining passwords and OTPs.</td>
      <td style="border: 1px solid gray; padding: 8px;">Google Authenticator</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <!-- Additional rows continue below -->
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Access Control</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Role-Based Access Control</td>
      <td style="border: 1px solid gray; padding: 8px;">Restricts access based on user roles to limit data exposure.</td>
      <td style="border: 1px solid gray; padding: 8px;">AWS IAM Policies</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Mobile Device Management</td>
      <td style="border: 1px solid gray; padding: 8px;">Enforces security policies on mobile devices, especially for lost/stolen cases.</td>
      <td style="border: 1px solid gray; padding: 8px;">Microsoft Intune</td>
      <td style="border: 1px solid gray; padding: 8px;">Application, Network</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Data Privacy</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Data Anonymization</td>
      <td style="border: 1px solid gray; padding: 8px;">Protects user privacy by masking personal identifiers before analysis.</td>
      <td style="border: 1px solid gray; padding: 8px;">Pseudonymizing names and addresses</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Encrypted Identifiers</td>
      <td style="border: 1px solid gray; padding: 8px;">Uses temporary, encrypted IDs for user tracking to protect privacy.</td>
      <td style="border: 1px solid gray; padding: 8px;">Subscription Concealed Identifier (SUCI) in 5G</td>
      <td style="border: 1px solid gray; padding: 8px;">Network, Application</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Secure Communication</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">VPN / IPsec</td>
      <td style="border: 1px solid gray; padding: 8px;">Encrypts all traffic over untrusted networks, like public Wi-Fi.</td>
      <td style="border: 1px solid gray; padding: 8px;">OpenVPN or IPsec for Ethernet connections</td>
      <td style="border: 1px solid gray; padding: 8px;">Network, Data Link</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">LoRaWAN AES Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Encrypts data transmitted over LoRa networks.</td>
      <td style="border: 1px solid gray; padding: 8px;">LoRaWAN AES-128 for IoT sensor data</td>
      <td style="border: 1px solid gray; padding: 8px;">Network, Data Link</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Device Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">IoT Devices</td>
      <td style="border: 1px solid gray; padding: 8px;">Device Certificates</td>
      <td style="border: 1px solid gray; padding: 8px;">Authenticates IoT devices to prevent unauthorized access.</td>
      <td style="border: 1px solid gray; padding: 8px;">X.509 certificates for device authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Data Link, Network</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Mutual Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures both server and device verify each other's identity.</td>
      <td style="border: 1px solid gray; padding: 8px;">TLS with mutual certificates</td>
      <td style="border: 1px solid gray; padding: 8px;">Transport, Application</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Network Security</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Firewalls</td>
      <td style="border: 1px solid gray; padding: 8px;">Filters network traffic to block malicious connections.</td>
      <td style="border: 1px solid gray; padding: 8px;">Cloudflare WAF for cloud server protection</td>
      <td style="border: 1px solid gray; padding: 8px;">Network</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">IoT Devices</td>
      <td style="border: 1px solid gray; padding: 8px;">Intrusion Detection Systems</td>
      <td style="border: 1px solid gray; padding: 8px;">Monitors traffic for suspicious activities and potential breaches.</td>
      <td style="border: 1px solid gray; padding: 8px;">Snort IDS for IoT and cloud networks</td>
      <td style="border: 1px solid gray; padding: 8px;">Network, Application</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Data Availability</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">DDoS Protection</td>
      <td style="border: 1px solid gray; padding: 8px;">Protects the cloud backend from Distributed Denial of Service attacks.</td>
      <td style="border: 1px solid gray; padding: 8px;">AWS Shield for cloud services</td>
      <td style="border: 1px solid gray; padding: 8px;">Network, Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Load Balancers</td>
      <td style="border: 1px solid gray; padding: 8px;">Distributes traffic to prevent overload and ensure service uptime.</td>
      <td style="border: 1px solid gray; padding: 8px;">AWS Elastic Load Balancer</td>
      <td style="border: 1px solid gray; padding: 8px;">Transport</td>
    </tr>
<tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Firmware and Software Updates</td>
      <td style="border: 1px solid gray; padding: 8px;">IoT Devices</td>
      <td style="border: 1px solid gray; padding: 8px;">Secure Firmware Updates</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures devices receive authenticated and encrypted updates.</td>
      <td style="border: 1px solid gray; padding: 8px;">Over-the-air updates with digital signatures</td>
      <td style="border: 1px solid gray; padding: 8px;">Application, Data Link</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">App Store Verification</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures only approved and verified apps are installed on devices.</td>
      <td style="border: 1px solid gray; padding: 8px;">Google Play Protect / Apple App Store policies</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td rowspan="2" style="border: 1px solid gray; padding: 8px;">Compliance & Auditing</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Logging & Auditing</td>
      <td style="border: 1px solid gray; padding: 8px;">Tracks access and changes to sensitive data for compliance.</td>
      <td style="border: 1px solid gray; padding: 8px;">AWS CloudTrail for monitoring access logs</td>
      <td style="border: 1px solid gray; padding: 8px;">Application, Network</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">GDPR / CCPA Compliance</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures compliance with data protection regulations for user data.</td>
      <td style="border: 1px solid gray; padding: 8px;">User data access requests, consent management</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>

  </tbody>
</table>

## References 
  |
1. Bouzidi, M., Gupta, N., Cheikh, F. A., Shalaginov, A., & Derawi, M. (2022). A novel architectural framework on IoT ecosystem, security aspects and mechanisms: a comprehensive survey. IEEE Access, 10, 101362-101384.
2. Devalal, S., & Karthikeyan, A. (2018, March). LoRa technology-an overview. In 2018 second international conference on electronics, communication and aerospace technology (ICECA) (pp. 284-290). IEEE.
