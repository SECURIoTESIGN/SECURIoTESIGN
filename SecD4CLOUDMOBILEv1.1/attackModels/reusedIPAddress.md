# Reused IP Address Attacks

IP address is reassigned and reused by other customer. The address still exists in the DNS cache, it violating the privacy of the original user.

## Definition

Each node of a network has an IP address which is allocated to a particular user when that user leaves the network, the IP address associated with him is assigned to a new user. The chances of accessing previous user data by the new user exist as the address still exist in DNS cache and hence the data belonging to one person can be accessed by another.

## Technical Impact
  * Bypass Protection Mechanism; 
  * Gain Privileges or Assume Identity.

## Risk Analysis
  * Critical Risk.

## Likelihood of Exploit
  * High.
  
## Attacker Powers

 * Access confidential information from legitimate/authorized users.


## Recommendations

To ensure that the mobile application is resilient or immune to malicious Reused IP Address attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed to ensure authenticity, integrity, privacy and authenticity of the data.

 
## Reused IP Address Attacks Diagram


