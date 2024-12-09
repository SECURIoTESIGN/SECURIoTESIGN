# Orbital Jamming Attacks

This is a DoS attack that targets the communication satellites, using a rogue uplink station to disrupt the intended transmission, aiming to make this service unavailable to users of the target mobile devices.

## Definition

 This type of attack targets low-orbit satellites because, although these low-orbit satellites are attractive due to the low power levels required for communications links from terrestrial terminals, they can also be vulnerable to jamming attacks when used in some applications. In fact, a jammer of reasonable power could easily saturate the RF front-end of a low-orbit satellite, resulting in disabling the link across the entire frequency band. 

## Techniques

1. **Satellite Signal Interference**:
 * Continuous Wave (CW) Jamming: Emit a constant RF signal at the satellite’s frequency;
 * Swept-Frequency Jamming: Vary the jamming frequency across a range;
 * Pulsed Jamming: Intermittently transmit RF pulses.
2. **Geolocation Spoofing**:
 * Transmit false location information to confuse satellite receivers.
3. **Selective Jamming**:
 * Target specific frequency bands (e.g., GPS, communication, weather).

## Consequences

1. **Communication Disruption:** 
 * Interrupt satellite communication links (e.g., military, civilian, emergency services);
 * Impact global navigation systems (e.g., GPS).
2. **Military Implications**:
 * Degrade situational awareness;
 * Compromise command and control operations.

## Mitigation

1. **Diversification of Communication Channels:** Use multiple communication channels and frequencies. If one channel is jammed, the system can switch to another;
2. **Spread Spectrum Techniques:** Spread Spectrum techniques such as Frequency Hopping Spread Spectrum (FHSS) and Direct Sequence Spread Spectrum (DSSS) can be used to resist jamming attacks;
3. **Encryption and Authentication:** Use strong encryption and authentication methods to ensure that only legitimate users can access the system;
4. **Geolocation:** Use geolocation to identify the location of the jamming source and take appropriate action;
5. **Power Control:** Adjust the power levels of the communication signals to minimize the impact of jamming;
6. **Redundancy:** Use redundant systems and networks to ensure availability even in the event of a jamming attack;
7. **Regular Monitoring and Incident Response:** Regularly monitor the system for signs of jamming and have an incident response plan in place.

## Architectural Risk Analysis of Orbital Jamming Vulnerability

The orbital jamming attack targets satellite communication systems and poses significant risks. Let’s analyze it using the Common Vulnerability Scoring System (CVSS) v3.1:

| **Metric**                        | **Description**                                                    | **Value** |
|-----------------------------------|--------------------------------------------------------------------|-----------|
| Base                              |                                                                    |           |
| CVSS ID                           | (placeholder, assigned by vulnerability reporting authority)       |           |
| Attack Vector (AV)                | Network (physical)                                                 | N         |
| Attack Complexity (AC)            | Low. Orbital jamming requires specialized equipment and knowledge. | L         |
| Privileges Required (PR)          | None. Attacker does not need privileges on the target system.      | N         |
| User Interaction (UI)             | None. User action is not required to exploit the vulnerability.    | N         |
| Scope (S)                         | Confidentiality, Availability                                      | C,A       |
| Confidentiality Impact (CI)       | High. Sensitive user data can be intercepted.                      | H         |
| Integrity Impact (II)             | None. Orbital jamming does not modify data.                        | N         |
| Availability Impact (AI)          | Medium. Users may be unable to access the application.             | M         |
| Threat                            | (default values used as likelihood is difficult to assess)         |           |
| Exploitability Ease (PE)          | High                                                               | H         |
| Exploit Code Maturity (EC)        | Not defined                                                        | X         |
| Impact Modifiers (MOD)            | None                                                               |           |
| Environmental                     | (consider specific environment when assigning values)              |           |
| Security Requirements (SR)        | Low. Limited security controls in place to prevent jamming.        | L         |
| Collateral Damage Potential (CDP) | Low. Disruption limited to application functionality.              | L         |
| Other Environmental Factors (O)   | None                                                               |           |

*Remember, addressing orbital jamming vulnerabilities is crucial for maintaining reliable communication and navigation.*



## References
1. [CAPEC-559: Orbital Jamming](https://capec.mitre.org/data/definitions/559.html).
2. Weerackody, V., 2021. Satellite diversity to mitigate jamming in leo satellite mega-constellations, in: 2021 IEEE International Conference on Communications Workshops (ICC Workshops), IEEE, Montreal, QC, Canada. pp. 1–6. doi:10.1109/ICCWorkshops50388.2021.9473519.

## Orbital Jamming Attack Tree Diagram
