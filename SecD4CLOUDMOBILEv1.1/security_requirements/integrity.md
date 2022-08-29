# Integrity 

Is the property of safeguarding the correctness and completeness of assets in a Cloud & Mobile system. In other words it involves maintaining the data consistent, trustworthy and accurate during it life-cycle.

**Note:** *This requirements is applied in the Cloud and Mobile Ecosystem.*

Not addressing this requirement may lead to vulnerabilities explored by attacks such as:                                                        

### 1. SQL Injection Attacks:                                          
In this type of attack, the attacker inserts malicious code with the intention of accessing the unauthorized database for the purpose of obtaining confidential or critical data from the legitimate user.

### 2. Wrapping Attacks:                                                       
In a wrapping attack scenario, the attacker duplicates the SOAP message in the course of the translation and sends it to the server as a legitimate user. Therefore, the attacker may interfere with the malicious code.

### 3. MITM Attacks:                                                             
In this type of attack, an attacker attempts to intrude on a mail exchange or continuous message between two users or clients of a cloud-based mobile application (client-server).

### 4. Cookie Poisoning:                                                     
This type of attack consists of replacing or modifying cookie content in ways to gain unauthorized access to applications or Web pages. 

### 5. Session Hijacking
This type of attack involves an adversary exploiting weaknesses in the use of an application's authentication sessions. Put another way, this type of attack results from the successful exploitation of improper authentication. Its main purpose is account hijacking. The attacker may be able to steal or manipulate an active session and use it to gain unauthorised access to the application.

### 6. Cross Site Request Forgery 
Cross-site Request Forgery (CSRF) is an attack that forces the user to execute unintended actions in an application for which it is already authenticated in a given moment. These attacks target unrequested status changes, and not directly data theft, as the attacker cannot see the answer to the forged request.

### 7. Server Side Request Forgery

We are in the presence of a Server Side Request Forgery Attack (SSRF) as long as the web application is vulnerable and redirects the attacker's requests to the internal network and exposes local services to the remote attacker, which introduces different forms of risks.

### 8. Buffer Overflow
                                                          
Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.

### 9. Spoofing

Spoofing attacks are a fraudulent act in which an entity fakes its identity to attempt to access resources and critical data. There are four variants of the spoofing attack, namely, content spoofing, identity spoofing, resource location spoofing and action spoofing.

### 10. Audit Log Manipulation Attacks (ALM) 

This type of attack targets log files for the purpose of manipulating (deleting, reading, and altering) them.

### 11. Code Inclusion

In this type of attack, an attacker exploits a weakness in the target in order to force arbitrary code to be retrieved locally or from a remote location and executed.

### 12. Malware-as-a-Service 

Malicious code, or simply malware, are scripts or programs that can be injected in the Cloud and Mobile ecosystem. Malware are traditionally mainly classified based on two main factors: propagation strategy (e.g., virus or worm) and malicious activity (trojan horse, spyware, adware, rootkits, botnets, ransomware, backdoors and key-loggers).

### 13. Code Injection

This type of attack targets injecting malicious code into user inputs from the interface (web application forms or hybrid mobile applications) of applications written in HTML5.

### 14. Command Injection Attacks

This is a class of attacks to which web applications are susceptible, resulting from the semantic gap existing between database interpretation and web application interpretation, as well as from the inappropriate handling of user input

### 15. Reverse Engineering

Reverse engineering attacks target the assets embedded in software. In such an attack scenario, the attacker by reverse engineering attempts to steal confidential information, such as embedded cryptographic keys or intellectual property in the form of algorithms.

### 16. Access Point hijacking 

This type of attack is a variant of the session hijacking attack and targets the AP access credentials of legitimate administrators. These credentials can be extracted through a sniffing, brute force or MiTM attack. After this, the attacker is able to carry out other types of attacks, such as DoS and Rogue Access Points.

### 17. Phishing

In this type of attack scenario, an attacker can perform a phishing attack by manipulating a web link to attempt to redirect users to a false one and capture user information and account access, with the final objective of stealing sensitive data. Main attacks vectors are e-mail keyloggers through trojan horses and Man-in-the-Middle Attack of data proxies.

### 18. Malicious QR Code 

Although this type of attack also affects the category or application layer, it also falls under the category of Social Engineering attacks as it mainly relies on human behaviour and its vulnerabilities. For example, the victim may be tricked into reading a malicious QR code advertising a fake promotional campaign for a product from a supermarket car park.

### 19. Malicious Insider 

This type of attack occurs when there a malicious entity (client, employee, hypervisor, Cloud provider/corrector, etc.) takes advantage of its privileges to secretly realize a malicious activity, such as information theft and data or physical infrastructure destruction. This type of attack also occurs from client to server, when the person, employee or team with insider knowledge on how the system is built can implant malicious code to fully destroy the Cloud solution.

### 20. On-Off Attacks 

This type of attack targets a wireless sensor network, aiming to disrupt a trust redemption scheme, behaving alternately good and bad, in order to ensure immediate trust redemption before another attack occurs. On the other hand, this occurs because there is a security vulnerability that has to do with the fact that not all trust redemption schemes are able to effectively discriminate an On-Off attack and temporary errors, especially when it is good most of the attacker's behaviour, making him able to remain active in the system, as he has the ability to disguise attacks as temporary errors.

### 21. Mobile SIM Swapping

This attack targets the SIM card of a smartphone user, i.e. swapping the victim user's SIM card. SIM swapping can happen remotely. A cybercriminal, with a few important details about your life in hand, can answer security questions correctly, impersonate you, and convince your mobile carrier to reassign your phone number to a new SIM card. At that point, the criminal can get access to your phone’s data and start changing your account passwords to lock you out of your online banking profile, email, and more. 