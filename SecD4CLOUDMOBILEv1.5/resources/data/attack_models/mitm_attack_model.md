# Man-in-th-Middle Attack 

Man-in-the-Middle (MITM) attack is an attack where a threat actor interferes with the communication between two systems. The threat actor inserts itself between the two systems and has access to all the data being sent between them.

MITM attacks are used to steal or modify data in transit, such as banking credentials, passwords, and security tokens. Hackers carry out these attacks by spoofing IP addresses and using malicious code to gain access to unencrypted data. They can also use packet-sniffing software to eavesdrop on the connection.

MITM attacks can be done through network-level attacks or application-level attacks. Network-level MITM attacks involve the hacker taking control of the entire communications path between the two hosts. Application level MITM attacks involve the hacker hacking into one of the hosts and manipulating their traffic.

## Mitigation

1. **Use of HTTPS:** Always use HTTPS for all communications. HTTPS encrypts the data between the client and the server, making it difficult for a MitM attacker to read or modify the data.
2. **Certificate Pinning:** Implement certificate pinning in your mobile applications. This involves hard coding the server’s certificate or public key within the application. The app can then verify the server’s identity by comparing the server’s certificate with the pinned certificate.
3. **VPN:** Encourage users to use a Virtual Private Network (VPN) when connecting to your services, especially when they are using public Wi-Fi networks.
4. **Two-Factor Authentication (2FA):** Implement 2FA to add an extra layer of security. Even if an attacker manages to intercept the user’s credentials, they would still need the second factor to gain access.
5. **Regular Updates and Patches:** Keep your systems and software up-to-date. Regular updates and patches can fix known vulnerabilities that could be exploited by MitM attacks.
6. **User Awareness:** Educate users about the risks of MitM attacks and how to identify potential threats. This includes training on how to recognize phishing attempts, unsafe websites, and malicious email attachments.

## Man-in-th-Middle Architectural Risk Analysis

| **Factor**                                    | **Description**                                                                                                 | **Value**                                     |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Attack   Vector (AV):                         | Network   (Exploiting unencrypted communication)                                                                | Network   (N)                                 |
| Attack   Complexity (AC):                     | Medium   (Requires setting up a MitM attack)                                                                    | Medium   (M)                                  |
| Privileges   Required (PR):                   | None   (Attacker needs to intercept communication)                                                              | None   (N)                                    |
| User   Interaction (UI):                      | None   (User doesn't need to interact with the attack)                                                          | None   (N)                                    |
| Scope   (S):                                  | Varies   (Depends on intercepted data)                                                                          | Intercept   (I)                               |
| Confidentiality   Impact (C):                 | High   (attacker can steal confidential data)                                                                   | High   (H)                                    |
| Integrity   Impact (I):                       | High   (attacker can modify data in transit)                                                                    | High   (H)                                    |
| Availability   Impact (A):                    | Medium   (attacker can potentially disrupt communication)                                                       | Medium   (M)                                  |
| Base   Score (assuming High for all impacts): | 0.85   * (AV:N/AC:M/PR:N/UI:N) * (S:I/C:H/I:H/A:M)                                                              | 8.5   (High)                                  |
| Temporal   Score (TS):                        | Public   exploit tools available for MitM attacks?                                                              |         Depends on exploit availability       |
| Environmental   Score (ES):                   | Depends   on application's security practices (encryption), network security measures   (HTTPS), user awareness | Varies                                        |

**Overall, a Man-in-the-Middle attack poses a significant risk to mobile cloud-based applications that hold user confidential data. Implementing strong encryption (HTTPS) for communication and educating users about secure network practices can mitigate this risk.**

## MiTM Attack Tree Diagram