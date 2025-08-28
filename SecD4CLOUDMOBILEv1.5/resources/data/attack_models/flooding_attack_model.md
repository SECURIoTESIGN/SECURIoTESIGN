# Flooding Attack 

Flooding attacks are attempts to inundate a resource with an overwhelming amount of data or requests in order to overwhelm or crash it. Flooding attacks are often effective when the target resource is limited in bandwidth or processing power, such as a server, and is unable to handle so much data or requests, resulting in performance degradation or service disruption.

Examples of flooding attacks include Denial-of-Service (DoS) attacks, which send an extremely large amount of requests/traffic to the victim’s server or network in order to saturate it and make it incapable of responding to legitimate requests. Additionally, there is also the Distributed Denial-of-Service (DDoS) attack, which uses more than one computer or device to send the traffic, making it even more of a challenge to defend against.

## Mitigation

Flooding attacks can be difficult to detect and stop as they often involve huge volumes of data. However, some steps to help mitigate the effects of flooding attacks include:

1. Rate Limiting: Implement rate limiting on your servers to prevent any single IP address from sending too many requests in a short period of time;
2. Traffic Shaping: Use traffic shaping techniques to control the amount and speed of traffic sent or received on a network.
3. Intrusion Detection Systems (IDS): Use IDS to monitor network traffic for suspicious activity and known threats;
4. Firewalls: Use firewalls to block unwanted traffic and prevent flooding attacks;
5. Load Balancing: Distribute network traffic across multiple servers to ensure no single server is overwhelmed with too much traffic;
6. DDoS Protection Services: Consider using a DDoS protection service that can detect and block flooding attacks;
7. Redundancy: Design your system to be redundant so that if one part of the system becomes overwhelmed with traffic, the system as a whole can still function;
8. Regular Monitoring and Logging: Regularly monitor and log traffic to identify patterns and detect potential flooding attacks;
9. Incident Response Plan: Have an incident response plan in place to quickly and effectively handle flooding attacks when they occur;
10. User Awareness and Training: Educate users about the risks of flooding attacks and how to report suspicious activity.

## Flooding Architectural Risk Analysis 

| **Factor**                    | **Description**                                                                                                 | **Value**                                         |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Attack   Vector (AV):         | Network   (Exploiting application logic)                                                                        | Network   (N)                                     |
| Attack   Complexity (AC):     | Low   (Requires crafting malicious requests)                                                                    | Low   (L)                                         |
| Privileges   Required (PR):   | None                                                                                                            | None   (N)                                        |
| User   Interaction (UI):      | None   (after initial attack setup)                                                                             | None   (N)                                        |
| Scope   (S):                  | Denial   of Service (attacker disrupts application functionality for legitimate users)                          |         Denial of service (DoS)                   |
| Confidentiality   Impact (C): | Low                                                                                                            | None   (N)                                        |
| Integrity   Impact (I):       | Low   (unless flooding crashes the app and corrupts data)                                                       | Low   (L)                                         |
| Availability   Impact (A):    | High   (attacker can disrupt app functionality for legitimate users)                                            | High   (H)                                        |
| Base   Score:                 | 0.85   * (AV:N/AC:L/PR:N/UI:N) * (S:DoS/C:N/I:L/A:H)                                                            | 9.9   (Critical)                                    |
| Overall   CVSS Score          | Base   Score + TS + ES                                                                                          |         Varies (Depends on TS & ES)               |
| Risk   Rating                 | Based   on Overall CVSS Score                                                                                   |         High to Critical (Depends on TS & ES)       |

**CVSS v3.1 Risk Rating:** Critical (Official Fix)

## Flooding Attack Tree Diagram