# Cross VM Attacks (Sid-Channel attacks)

Side-channel attacks are used to extract cryptographic keys from a victim device or process in a virtualized layer of the cloud ecosystem where a Cross-VM attack exploits the nature of multi-tenancy, which enables that VMs belonging to different customers may co-reside on the same physical machine.


## Definition

The side-channel attack takes advantage of low-bandwidth message channels in a system to leak sensitive security information. There is no doubt that this type of attack exists and is real for today's computer systems, including modern smartphones and tablets. Here we highlight the cache-based side-channel attacks that have been used to steal cryptographic information from a single OS. Furthermore, the weak link is in the fact that cryptographic algorithms usually have data-dependent memory access patterns, giving the possibility of being revealed by the observation and statistical analysis of hits / errors from the associated cache. Recent research has shown attackers can build up cross-VM side channels to obtain sensitive information. However, currently these channels are mostly based on shared CPU cache, networks, CPU loads and so on. These attacks are generally categorized into one of three classes:

 * Time-driven side-channel attack;
 * Trace-driven side-channel attacks;
 * Access-driven side-channel attacks.

## Technical Impact
* Modify and Read Memory; 
* Read Files or Directories; 
* Modify Files or Directories; 
* Execute Unauthorized Code or Commands; 
* Gain Privileges or Assume Identity; 
* Bypass Protection Mechanism; 
* Read Application Data; 
* Modify Application Data; 
* Hide Activities.

## Risk Analysis
  * High Risk.

## Likelihood of Exploit
  * Low.


## Attacker Powers

 * Steal cryptographic information;
 * Extract cryptographic key;
 * Obtains confidential data or sensitive information.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the side-channel attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## Cross VM Attacks Diagram


