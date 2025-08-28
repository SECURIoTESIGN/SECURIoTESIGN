# IoT Security Mechanisms

## Overview

IoT security is the practice that keeps your IoT systems safe. IoT security tools protect from threats and breaches, identify and monitor risks and can help fix vulnerabilities. IoT security ensures the availability, integrity, and confidentiality of your IoT solution¹.

Some security mechanisms for embedded IoT devices include malware protection, firmware security, OS hardening, secure software development, root-of-trust establishment, runtime integrity verification, remote attestation and secure update mechanisms². Security architectures, protocols and mechanisms for IoT systems include authentication, authorization, access control, auditing, intrusion detection, secured communications, lightweight and postquantum cryptography, key management and protection against denial-of-service attacks².

## IoT Security Mechanism Examples


| Security Requirement | Mobile Platform | Mechanism | Description | Mechanism Example | OSI Model Layer |
| --- | --- | --- | --- | --- | --- |
| Confidentiality | Android, iOS | Encryption | Encryption is used to protect data from unauthorized access by converting it into a code that can only be read by those who have the key to decrypt it. | AES (Advanced Encryption Standard) | Presentation |
| Integrity | Android, iOS | Digital Signatures | Digital signatures are used to ensure that data has not been tampered with during transmission. They provide a way to verify the authenticity and integrity of data. | RSA (Rivest–Shamir–Adleman) | Presentation |
| Availability | Android, iOS | Redundancy | Redundancy is used to ensure that data is always available, even in the event of a failure. This can be achieved through the use of multiple servers or backup systems. | RAID (Redundant Array of Inexpensive Disks) | Network |
| Authentication | Android, iOS | Passwords | Passwords are used to verify the identity of a user or device. They provide a way to ensure that only authorized users or devices have access to data or systems. | PBKDF2 (Password-Based Key Derivation Function 2) | Application |
| Authorization | Android, iOS | Access Control Lists (ACLs) | Access control lists are used to determine who has access to what data or systems. They provide a way to control who can do what with data or systems. | RBAC (Role-Based Access Control) | Application |

## References

(1) IoT Security - A Safer Internet of Things (for 2022) - Thales. https://www.thalesgroup.com/en/markets/digital-identity-and-security/iot/iot-security.
(2) Sensors | Special Issue : Security and Privacy in IoT Systems and .... https://www.mdpi.com/journal/sensors/special_issues/SP_IoT.
(3) Security best practices - Azure IoT | Microsoft Learn. https://learn.microsoft.com/en-us/azure/iot/iot-security-best-practices.
