# GPS Jamming Attacks

This is a DoS attack that targets the GPS sensor, aiming to make this service (position, path, speed, direction, time, and distance) unavailable to users of the target mobile devices.

## Definition

 This attack aims to interrupt or obstruct the communication between the emitting satellite and the device (smartphone/tablet) receiving the GPS signal. Normally, the attack consists of blocking the signal from the receiver, since the receiving signal is weaker compared to the broadcasting signal, and can be carried out in two different ways:
 
  * Blanket Jamming;
  * Deception Jamming.  
 
## Technical Impact

 * Service unavailability.

## Typical Severity

 * High

## Risk Analysis

 * High Risk.

## Likelihood of Exploit

 * Low.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the GPS Jamming attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. [CAPEC-627: Counterfeit GPS Signals](https://capec.mitre.org/data/definitions/627.html).

## GPS Jamming Attacks Diagram
