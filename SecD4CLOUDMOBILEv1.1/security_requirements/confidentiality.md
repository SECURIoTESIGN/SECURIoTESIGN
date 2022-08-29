# Confidentiality

The property that ensures that information is not disclosed or made available to any unauthorized entity. In other words, information cannot be accessed by an unauthorized third party.

**Note** *This requirement is applied were the information is stored*.

Failure to guarantee this security requirement can lead to the leakage or loss of confidential data shared among authorized users of the application e a aplicação poderá estar sujeita aos seguintes ataques:

### 1. Brute Force 
The attacker attempts to gain access to systems' asset (information, functionality, identity, etc.) protected by a finite secret value by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or a value that is functionally equivalent) that will unlock the asset.

### 2. Eavesdropping
Eavesdropping is a type of attack where the attacker tries to gain access to sensitive information of legitimate users from the messages (text, voice and video) exchanged between two or more users of Instant Messaging (IM) applications. The same applies to recorded calls, call logs and multimedia stored in clear text on memory cards.

### 3. Session Hijacking
This type of attack involves an adversary exploiting weaknesses in the use of an application's authentication sessions. Put another way, this type of attack results from the successful exploitation of improper authentication. Its main purpose is account hijacking. The attacker may be able to steal or manipulate an active session and use it to gain unauthorised access to the application.

### 4. Session Fixation 
The aim of this attack is account hijacking, with the aim of fraudulently accessing the area restricted to legitimate users of a web app or a hybrid mobile app. The success of this attack depends on prior login, as it requires the session ID of a legitimate user of the target application, impersonating the victim, which grants privileges and results in the violation of confidentiality, access control and authorisation of sensitive user data, and theft of money from mobile banking app or mobile interbank application.

### 5. Cross Site Request Forgery 
Cross-site Request Forgery (CSRF) is an attack that forces the user to execute unintended actions in an application for which it is already authenticated in a given moment. These attacks target unrequested status changes, and not directly data theft, as the attacker cannot see the answer to the forged request.

### 6. MITM Attacks:                                                             
In this type of attack, an attacker attempts to intrude on a mail exchange or continuous message between two users or clients of a cloud-based mobile application (client-server).

### 7. Server Side Request Forgery

We are in the presence of a Server Side Request Forgery Attack (SSRF) as long as the web application is vulnerable and redirects the attacker's requests to the internal network and exposes local services to the remote attacker, which introduces different forms of risks.

### 8. Sniffing Attacks

Sniffing is the act of obtaining data in real time from data transmitted between smartphones (or tablets) and with the Cloud, through a network (Bluetooth, Wireless Sensor Network (WSN), Wi-Fi, 3G/4G/5G, etc.)

### 9. Buffer Overflow
                                                          
Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.

### 10. Spoofing

Spoofing attacks are a fraudulent act in which an entity fakes its identity to attempt to access resources and critical data. There are four variants of the spoofing attack, namely, content spoofing, identity spoofing, resource location spoofing and action spoofing.

### 11. Code Inclusion 

Unlike code injection, in this type of attack, an attacker exploits a weakness in the target in order to force arbitrary code to be retrieved locally or from a remote location and executed.

### 12. Malware-as-a-Service 

Malicious code, or simply malware, are scripts or programs that can be injected in the Cloud and Mobile ecosystem. Malware are traditionally mainly classified based on two main factors: propagation strategy (e.g., virus or worm) and malicious activity (trojan horse, spyware, adware, rootkits, botnets, ransomware, backdoors and key-loggers).

### 13. Code Injection

This type of attack targets injecting malicious code into user inputs from the interface (web application forms or hybrid mobile applications) of applications written in HTML5.

### 14. Command Injection Attacks

This is a class of attacks to which web applications are susceptible, resulting from the semantic gap existing between database interpretation and web application interpretation, as well as from the inappropriate handling of user input.

### 15. SQL Injection Attack

In  this  attack  the  perpetrator injects  malicious command in the system to gain access to information or even to gain control of the entire system. 

### 16. Reverse Engineering

Reverse engineering attacks target the assets embedded in software. In such an attack scenario, the attacker by reverse engineering attempts to steal confidential information, such as embedded cryptographic keys or intellectual property in the form of algorithms.

### 17. Cryptanalysis

Cryptanalysis focuses on finding vulnerabilities in cryptographic algorithms and using these weaknesses to decrypt the ciphertext without knowing the secret key.

### 18. Cellular Rogue Base Station Attacks 

Cellular Rogue Base Station is a security threat targeting a mobile phone network that can exploit the radio interface between smartphones and base stations, potentially launching passive or active attacks against user equipment. Such attacks range from acquiring the International Mobile Subscriber Identifier (IMSI) of subscribers, DoS, leaking private information on 4G networks and eavesdropping.

### 19. Rogue Access Points 

The Access Points (AP) in a Wi-Fi networks are subject to the attack of access point spoofing, usually called Rogue Access Point (RAP). This attack consists of cloning the Media Access Control (MAC) address and Service Set IDentifier (SSID) of an AP, giving rise to the emergence of a fake access point posing as a genuine one, leading users to connect to this new network as if they were connecting to the genuine network. After connection, an attack is able to eavesdrops on its communication to hijack client's communication, re-direct clients to malicious websites, steal credentials (session hijacking) of the clients connecting to it.

### 20. GPS Spoofing Attacks 

GPS has grown to such an extent that today it is considered a ubiquitous technology that provides positioning, navigation and timing services (PNT). As an essential element of the global information infrastructure, GPS cybersecurity faces serious challenge issues. Although some mission-critical systems even rely on GPS as a security measure, GPS in civilian version has no protection against malicious acts such as spoofing. According, "GPS spoofing breaches authentication by forging satellite signals to mislead users with wrong location/timing data that threatens homeland security".

### 21. Access Point hijacking 

This type of attack is a variant of the session hijacking attack and targets the AP access credentials of legitimate administrators. These credentials can be extracted through a sniffing, brute force or MiTM attack. After this, the attacker is able to carry out other types of attacks, such as DoS and Rogue Access Points.

### 22. NFC Payment replay attacks 

This type of attack targets the exploitation of vulnerabilities in the European Visa and Mastercad (EMV) wireless communication protocol between the smartcard and the payment terminal, namely, the authenticity of the payment terminal is not guaranteed to the customer's payment device and the banking data exchanged between the customer's payment device (smartcard) and the point of sale terminal are not encrypted and are transferred in clear text.

### 23. Wi-Fi SSID Tracking Attacks 

This type of attack aims to obtain sensitive data (location, routine, trajectory, etc.) of users of mobile devices using Wi-Fi networks to access the Internet. Furthermore, it consists of using sophisticated sniffing devices to bypass authentication (for closed networks), extract and identify the MAC address of the mobile device and establish a match with its potential owner.

### 24. Phishing Attacks 

In this type of attack scenario, an attacker can perform a phishing attack by manipulating a web link to attempt to redirect users to a false one and capture user information and account access, with the final objective of stealing sensitive data. Main attacks vectors are e-mail keyloggers through trojan horses and Man-in-the-Middle Attack of data proxies.

### 25. Pharming Attacks 

Pharming is a special type of phishing attack or DNS poisoning attack in which the user is redirected to a fake website by changing the IP address on the DNS server. The target of the attack is the same as the phishing attack, i.e. theft of sensitive data and money from legitimate users of the applications.

### 26. Malicious QR Code 

Although this type of attack also affects the category or application layer, it also falls under the category of Social Engineering attacks as it mainly relies on human behaviour and its vulnerabilities. For example, the victim may be tricked into reading a malicious QR code advertising a fake promotional campaign for a product from a supermarket car park.

### 27. On-Off Attacks 

This type of attack targets a wireless sensor network, aiming to disrupt a trust redemption scheme, behaving alternately good and bad, in order to ensure immediate trust redemption before another attack occurs. On the other hand, this occurs because there is a security vulnerability that has to do with the fact that not all trust redemption schemes are able to effectively discriminate an On-Off attack and temporary errors, especially when it is good most of the attacker's behaviour, making him able to remain active in the system, as he has the ability to disguise attacks as temporary errors.

### 28. Mobile SIM Swapping

This attack targets the SIM card of a smartphone user, i.e. swapping the victim user's SIM card. SIM swapping can happen remotely. A cybercriminal, with a few important details about your life in hand, can answer security questions correctly, impersonate you, and convince your mobile carrier to reassign your phone number to a new SIM card. At that point, the criminal can get access to your phone’s data and start changing your account passwords to lock you out of your online banking profile, email, and more. 

## References
1. [https://capec.mitre.org/data/definitions/651.html];
2. [https://capec.mitre.org/data/definitions/112.html].
