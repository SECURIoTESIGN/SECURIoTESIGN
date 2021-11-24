# Domain Name Server Attacks

In this type of attack the attacker uses DNS to convert the domain name to an IP address for the purpose of accessing the user's confidential data. On the other hand, sender and a receiver get rerouted through some evil connection.

## Definition

In DNS reflection attacks, attackers send DNS requests toward multiple open DNS servers with spoofed source address of the target, which results in a large number of DNS responses to the target from DNS servers. Since the cloud has its own DNS servers to answer DNS queries from hosted tenants, there should not be any DNS responses from the Internet to the cloud. Therefore, any activity of inbound DNS responses may signify a potential DNS reflection attack. Inbound DNS reflection attacks often come from up to 6K distinct sources (with 1500 byte full-size packets). We only observed outbound DNS responses from a single VIP hosting a DNS server at 5666 packets per second for a couple of days repeatedly.

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
  1. [https://cwe.mitre.org/data/definitions/350.html]

## DNS Attacks Diagram


