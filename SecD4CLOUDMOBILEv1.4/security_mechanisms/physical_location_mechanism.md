# Physical Location Mechanisms 

Security physical location mechanisms are applied to cloud-based mobile apps to ensure that user data is not accessed or stored from locations outside of an approved geographic region. These mechanisms include technologies such as geofencing and IP address tracking. Geofencing verifies that user data is being accessed and stored within a predetermined geographic area by creating a virtual fence around the area. IP address tracking allows mobile apps to identify the geographical location associated with a particular IP address in order to verify that a user is located in the approved geographic area. These security location mechanisms are essential for cloud-based mobile apps, as they help prevent unauthorized access to user data from malicious actors located in remote locations.

## Physical Location Mechanisms Examples: 

Security Requirement | Mobile Platform | Mechanism | Description | OSI Layer
 :---: | :---: | :---: | :---: | :---:
Authenticated Access | iOS | Biometric Scanner | Uses user's fingerprints as part of the authentication process | Physical
Data Integrity | Android | Transparent Encryption | Files are encrypted transparently and automatically | Network
Data Availability | Both | Secure Boot & Root | Ensures that all parts of system are authenticated and verified | Physical
Data Confidentiality | iOS | App sandboxes | Prevents unauthorized access to specific files | Application
Data Security | Android | Full Disk Encryption | Encrypts all data on device | Network