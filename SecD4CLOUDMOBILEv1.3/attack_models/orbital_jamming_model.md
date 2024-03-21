# Orbital Jamming Attacks

This is a DoS attack that targets the communication satellites, using a rogue uplink station to disrupt the intended transmission, aiming to make this service unavailable to users of the target mobile devices.

## Definition

 This type of attack targets low-orbit satellites because, although these low-orbit satellites are attractive due to the low power levels required for communications links from terrestrial terminals, they can also be vulnerable to jamming attacks when used in some applications. In fact, a jammer of reasonable power could easily saturate the RF front-end of a low-orbit satellite, resulting in disabling the link across the entire frequency band. 

## Architectural Risk Analysis of Orbital Jamming Vulnerability

The orbital jamming attack targets satellite communication systems and poses significant risks. Let’s analyze it using the Common Vulnerability Scoring System (CVSS) v3.1:

### Overview

**Objective**: Disrupt or degrade satellite communication, navigation, or reconnaissance capabilities.
**Method**: Emit powerful radio frequency (RF) signals toward the targeted satellite.
**Impact**: Can interfere with satellite signals, rendering them unreliable or unusable.

### Techniques

**Satellite Signal Interference**:
Continuous Wave (CW) Jamming: Emit a constant RF signal at the satellite’s frequency.
Swept-Frequency Jamming: Vary the jamming frequency across a range.
Pulsed Jamming: Intermittently transmit RF pulses.
**Geolocation Spoofing**:
Transmit false location information to confuse satellite receivers.
**Selective Jamming**:
Target specific frequency bands (e.g., GPS, communication, weather).

### Consequences

**Communication Disruption**:
Interrupt satellite communication links (e.g., military, civilian, emergency services).
Impact global navigation systems (e.g., GPS).
**Military Implications**:
Degrade situational awareness.
Compromise command and control operations.

### Mitigation Strategies

**Frequency Hopping**:
Use spread spectrum techniques to change frequencies rapidly.
Makes jamming more difficult.
**Satellite Diversity**:
Deploy multiple satellites to reduce reliance on any single one.
Enhances system resilience.
**Anti-Jamming Algorithms**:
Implement algorithms to detect and mitigate jamming.
Adaptively switch frequencies.

*Remember, addressing orbital jamming vulnerabilities is crucial for maintaining reliable communication and navigation.*



## References
1. [CAPEC-559: Orbital Jamming](https://capec.mitre.org/data/definitions/559.html).
2. Weerackody, V., 2021. Satellite diversity to mitigate jamming in leo satellite mega-constellations, in: 2021 IEEE International Conference on Communications Workshops (ICC Workshops), IEEE, Montreal, QC, Canada. pp. 1–6. doi:10.1109/ICCWorkshops50388.2021.9473519.

## Orbital Jamming Attack Tree
