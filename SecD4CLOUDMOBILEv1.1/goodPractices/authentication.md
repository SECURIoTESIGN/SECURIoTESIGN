# Authentication

Is the assurance that information transaction is from the source it claims to be from. The device authenticates itself prior to receiving or transmitting any information. It assures that the information received is authentic. It is assumed that communications may be intercepted by an unauthorized entity and data at rest may be subject to unauthorized access during transport and rest, taking into account the nature of the cloud and mobile ecosystem. 

This security requirement is applied across all layers of the ecosystem under consideration, i.e., communication, transport and storage of information shared or exchanged between authorized entities.

## Security Verification Requirements
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

## Botnet Attack
A botnet is a collection of compromised devices that can be remotely controlled by an attacker, i.e. the bot master. Its main purpose is to steal business information, remote access, online fraud, phishing, malware distribution, spam emails, etc.                                      

## Phishing Attack 
In a scenario of this type of attack, when using cloud services, an attacker can conduct phishing attacks by manipulating the web link to redirect it to a false link and hijack the user account for the purpose of stealing the your sensitive data.                                     

## DNS Attack                                        
DNS attacks always occur in the case where the attacker makes use of the translation of the domain name in an Internet Protocol (IP) address, in order to access the confidential data of the user in an unauthorized way 

## MITM Attack 
In this type of attack, an attacker attempts to intrude on a mail exchange or continuous message between two users or clients of a cloud-based mobile application (client-server).                                                     

## Reused IP Address Attack:
This type of attack occurs whenever a IP address is reused on a network. This occurs because in a network the number of IP addresses is usually limited, which causes an address assigned to one user to be assigned to another, so that it leaves the network.                               

## Wrapping Attacks
In a wrapping attack scenario, the attacker duplicates the SOAP message in the course of the translation and sends it to the server as a legitimate user. Therefore, the attacker may interfere with the malicious code.

## Cookie Poisoning Attack                             
This type of attack consists of replacing or modifying cookie content in ways to gain unauthorized access to applications or Web pages.
 
## Google Hacking Attacks                                       
This type of attack involves the use of the Google search engine for the purpose of discovering confidential information that a hacker or wrongdoer can use for their benefit by hacking the account of a used.
                
## Hypervisor Attacks:  
In this type of attack the attacker aims to compromise the authenticity of sensitive user data and the availability of services from the cloud at the VM level.                                          

### References

 * In general - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md;
 * For Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md;
 * For iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md.