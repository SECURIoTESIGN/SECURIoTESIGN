# Malicious QR Code Attack 

Malicious QR Code attacks involve the use of QR codes (Quick Response Code) that, when scanned by unsuspecting users, can launch malicious applications or websites that contain malware. These QR Codes can be found in emails, websites, ads, or printed material, and can be used by hackers to launch malicious code on user devices.

In order to protect against malicious QR code attacks, users should be aware of what kind of content they are accessing through their devices and avoid clicking on any suspicious links. Furthermore, if a user is unsure of a QR code's origin, it is important to scan the code using specialized software (e.g. antivirus and anti-malware programs) to ensure it is safe before interacting with it.

## Malicious QR Code Architectural Risk Analysis: 

**Arquitectural Risk Analysis of Malicious QR Code Vulnerability**

**CVSS v3.1 Base Score: 8.8 (High)**

**Vector: AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H**

**Impact Subscore: 6.6**

Malicious QR codes are physical objects which contain malicious code which may execute on devices when scanned by a camera. The risk posed by malicious QR codes is that they may allow malicious code to be executed on a device without the user's knowledge or consent. Such malicious code could be a payload that contains a malicious program or script, which may execute malicious code or exfiltrate data from the device.

The Arquitectural Risk Analysis of this vulnerability consists of the following:

**Attack Vector (AV): Local**
The malicious code is embedded in the physical QR code which must be scanned in order to execute.

**Attack Complexity (AC): High**
Scanning the code and executing the malicious code requires physical access to the QR codes as well as considerable technical expertise.

**Privileges Required (PR): None**
No user privileges are necessary for the malicious code to execute.

**User Interaction (UI): None**
No user interaction is necessary to exploit the vulnerability.

**Scope (S): Unchanged**
The malicious code remains confined to the device in which it was executed.

**Confidentiality (C): High**
Data on the device may be stolen or altered if the malicious code is successful.

**Integrity (I): High**
The malicious code could corrupt data on the device, or inject malicious code that could remain hidden after the malicious code is executed.

**Availability (A): High**
The malicious code could disrupt the operation of the device, or cause the device to become unresponsive.