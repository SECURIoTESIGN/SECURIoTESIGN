# Cache Poisoning Attacks

In this type of attack the attacker uses DNS to convert the domain name to an IP address for the purpose of accessing the user's confidential data. On the other hand, sender and a receiver get rerouted through some evil connection.

## Definition

Cache poisoning is the act of introducing false information into a Domain Name System (DNS) cache in order to cause DNS queries to return an incorrect response and, e.g., redirect users to malicious websites. This type of attack can target the cache of an application (e.g., a web browser cache) or a public cache (e.g. a DNS or Address Resolution Protocol (ARP) cache), exposing the application to a variety of attacks, such as redirection to malicious websites and malware injection.

## Technical Impact
  * Gain Privileges or Assume Identity; 
  * Bypass Protection Mechanism.

## Risk
  * Medium.

## Likelihood of Exploit
  * Low.
  
## Attacker Powers
  * Access confidential information from legitimate/authorized users;
  * Perpetrate other types of attacks like DDoS and Main-in-the-Middle.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the DNS attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed.

## Reference
  1. [https://cwe.mitre.org/data/definitions/350.html];
  2. [https://capec.mitre.org/data/definitions/141.html].

## Cache Poisoning Attacks Diagram


