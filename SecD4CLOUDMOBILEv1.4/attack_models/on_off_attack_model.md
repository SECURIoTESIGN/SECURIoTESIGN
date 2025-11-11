# On–Off Attack Model

## Definition

An **On–Off attack** (also called intermittent or periodic jamming/availability attack) is a strategy where an adversary alternates between active interference/attack periods (*on*) and idle periods (*off*) to **maximize disruption while minimizing detection and resource cost**. In IoT/WSN and mobile/cloud contexts this might mean intermittent RF jamming, sporadic packet drops, selective gateway outages, or periodic service-layer interference that causes missed telemetry, repeated retransmissions, battery drain, or instability in autoscaling and provisioning systems.

---

## Attack Categories

* **Intermittent RF jamming:** jammer transmits only periodically or when traffic is detected to conserve power and evade simple alarms.
* **Duty-cycled DoS at link/MAC layer:** attacker injects interference or malformed frames intermittently to provoke retransmissions and energy drain.
* **Application-layer on–off flooding:** bursts of high-rate API calls or connection attempts that alternate with quiet periods to evade rate-based detection and force autoscaling.
* **Gateway/edge on–off compromise:** attacker briefly compromises a gateway (or toggles service) to inject bad telemetry or commands, then withdraws to hide.
* **Power/energy-depletion attacks:** intermittent activity timed to coincide with scheduled wake windows of battery-powered IoT nodes, causing repeated wake-ups and rapid battery exhaustion.
* **Coordinated multi-vector on–off campaigns:** combine short RF jamming bursts with brief provisioning attacks or replay attempts during off-periods to compound effects.

---

## Mitigations & defensive controls (practical priorities)

**Radio / PHY & device**

* Use frequency/channel agility (FHSS or channel-hopping), listen-before-talk, and spread-spectrum to reduce single-channel dependency.
* Duty-aware MACs with randomized wake schedules and adaptive backoff to avoid synchronized retries that amplify energy drain.
* Multi-path and redundant gateways (spatial diversity) so intermittent outage of one path doesn’t cut service.

**Protocol & application**

* Implement anti-replay/nonces, per-transaction sequence counters, and robust duplicate detection at cloud backends to reduce impact of intermittent replays/floods.
* Application-level smoothing and debouncing: aggregate telemetry, tolerate transient losses, and avoid immediate autoscale triggers on short spikes—use anomaly scoring rather than single-metric thresholds.

**Energy & power defenses**

* Design wake windows and polling strategies that are resilient to timed bursts (randomized schedules, exponential backoff, energy-aware retry logic).
* Monitor battery drain trends and trigger alerts on unusual energy profiles for devices.

**Detection & monitoring**

* Correlate intermittent anomalies across layers: short RF noise spikes, concurrent retransmissions, repeated failed API attempts, and sudden autoscaling events.
* Deploy distributed spectrum sensors or piggyback SNR/noise-floor telemetry to detect low-duty jammers.
* Use sliding-window analytics and burst-detection (short high-amplitude anomalies) rather than only long-term averages.

**Operational & architecture**

* Use fallback communications (cellular, BLE, wired) for critical devices and out-of-band control channels for management-plane actions.
* Harden provisioning & gateway firmware to prevent brief compromises and require attestation for critical operations.
* Maintain incident runbooks that include on–off detection, spectrum triage, and controlled de-escalation of autoscaling.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Short rationale                                                                                                                                      |
| ---------------- | -----------: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Causes availability loss, misreported telemetry, battery depletion and costly autoscaling or operational disruption for critical IoT/cloud services. |
| Reproducibility  |        **8** | Intermittent attacks are easy to implement (timers or reactive jammers) and inexpensive; techniques are well-known.                                  |
| Exploitability   |        **7** | Requires proximity/radio access for RF variants or ability to trigger application bursts; feasible against exposed deployments and weak onboarding.  |
| Affected Users   |        **7** | Localized but can cascade—many nodes or customers may be affected (gateways, sensor clusters, mobile users).                                         |
| Discoverability  |        **5** | Intermittent nature makes detection and forensics harder; short bursts can evade threshold-based alarms.                                             |
**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 7 + 5 = **35**.
Average = 35 / 5 = **7.0**.

**DREAD average = 7.0**; Rating: **High Risk**.

---

## References

1. Xu, W., Trappe, W., Zhang, Y., & Wood, T. (2005). *The feasibility of launching and detecting jamming attacks in wireless networks.* Proceedings of the 6th ACM International Symposium on Mobile Ad Hoc Networking and Computing (MobiHoc).
2. Wood, A. D., & Stankovic, J. A. (2002). *Denial of service in sensor networks.* Computer, 35(10), 54–62.
3. Akyildiz, I. F., Su, W., Sankarasubramaniam, Y., & Cayirci, E. (2002). *Wireless sensor networks: a survey.* Computer Networks, 38(4), 393–422.
4. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/](https://www.enisa.europa.eu/)
5. National Institute of Standards and Technology. (2020). *NISTIR 8259: Foundational Cybersecurity Activities for IoT Device Manufacturers.* NIST. [https://doi.org/10.6028/NIST.IR.8259](https://doi.org/10.6028/NIST.IR.8259)

---                                  |


## On-Off Attack Tree Diagram


