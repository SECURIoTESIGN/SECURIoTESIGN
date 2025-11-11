# IoT Security Mechanisms

## Overview

IoT security is the practice that keeps your IoT systems safe. IoT security tools protect from threats and breaches, identify and monitor risks and can help fix vulnerabilities. IoT security ensures the availability, integrity, and confidentiality of your IoT solution¹.

Some security mechanisms for embedded IoT devices include malware protection, firmware security, OS hardening, secure software development, root-of-trust establishment, runtime integrity verification, remote attestation and secure update mechanisms². Security architectures, protocols and mechanisms for IoT systems include authentication, authorization, access control, auditing, intrusion detection, secured communications, lightweight and postquantum cryptography, key management and protection against denial-of-service attacks².

## IoT Security Mechanism Examples


<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="border: 1px solid gray; padding: 8px;">Security Requirement</th>
      <th style="border: 1px solid gray; padding: 8px;">Mobile Platform</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism</th>
      <th style="border: 1px solid gray; padding: 8px;">Description</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism Example</th>
      <th style="border: 1px solid gray; padding: 8px;">OSI Model Layer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Confidentiality</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Encryption is used to protect data from unauthorized access by converting it into a code that can only be read by those who have the key to decrypt it.</td>
      <td style="border: 1px solid gray; padding: 8px;">AES (Advanced Encryption Standard)</td>
      <td style="border: 1px solid gray; padding: 8px;">Presentation</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Integrity</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Digital Signatures</td>
      <td style="border: 1px solid gray; padding: 8px;">Digital signatures are used to ensure that data has not been tampered with during transmission. They provide a way to verify the authenticity and integrity of data.</td>
      <td style="border: 1px solid gray; padding: 8px;">RSA (Rivest–Shamir–Adleman)</td>
      <td style="border: 1px solid gray; padding: 8px;">Presentation</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Availability</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Redundancy</td>
      <td style="border: 1px solid gray; padding: 8px;">Redundancy is used to ensure that data is always available, even in the event of a failure. This can be achieved through the use of multiple servers or backup systems.</td>
      <td style="border: 1px solid gray; padding: 8px;">RAID (Redundant Array of Inexpensive Disks)</td>
      <td style="border: 1px solid gray; padding: 8px;">Network</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Passwords</td>
      <td style="border: 1px solid gray; padding: 8px;">Passwords are used to verify the identity of a user or device. They provide a way to ensure that only authorized users or devices have access to data or systems.</td>
      <td style="border: 1px solid gray; padding: 8px;">PBKDF2 (Password-Based Key Derivation Function 2)</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authorization</td>
      <td style="border: 1px solid gray; padding: 8px;">Android, iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Access Control Lists (ACLs)</td>
      <td style="border: 1px solid gray; padding: 8px;">Access control lists are used to determine who has access to what data or systems. They provide a way to control who can do what with data or systems.</td>
      <td style="border: 1px solid gray; padding: 8px;">RBAC (Role-Based Access Control)</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
  </tbody>
</table>


## References

1. Kalinin, E., Belyakov, D., Bragin, D., & Konev, A. (2021). IoT security mechanisms in the example of BLE. *Computers*, 10(12), 162.
2. Hassan, W. H. (2019). Current research on Internet of Things (IoT) security: A survey. *Computer networks*, 148, 283-294.
3. SMinoli, D., Sohraby, K., & Occhiogrosso, B. (2017, July). Iot security (IoTsec) mechanisms for e-health and ambient assisted living applications. In *2017 IEEE/ACM International Conference on Connected Health: Applications, Systems and Engineering Technologies (CHASE)* (pp. 13-18). IEEE.
