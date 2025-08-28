# Bluejacking Attacks

During a BlueJacking attack, the attacker sends unsolicited messages to a device to trick the user into using an access code. This enables the adversary to access files on the targeted device. The devices involved in the attack and the exact source of the message received need to be within a specific range, 10 m, for the attack to be successful. This attack is commonly used in crowded areas (e.g., airports, shopping malls, and train stations). While it does not usually involve the alteration of data, it could make devices susceptible to other attacks.
 

## Mitigation

Bluejacking is a type of cyber attack that involves sending unsolicited messages to Bluetooth-enabled devices. Here are some general strategies to mitigate Bluejacking in Cloud, Mobile, and IoT ecosystems:

1. **Turn off Bluetooth When Not in Use**: This can prevent unauthorized access to your device⁴.
2. **Use Non-Descriptive Device Names**: Using non-descriptive names for your devices can make it harder for attackers to identify them⁴.
3. **Reject Unknown Connection Requests**: Do not accept any Bluetooth connection requests that you don't recognize⁴.

For Cloud, Mobile, and IoT ecosystems specifically, consider the following:

1. **Security by Design**: Secure application development across these three technologies can only be achieved when applications and systems are designed and developed with security in mind¹. This will improve the quality of the solutions and ensure that vulnerabilities are identified¹.
2. **System Modeling**: Use system modeling to identify potential vulnerabilities and threats. This can help in the development of effective countermeasures¹.
3. **Regular Audits and Monitoring**: Regularly monitor and audit your systems to detect any unusual activities or potential security breaches.
4. **Use of Secure Cloud Services**: Use secure cloud services for IoT devices. These services provide a spectrum of capabilities, including data storage, data processing, and application hosting, which can help IoT devices collect, analyze, and share data securely².
5. **Data Encryption**: Encrypt sensitive data before storing it in the cloud or transmitting it over the network.

Remember, the key to effective mitigation is a proactive approach to security. Regularly updating security measures and staying informed about the latest threats can go a long way in protecting your systems from Bluejacking and other cyber threats.


## Bluejacking Risk Analysis

| **Factor**                  | **Description**                                            | **Value**                                                                  |
|-----------------------------|------------------------------------------------------------|----------------------------------------------------------------------------|
| Vulnerability               | Unsecured Bluetooth connections on the mobile device       | -                                                                          |
| Attack Vector (AV):         | Physical (Requires close proximity to the target device)   | Physical (L)                                                               |
| Attack Complexity (AC):     | Low ( readily available tools can be used)                 | Low (L)                                                                    |
| Privileges Required (PR):   | None (Attack doesn't require any privileges on the device) | None (N)                                                                   |
| User Interaction (UI):      | None (Attack is passive and sends unsolicited messages)    | None (N)                                                                   |
| Scope (S):                  | Nuisance (Sending unwanted messages)                       | Social Engineering (SE) (Potential gateway for social engineering attacks) |
| Confidentiality Impact (C): | None (Doesn't expose confidential data)                    | Low (Limited potential information disclosure through social engineering)  |
| Integrity Impact (I):       | None (Doesn't impact data integrity)                       | Low (Limited potential data manipulation through social engineering)       |
| Availability Impact (A):    | None (Doesn't impact application availability)             | N/A                                                                       |
| Base Score |N/A |N/A |
|Temporal Score (TS) | Low (Bluejacking is a less common attack method compared to others) | Low (L) |
|Environmental Score (ES) | Depends on Bluetooth security settings, user awareness of social engineering tactics | Varies (L to M) |
|Overall CVSS Score | Base Score + TS + ES | Varies (L to M) |
|Risk Rating: | Low (Depends on TS, ES, and potential for social engineering) | Low to Medium |

## Recommendations

In order to ensure that the mobile application is resilient or immune to the Bluejacking attack, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. Patel, N., Wimmer, H., Rebman, C.M., 2021. Investigating bluetooth vulnerabilities to defend from attacks, in: 2021 5th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT), IEEE, Ankara, Turkey. pp. 549–554. doi:10.1109/ISMSIT52890.2021.9604655.
2. Attack and System Modeling Applied to IoT, Cloud, and Mobile Ecosystems .... https://dl.acm.org/doi/fullHtml/10.1145/3376123.
3. Secure cloud-based mobile apps: attack taxonomy, requirements .... https://link.springer.com/article/10.1007/s10207-023-00669-z.
4. Securing Cloud-Based Internet of Things: Challenges and Mitigations. https://arxiv.org/pdf/2402.00356.


