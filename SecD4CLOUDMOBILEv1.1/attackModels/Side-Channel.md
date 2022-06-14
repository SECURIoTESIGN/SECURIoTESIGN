# Side-Channel Attacks

It is a type of attack enabled by leakage of information from a physical cryptosystem.


## Definition

Side-channel attacks use statistical models such as differential analysis and correlation analysis on the information leaked from the cryptographic device during runtime. While early attacks required attackers to be in physical possession of the device, newer side-channel attacks such as cache-timing attacks or DRAM row buffer attacks are conducted remotely by executing malicious software in the targeted cloud environment. Regarding smartphones/tablets, they have developed more sophisticated side-channel attacks that target the built-in sensors of these devices, allowing them to infer keyboard input on touchscreens through sensor readings of native applications and websites, infer a user's location by the power consumption available in the proc file system (procfs), and infer a user's identity, location and diseases through procfs.

 * Time-driven side-channel attack;
 * Trace-driven side-channel attacks;
 * Access-driven side-channel attacks.
 * Power Analysis;
 * Electromagnetic Analysis;
 * Laser/optical;
 * Clock/power Glitch;
 * Temperature Variation;
 * EMFI;
 * Differential Computation Analysis
 * Reflection/hands;
 * Smudges;
 * Network Traffic Analysis;
 * USB Power Analysis;
 * Wi-Fi Signal Monitoring;
 * Figerprinting Devices;
 * Data-usage Statistics;
 * Page Deduplication;
 * Procfs Leaks;
 * Microarchitectural Attacks;
 * Location Inference;
 * Speech Recognition;
 * Soundcomber;
 * Sensor-based Keyloggers;
 * Rowhammer.

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

## References
1. Grassi, P.A., et al., 2017. Digital identity guidelines. URL: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.
800-63-3.pdf, doi:https://doi.org/10.6028/NIST.SP.800-63-3.
2. Spreitzer, R., et al., 2018. Systematic classification of side-channel attacks: A case study for mobile devices. IEEE Communications Surveys Tutorials 20, 465–488. doi:10.1109/COMST.2017.2779824.

## Cross VM Attacks Diagram


