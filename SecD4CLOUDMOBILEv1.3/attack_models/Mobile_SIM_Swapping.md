# Mobile SIM Swapping Attacks

This attack consists of fraudulently obtaining and using a target user's SIM card to gain unauthorized access to sensitive user data or to perform fraudulent activities, such as stealing money from a mobile banking application that requires factorial authentication, the second factor of which is a code sent by SMS to the customer's smartphone.

## Definition

 This attack targets the SIM card of a smartphone user, i.e. swapping the victim user's SIM card. SIM swapping can happen remotely. A cybercriminal, with a few important details about your life in hand, can answer security questions correctly, impersonate you, and convince your mobile carrier to reassign your phone number to a new SIM card. At that point, the criminal can get access to your phone’s data and start changing your account passwords to lock you out of your online banking profile, email, and more.

 ## Mitigation

1. **Two-Factor Authentication (2FA):** Implement 2FA to add an extra layer of security. However, avoid using SMS-based 2FA, as it can be vulnerable to SIM swapping. Instead, use app-based 2FA like Google Authenticator or hardware-based 2FA like YubiKey;
2. **Account Activity Monitoring:** Monitor account activities for any unusual behavior such as login from new devices or locations, which could indicate a SIM swap;
3. **Limit Personal Information Sharing:** Educate users not to share personal information, especially those used for security questions, on public platforms. This information can be used by attackers to impersonate the user and convince the telecom operator to swap the SIM;
4. **Use of Biometrics:** Use biometric authentication methods like fingerprint or facial recognition, which are harder for an attacker to replicate;
5. **Regular Updates and Patches:** Keep your systems and software up-to-date. Regular updates and patches can fix known vulnerabilities that could be exploited by SIM swapping attacks;
6. **User Awareness:** Educate users about the risks of SIM swapping attacks and how to identify potential threats. This includes training on how to recognize phishing attempts, unsafe websites, and malicious email attachments.

 ## Mobile SIM Swapping Risk Analysis
 
| **Factor**                                    | **Description**                                                                     | **Value**                             |
|-----------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------|
| Attack   Vector (AV):                         | Social   (Exploiting social engineering to manipulate the mobile carrier)           | Social   (S)                          |
| Attack   Complexity (AC):                     | Medium   (Requires social engineering skills and knowledge of victim's information) | Medium   (M)                          |
| Privileges   Required (PR):                   | None   (Attacker needs to trick the carrier)                                        | None   (N)                            |
| User   Interaction (UI):                      | None   (After initial social engineering)                                           | None   (N)                            |
| Scope   (S):                                  | Account   Compromise (attacker gains access to the user's account)                  |         Unauthorized Access (U)       |
| Confidentiality   Impact (C):                 | High   (attacker can access confidential data)                                      | High   (H)                            |
| Integrity   Impact (I):                       | High   (attacker can modify data)                                                   | High   (H)                            |
| Availability   Impact (A):                    | Medium   (attacker can potentially disrupt access for the legitimate user)          | Medium   (M)                          |
| Base   Score (assuming High for all impacts): | 0.85   * (AV:S/AC:M/PR:N/UI:N) * (S:U/C:H/I:H/A:M)                                  | 8.5   (High)                          |
| Temporal   Score (TS):                        | Not   Applicable (N/A)                                                              | N/A                                   |

**Overall, Mobile SIM Swapping poses a significant risk to mobile cloud-based applications that rely solely on SMS-based 2FA. Implementing stronger authentication methods and educating users about the risks can help mitigate this risk.**

## References
1. [Countering SIM-Swapping](https://www.enisa.europa.eu/publications/countering-sim-swapping).

## Mobile SIM Swapping Attacks Diagram
