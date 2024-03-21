# Bluesnarfing Attack 

Bluesnarfing attack is a type of wireless attack that allows attackers to gain unauthorized access to data stored on a Bluetooth-enabled device. The attacker is able to connect to an exposed Bluetooth-enabled device without the user's knowledge, and then transfer data stored on it, such as contact lists, calendar events, and text messages. Because Bluetooth-enabled devices frequently remain in discoverable mode, even if they are not actively in use, they can be vulnerable to this kind of attack.

## Bluesnarfing Architectural Risk Analysis: 

**Bluesnarfing Vulnerability - Risk Analysis Using CVSS v3.1**

- **Attack Vector (AV):** Remote
- **Attack Complexity (AC):** Low
- **Privileges Required (PR):** None
- **User Interaction (UI):** None
- **Scope (S):** Changed
- **Confidentiality (C):** High
- **Integrity (I):** Low
- **Availability (A):** Low

**CVSS Base Score:** 6.5
 
**CVSS Vector String:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:L

Bluesnarfing is a type of attack that takes advantage of a Bluetooth connection between two devices. This attack enables attackers to access data and other confidential information stored on the victim's device. The attack vector for this vulnerability is Remote since an attacker can exploit this vulnerability without having physical access to the device. The Attack Complexity is Low since no sophisticated methods or tools are required to exploit it. No privilege is required to exploit this vulnerability. Moreover, user interaction is not required as the attack would occur silently in the background. The Scope of this attack is Changed since only one device will be affected by this attack. The Confidentiality of the device is highly compromised since attackers will be able to access sensitive information stored on the device. The Integrity of the device is Low since this attack does not alter the information stored on the device, but only reads it. Lastly, the Availability of the device is Low since attackers can use this vulnerability to steal resources from the victim's device which leads to disruption of service.

Therefore, the overall risk score for this vulnerability is 6.5 based on the CVSS v3.1 Common Vulnerability Scoring System.

## Bluetooth Attack Tree