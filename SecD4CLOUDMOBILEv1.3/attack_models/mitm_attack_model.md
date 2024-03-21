# Man-in-th-Middle Attack 

Man-in-the-Middle (MITM) attack is an attack where a threat actor interferes with the communication between two systems. The threat actor inserts itself between the two systems and has access to all the data being sent between them.

MITM attacks are used to steal or modify data in transit, such as banking credentials, passwords, and security tokens. Hackers carry out these attacks by spoofing IP addresses and using malicious code to gain access to unencrypted data. They can also use packet-sniffing software to eavesdrop on the connection.

MITM attacks can be done through network-level attacks or application-level attacks. Network-level MITM attacks involve the hacker taking control of the entire communications path between the two hosts. Application level MITM attacks involve the hacker hacking into one of the hosts and manipulating their traffic.

To protect against MITM attacks, it is important to use secure protocols such as HTTPS and SSL/TLS. It is also important to ensure that sensitive data is encrypted while in transit. Additionally, strong authentication methods should be used to authenticate users and prevent unauthorized access.

## Man-in-th-Middle Architectural Risk Analysis: 

### Overview
Man-in-the-Middle (MITM) vulnerabilities occur when an attacker is able to intercept and modify data sent between two parties. This attack is especially dangerous as it can be used to intercept sensitive and confidential information. 
 
### Risk Factors
The Common Vulnerability Scoring System (CVSS) version 3.1 measures the risk of a Man-in-the-Middle (MITM) attack along four different vectors:

1. **Attack vector (AV)** : Remote
2. **Attack complexity (AC)**: Low
3. **Privileges required (PR)**: None
4. **User Interaction (UI)**: None


### Risk Score
Based on the risk factors defined above, the risk score for a Man-in-the-Middle attack using CVSS v3.1 is 7.2. This falls under the medium risk category. 

**Overall Risk Score: 7.2 (Medium)**

## MiTM Attack Tree