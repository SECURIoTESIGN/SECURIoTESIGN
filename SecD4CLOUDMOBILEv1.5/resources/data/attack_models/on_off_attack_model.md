# On-Off Attack

An On-Off attack is a security threat that jeopardizes the trustworthiness of Internet of Things (IoT) resources. Let’s delve into the details:

## Overview

* **Objective**: To disrupt trust mechanisms in IoT environments.
* **Method**: Nodes exhibit both good and bad behaviors randomly, evading classification as a menace.
* **Impact**: Undermines trust-based security measures.

## How On-Off Attacks Work

1. **Behavior Variability**:
* Nodes alternate between cooperative and malicious behaviors.
* This unpredictability challenges trust assessment.
2. **Trust Abuse**:
* Nodes exploit their dual nature to avoid being labeled as threats.
* Countermeasures relying on prior trust knowledge struggle.

## Mitigation Strategies

1. **Adaptive Duty Cycling:** Implement adaptive duty cycling for IoT devices. This technique adjusts the active and sleep periods of a device based on network conditions, making it harder for an attacker to predict when the device is active;
2. **Randomized Sleep Schedules:** Use randomized sleep schedules for IoT devices. This can prevent an attacker from predicting when a device is in sleep mode and launching an On-Off attack during that time;
3. **Intrusion Detection Systems (IDS):** Implement IDS in the cloud to monitor network traffic and detect any suspicious activities that could indicate an On-Off attack;
4. **Regular Monitoring and Auditing:** Regularly monitor the performance of your IoT devices and conduct audits to identify and address any potential On-Off attacks;
5. **Network Redundancy:** Implement network redundancy to ensure that there are multiple paths for data transmission. This can help maintain network connectivity even if some devices are under an On-Off attack.

## Architectural Risk Analysis of On-Off Vulnerability

The On-Off attack poses a threat to trust security in Internet of Things (IoT) environments. Let’s assess the risk using the Common Vulnerability Scoring System (CVSS) v3.1:

| **Factor**                                        | **Description**                                                                                  | **Value**                                     |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Attack   Vector (AV):                             | Network   (Exploiting the application or system functionality)                                   | Network   (N)                                 |
| Attack   Complexity (AC):                         | Low   (Relatively simple to automate on/off cycles)                                              | Low   (L)                                     |
| Privileges   Required (PR):                       | None   (Denial-of-Service doesn't require privileged access)                                     | None   (N)                                    |
| User   Interaction (UI):                          | None   (Attack can be automated)                                                                 | None   (N)                                    |
| Scope   (S):                                      | Denial-of-Service   (DoS)                                                                        |         Denial-of-Service (DoS)               |
| Confidentiality   Impact (C):                     | None   (DoS doesn't directly impact confidentiality)                                             | None   (N)                                    |
| Integrity   Impact (I):                           | Low   (DoS might disrupt ongoing data processing but not necessarily corrupt data)               | Low   (L)                                     |
| Availability   Impact (A):                        | High   (DoS can render the application or system unavailable)                                    | High   (H)                                    |
| Base   Score (assuming High Availability Impact): | 0.85   * (AV:N/AC:L/PR:N/UI:N) * (S:DoS/C:N/I:L/A:H)                                             | 5.3   (Medium)                                |
| Temporal   Score (TS):                            | Public   exploit tools available for DoS via power cycling?                                      |         Depends on exploit availability       |
| Environmental   Score (ES):                       | Depends   on application resilience to DoS attacks, system redundancy, monitoring   capabilities | Varies                                        |


## On-Off Attack Tree Diagram


