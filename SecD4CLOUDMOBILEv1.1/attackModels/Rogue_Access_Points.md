# Rogue Access Point Attacks

This attack aims to access and steal sensitive data from legitimate users of a wireless network by redirecting them to a fake network (from a fake access point) using a stronger signal than that of the real network, which facilitates the authentication of the target mobile devices to the fraudulent network, given the fact that this authentication is automatic.

## Definition

 The Access Points (AP) in a Wi-Fi networks are subject to the attack of access point spoofing, usually called Rogue Access Point (RAP). This attack consists of cloning the Media Access Control (MAC) address and Service Set IDentifier (SSID) of an AP, giving rise to the emergence of a fake access point posing as a genuine one, leading users to connect to this new network as if they were connecting to the genuine network. After connection, an attack is able to eavesdrops on its communication to hijack client's communication, re-direct clients to malicious websites, steal credentials (session hijacking) of the clients connecting to it.
 
## Technical Impact

* Read Data;
* Gain Privileges or Assume Identity.

## Typical Severity

* Low.

## Risk Analysis

  * Very High Risk.

## Likelihood of Exploit

  * Medium.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the Rogue Access Point attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. [CAPEC-175: Code Inclusion](https://capec.mitre.org/data/definitions/175.html).

## Rogue Access Point Attacks Diagram
