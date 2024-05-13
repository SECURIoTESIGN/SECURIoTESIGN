# Wi-Fi Jamming Attack 

Wi-Fi jamming attack is an attack on a wireless network using radio frequency signals to disrupt the normal operation of the network. The goal of the attack is to block or reduce the amount of legitimate traffic that can access the network. This can be done by using powerful signal transmitters to disrupt communications between the access point and its client devices or by blocking the access point’s radio signal. 

Wi-Fi jamming attacks are a type of denial of service attack that affects wireless networks and can occur on any wireless network regardless of its size. It can cause network outages, reduce throughput, and cause major disruptions for users. Wi-Fi jamming attacks can be difficult to detect and prevent due to their potential for wide area disruption.

## Mitigation


## Wi-Fi Jamming Risk Analysis

| **Factor**                    | **Description**                                                                      | **Value**                           |
|-------------------------------|--------------------------------------------------------------------------------------|-------------------------------------|
| Attack   Vector (AV):         | Physical   (Disrupting Wi-Fi signal and exploiting the opportunity)                  | Physical   (L)                      |
| Attack   Complexity (AC):     | Varies   (Depends on the complexity of data interception techniques after jamming)   |         Low (L) to Medium (M)       |
| Privileges   Required (PR):   | None   (Jamming and basic interception might not require privileges)                 |         None (N) to Low (L)         |
| User   Interaction (UI):      | None   (Attack doesn't require user interaction)                                     | None   (N)                          |
| Scope   (S):                  | Data   Breach (if data intercepted during jamming)                                   |         Data Breach (DB)            |
| Confidentiality   Impact (C): | High   (Intercepted data might reveal confidential user information)                 | High   (H)                          |
| Integrity   Impact (I):       | High   (Intercepted data could be modified)                                          | High   (H)                          |
| Availability   Impact (A):    | High   (Jamming disrupts communication, application functionality might be impacted) | High   (H)                          |

**Exploitation Requirements (modifies base score):**

**Confidentiality Requirement:** High (Confidentiality is severely impacted if data is intercepted)
**Integrity Requirement:** High (Integrity is severely impacted if data is intercepted)
**Availability Requirement:** High (Availability is severely impacted by jamming)

Since all confidentiality, integrity, and availability requirements are high, the base score modification factor becomes 1.0.

**Base Score:** 0.85 * (AV:L/AC:L/PR:N/UI:N) * (S:DB/C:H/I:H/A:H) * 1.0 = 7.2 (High)

**Temporal Score (TS):** | Not Applicable (N/A) | N/A |
**Environmental Score (ES):** | Depends on mobile app's security practices (data encryption in transit), user awareness (using secure Wi-Fi networks), attacker's capability (advanced interception techniques) | Varies |

**Overall CVSS Score:** | Base Score + TS + ES | Varies (Depends on TS & ES) |
**Risk Rating:** | High to Critical (Depends on ES) | High to Critical |

## Wi-Fi Jamming Attack Tree Diagram
