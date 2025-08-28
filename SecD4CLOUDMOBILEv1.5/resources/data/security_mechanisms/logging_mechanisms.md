# Logging Mechanisms 

An inspection mechanism is a process or tool used to ensure that cloud-based mobile apps meet certain quality and security requirements. Inspection mechanisms involve thoroughly evaluating the source code, architecture, and security of the app to ensure it meets the desired standard. Examples of inspection mechanisms include static code analysis, application security testing, architectural design reviews, and penetration testing. These inspection mechanisms help identify any weaknesses, vulnerabilities, or security issues in the app before it is deployed in the cloud.

## Logging Mechanisms Examples: 

Security Requirement | Mobile Plataform | Mechanism | Description | OSI Layer |
:-------------: | :-------------: | :-------------: | :-------------: | :-------------:
Authentication | iOS | DeviceCheck | DeviceCheck enables customers to securely store small bits of data on Apple devices during the coding and runtime phases | Application |
Access Control | iOS | KeyChain | Apple’s Keychain, is a encrypted storage system that primarily stores passwords, certificates, and encryptionkeys| Application | 
Auditing | Android | Syslog | System logging mechanism for capturing and persistently logging system and audit-specific events in the Android OS | Transport |
Logging | Android | LumberJack | Logging mechanism for logging the events for mobile applications | Application |