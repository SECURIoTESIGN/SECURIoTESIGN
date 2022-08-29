# Authenticity

Is the assurance that information transaction is from the source it claims to be from. The device authenticates itself prior to receiving or transmitting any information. It assures that the information received is authentic. It is assumed that communications may be intercepted by an unauthorized entity and data at rest may be subject to unauthorized access during transport and rest, taking into account the nature of the cloud and mobile ecosystem. 

**Note:** *This security requirement is applied across all layers of the ecosystem under consideration, i.e., communication, transport and storage of information shared or exchanged between authorized entities.*

### Security Verification Requirements

 * If the app provides users access to a remote service, some form of authentication, such as username/password authentication, is perfumed at the remote endpoint;
 * if stateful session management is used, the remote andpoint uses rendomly generated session identifiers to authenticate client requests without sending the user's crendentials;
 * If stateless token-base authentication is used, the server provides a token that has been signed using a secure algorithm;
 * The remote endpoint terminates the existing session when the user logs out;
 * A password policy exists and is enforcer at the remote endpoint;
 * The remote endpoint implements a mechanism to protect against the submission of credentials an excessive number of times;
 * Sessions are invalidated at the remote endpoint after a predefined period of inactivity and access number of times;
 * Biometric authentication, if any, is not event-bound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore;
 * A second factor of authentication exists at the remote endpoint and the 2FA requirements is consistently enforced;
 * Sensitive transactions require set-up authentication;
 * The app informas the user of all login activities with their account. Users are able view a list of devices used to access the account, and to block specific devices.

Not addressing this requirement may lead to vulnerabilities explored by attacks such as:                                                                

### 1. Botnets Attack

A botnet is a collection of compromised devices that can be remotely controlled by an attacker, i.e. the bot master. Its main purpose is to steal business information, remote access, online fraud, phishing, malware distribution, spam emails, etc.                                      

### 2. Phishing

In this type of attack scenario, an attacker can perform a phishing attack by manipulating a web link to attempt to redirect users to a false one and capture user information and account access, with the final objective of stealing sensitive data. Main attacks vectors are e-mail keyloggers through trojan horses and Man-in-the-Middle Attack of data proxies.

### 3. DNS Attack
                                        
DNS attacks always occur in the case where the attacker makes use of the translation of the domain name in an Internet Protocol (IP) address, in order to access the confidential data of the user in an unauthorized way 

### 4. MITM Attack 

In this type of attack, an attacker attempts to intrude on a mail exchange or continuous message between two users or clients of a cloud-based mobile application (client-server).                                                     

### 5. Reused IP Address Attack:

This type of attack occurs whenever a IP address is reused on a network. This occurs because in a network the number of IP addresses is usually limited, which causes an address assigned to one user to be assigned to another, so that it leaves the network.                               

### 6. Wrapping Attacks

In a wrapping attack scenario, the attacker duplicates the SOAP message in the course of the translation and sends it to the server as a legitimate user. Therefore, the attacker may interfere with the malicious code.

### 7. Cookie Poisoning Attack 
                            
This type of attack consists of replacing or modifying cookie content in ways to gain unauthorized access to applications or Web pages.
 
### 8. Google Hacking Attacks 
                                      
This type of attack involves the use of the Google search engine for the purpose of discovering confidential information that a hacker or wrongdoer can use for their benefit by hacking the account of a used.
                
### 9. VM Escape

This type of attack occurs whenever an application escapes the VM and obtains control over the VMM, as it escalates its VM privileges to root level. The malicious application accesses the host machine, bypassing the hypervisor. 

### 10. Session Fixation

The aim of this attack is account hijacking, with the aim of fraudulently accessing the area restricted to legitimate users of a web app or a hybrid mobile app. The success of this attack depends on prior login, as it requires the session ID of a legitimate user of the target application, impersonating the victim, which grants privileges and results in the violation of confidentiality, access control and authorisation of sensitive user data, and theft of money from mobile banking app or mobile interbank application.     

### 11. Brute Force 
The attacker attempts to gain access to systems' asset (information, functionality, identity, etc.) protected by a finite secret value by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or a value that is functionally equivalent) that will unlock the asset.

### 12. Buffer Overflow
                                                          
Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.

### 13. Spoofing

Spoofing attacks are a fraudulent act in which an entity fakes its identity to attempt to access resources and critical data. There are four variants of the spoofing attack, namely, content spoofing, identity spoofing, resource location spoofing and action spoofing.

### 14. Cache Poisoning

This type of attack has to do with any attack whereby an attacker caches incorrect or harmful material. The cache targeted can be an application's cache (e.g., a web browser cache) or a public cache (fe.g., a DNS or ARP cache).

### 15. Reverse Engineering

Reverse engineering attacks target the assets embedded in software. In such an attack scenario, the attacker by reverse engineering attempts to steal confidential information, such as embedded cryptographic keys or intellectual property in the form of algorithms.

### 15. NFC Payment replay attacks 

This type of attack targets the exploitation of vulnerabilities in the European Visa and Mastercad (EMV) wireless communication protocol between the smartcard and the payment terminal, namely, the authenticity of the payment terminal is not guaranteed to the customer's payment device and the banking data exchanged between the customer's payment device (smartcard) and the point of sale terminal are not encrypted and are transferred in clear text.

### 16. Bypassing Physical Security 

This type of attack aims to circumvent or avoid detection by physical security and building surveillance systems and use methods to bypass electronic or physical locks protecting entry points. It also results in other types of attacks aimed at accessing, altering or destroying sensitive user information or making a service or resource unavailable. 

### 17. Physical Theft 

This type of attack aims to access and steal the target user's device in order to perform a malicious action, such as altering, deleting, leaking, inserting and destroying data, as well as stealing money through banking transactions, posing as the rightful owner. The attacker can simply destroy the device, preventing the user from accessing their data and the services provided in the form of an application as a service.

### 18. On-Off Attacks 

This type of attack targets a wireless sensor network, aiming to disrupt a trust redemption scheme, behaving alternately good and bad, in order to ensure immediate trust redemption before another attack occurs. On the other hand, this occurs because there is a security vulnerability that has to do with the fact that not all trust redemption schemes are able to effectively discriminate an On-Off attack and temporary errors, especially when it is good most of the attacker's behaviour, making him able to remain active in the system, as he has the ability to disguise attacks as temporary errors.

### 19. Mobile SIM Swapping

This attack targets the SIM card of a smartphone user, i.e. swapping the victim user's SIM card. SIM swapping can happen remotely. A cybercriminal, with a few important details about your life in hand, can answer security questions correctly, impersonate you, and convince your mobile carrier to reassign your phone number to a new SIM card. At that point, the criminal can get access to your phone’s data and start changing your account passwords to lock you out of your online banking profile, email, and more. 

## References

 * In general - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md;
 * For Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md;
 * For iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md;
 * CAPEC - https://capec.mitre.org/data/definitions/141.html.