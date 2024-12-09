# Device Detection Mechanisms 

Security Device Tamper Detection Mechanisms (SDTDM) in cloud-based mobile apps are security measures designed to detect when an application has been altered or interfered with in a malicious manner. These mechanisms rely on a variety of techniques, such as application behavior monitoring, code validation, application certificate inspection, and digital signature verification. Applying these measures helps to protect against attack attempts, such as reverse engineering or tampering, which can damage the integrity and reliability of a mobile application, and leave it vulnerable to cyber attacks.

## Device Tamper Detection Mechanisms Examples: 

| Security Requirement | Mobile Plataform | Mechanism | Description | OSI Layer | 
| :--- | :--- | :--- | :--- | :--- | 
| Coding Phase | Android | Smali Anti-Tamper | Software code is compiled to native assembly code only found in Smali folders, making it more difficult to find and modify. | Application Layer |
| Coding Phase | Android | Proguard | Software code is obfuscated, reducing the change of code tampering by making the code difficult to understand or modify. | Application Layer |
| Runtime | Android | Device Profiling | Leverage Device-Based Data to detect unusual or suspicious behavior indicative of tampering. | Presentation Layer |
| Runtime | iOS | Secure Boot Chain | Checking the Integrity and authenticity of the bootloaders, kernel, and signature of the system partition. | Network Layer |
| Runtime | iOS | Runtime Integrity Checks | Tamper detection checks executed at runtime to ensure integrity and accuracy of code and data | Application Layer |