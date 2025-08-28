# Man-in-the-Middle Attack

In this type of attack an active man listen and change communications between Mobile Device and Cloud. In other hand, in this attack an intruder enters in the ongoing conversation between sender and the receiver and makes them believe that conversation is taking place between them only.


## Definition

This type of attack occurs whenever an attacker intends to intercept communications in order to interpret or alter the original data in transit between the sender and the receiver establishing a conversation.

## Technical Impact

 * An attacker is able to decrypt and read all SSL/TLS traffic between the client and server;
 * Gain Privileges or Assume Identity.

## Risk Analysis
 * Critical Risk.

## Likelihood of Exploit
 * Medium.

## Attacker Powers

The attacker generally and depending on whether the communication situation is encrypted or not, is able to modify the cryptographically unprotected communication or modify the cryptographically protected communication. More specifically, it will have the following powers:

 * Steal encryption key;
 * Discover cryptographic key using cryptanalysis;
 * Exploit vulnerabilities in cryptographic algorithm;
 * Exploit vulnerabilities in cryptographic protocol.

## Recommendations
To ensure that the mobile application is resilient or immune to malicious MitM attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed to ensure authenticity, integrity, privacy and authenticity of the data.

## Reference
 1. [https://cwe.mitre.org/data/definitions/300.html];
 2. [https://www.first.org/cvss/v3.1/examples].
 
## Man-in-the-Middle Attack Diagram


