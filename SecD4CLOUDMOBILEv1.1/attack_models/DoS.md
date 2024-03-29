# Denial of Services

In a DoS attack scenario, the attacker attempts to disrupt the network or disable services provisioned by a server by sending uninterrupted data packets to the target server and without changing nodes, data packets, or decrypting encrypted data. Typically, these data packets take up bandwidth and consume server resources.

## Definition

In such attacks, the attacker attempts to prevent a service or feature that is signed by authorized users from being released by launching various types of floods - SYN flooding, User Datagram Protocol (UDP) flooding, Internet Control Message Protocol (ICMP) attacks ) flooding, etc - on the server.

## Technical Impact
  * Crash, Exit, or Restart;
  * Bypass protection mechanism;
  * Other.

## Risk
  * High.

## Likelihood of Exploit
  * High.

## Attacker's Powers

 * Prevent the availability of a service or resource to authorized users;
 * Perpetrating other types of attacks while services or features are unavailable, such as Spoofing.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the DoS attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed.

## References
1. [https://cwe.mitre.org/data/definitions/400.html]

## Denial of Services Attacks Diagram


