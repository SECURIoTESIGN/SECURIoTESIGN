# Malicious Insider Attack 

Malicious insider attack is when a person with authorized access to an organization's systems and networks misuses their privileges to damage the organization's information systems, applications or data. This type of attack can lead to complete system or network shutdown, data theft, fraud or other malicious activities. 

## Mitigation
The malicious insider threat is one of the most difficult threats to detect because the insider has legitimate access and is part of the organization which makes it hard to identify the malicious activity. Some of the most preventative measures organizations can take to mitigate against malicious insider attacks are: 

1. **Least Privilege Principle:** Implement the principle of least privilege. Each user should have the minimum levels of access necessary to perform their job functions;
2. **User Access Reviews:** Regularly review user access rights and privileges. This can help identify any inappropriate access rights that could be exploited by a malicious insider;
3. **Separation of Duties:** Implement separation of duties. This can prevent any single user from having control over an entire process, making it harder for a malicious insider to cause significant damage;
4. **Monitoring and Auditing:** Implement monitoring and auditing of user activities. This can help detect any unusual or suspicious behavior that could indicate a malicious insider;
5. **Security Training and Awareness:** Provide regular security training and awareness programs. This can help employees understand the risks associated with their actions and encourage them to report any suspicious activities;
6. **Incident Response Plan:** Have an incident response plan in place. This can help your organization respond quickly and effectively if a malicious insider is detected.

## Malicious Insider Architectural Risk Analysis


| **Factor**                                  | **Description**                                                                                 | **Value**                        |
|---------------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------|
| Attack Vector (AV):                         | Internal (Exploiting authorized access)                                                         | Internal (I)                     |
| Attack Complexity (AC):                     | Low (Insider already has access)                                                                | Low (L)                          |
| Privileges Required (PR):                   | Varies (Depends on insider's privileges)                                                        | Low (L), Medium (M), or High (H) |
| User Interaction (UI):                      | May be required (Depends on insider's actions)                                                  | Required (R) or None (N)         |
| Scope (S):                                  | Unauthorized Access (insider gains unauthorized access to data or modifies it)                  | Unauthorized Access (U)          |
| Confidentiality Impact (C):                 | High (insider can access confidential data)                                                     | High (H)                         |
| Integrity Impact (I):                       | High (insider can modify data)                                                                  | High (H)                         |
| Availability Impact (A):                    | High (insider can disrupt application or data access)                                           | High (H)                         |
| Base Score (assuming High for all impacts): | 0.85 * (AV:I/AC:L/PR:V/UI:R) * (S:U/C:H/I:H/A:H)                                                | 9.0 (Critical)                   |
| Temporal Score (TS):                        | Not applicable (N/A)                                                                            | N/A                              |
| Environmental Score (ES):                   | Depends on access controls, data encryption, monitoring and detection practices                 | Varies                           |
| Overall CVSS Score                          | Base Score + TS + ES                                                                            | Varies (Depends on ES)           |
| Risk Rating                                 | High to Critical (Depends on ES)                                                                | High to Critical                 |

## Malicious Insider Attack Tree Diagram