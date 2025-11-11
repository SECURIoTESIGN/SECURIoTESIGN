# Node Jamming in Wireless Sensor Networks (WSNs) Model

## Definition

**Node jamming** is the deliberate transmission of radio signals that interfere with the wireless medium used by sensor nodes, preventing legitimate nodes from sending or receiving packets. In WSN/IoT deployments (including mobile apps that rely on edge sensors and cloud backends), jamming causes packet loss, increased retransmissions, depleted batteries, disrupted topology/routing, and ultimately denial-of-service for sensing, control and provisioning workflows.

---

## Attack Categories

* **Constant (barrage) jamming:** continuous emission over the channel to completely deny communications in an area.
* **Deceptive/Reactive jamming:** transmitter injects packets only when legitimate traffic is observed, making detection harder and conserving jammer power.
* **Random/Intermittent jamming:** sporadic interference to create instability, increase retransmissions and drain node energy.
* **Protocol-aware jamming:** targets specific control messages (beacon, ACK, routing updates) to break neighbour discovery or routing.
* **Selective/targeted jamming:** jam only critical nodes (gateway, aggregator, time-sync master) to maximize impact.
* **Physical-layer spoofing/combined attacks:** combine jamming with spoofed control frames or replay to manipulate topology or hide the jammer.
* **Application-level cascading:** cause IoT edge gateways to failover or misreport to cloud services, triggering false alarms, autoscaling, or provisioning errors.

---

## Mitigation & Defensive Controls

**Radio & PHY controls**

* Frequency hopping or channel diversity (FHSS / channel agility).
* Spread-spectrum techniques and adaptive rate/power control to reduce jammer effectiveness.
* Directional antennas and physical separation of critical infrastructure (gateways).

**MAC / protocol controls**

* Clear jam-detection logic (RSSI/SNR thresholds, packet delivery ratio baselines) and rapid switch to alternative MAC/channel.
* Retransmission backoff strategies that avoid synchronized retries and rapid battery drain.
* Use of lightweight anti-jamming MACs (adaptive duty cycles, randomised beaconing).

**Network & topology**

* Multi-path routing and redundant gateway placement (spatial diversity) so single-node jamming does not isolate large regions.
* Mobile or mobile-assisted relays (mobile collectors / drones) to bypass jammed zones for critical data collection.

**Device & energy**

* Energy-aware detection to avoid exhaustion (suspend high-energy retransmit loops when jamming suspected).
* Tamper-evident placement and hardened mounts to prevent co-located jammers.

**Cloud & application**

* Correlate edge telemetry (read-rate drops, RSSI anomalies) with mobile app/cloud logs to detect distributed jamming incidents.
* Graceful degradation in cloud applications (queueing, de-duping, human-in-the-loop) and avoid automated actions that amplify the failure (e.g., uncontrolled autoscaling).
* Fallback channels: BLE, cellular uplink, or wired gateways for critical devices.

**Operational**

* Regular RF site surveys and interference maps; rapid incident playbook (isolate readers, switch channels, engage spectrum authority).
* Legal/regulatory coordination to locate and remove illegal jammers.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                                                             |
| ---------------- | -----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Localized DoS can disrupt safety-critical sensors, break access control, or corrupt telemetry to cloud -- business and safety impact high for critical deployments.    |
| Reproducibility  |        **9** | Simple jammers are inexpensive and easy to build; reactive jammers require more skill but are feasible.                                                               |
| Exploitability   |        **7** | Requires physical proximity or radio access; can be automated (bot of SDRs) to scale attacks in dense environments.                                                   |
| Affected Users   |        **7** | Typically affects users/devices in the jam footprint (gates, checkout lanes, localized sensor zones); cloud services may see degraded telemetry across regions.       |
| Discoverability  |        **6** | RF anomalies are detectable with spectrum monitoring, but intermittent/reactive jammers are harder to spot; detection requires deployed sensors or portable scanners. |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 9 + 7 + 7 + 6 = **37**.
Average = 37 / 5 = **7.4**.

**DREAD average = 7.4**; Rating: **High priority** — focus on detection, spatial redundancy and graceful degradation.

---

## References

1. Akyildiz, I. F., Su, W., Sankarasubramaniam, Y., & Cayirci, E. (2002). Wireless sensor networks: a survey. *Computer Networks*, 38(4), 393–422.
2. Wood, A. D., & Stankovic, J. A. (2002). Denial of service in sensor networks. *Computer*, 35(10), 54–62.
3. Karlof, C., & Wagner, D. (2003). Secure routing in wireless sensor networks: attacks and countermeasures. *Ad Hoc Networks*, 1(2–3), 293–315.
4. Xu, W., Trappe, W., Zhang, Y., & Wood, T. (2005). The feasibility of launching and detecting jamming attacks in wireless networks. *Proceedings of the 6th ACM International Symposium on Mobile Ad Hoc Networking and Computing (MobiHoc)*.
5. ENISA. (2017). *Baseline Security Recommendations for IoT* (or similar ENISA guidance). European Union Agency for Network and Information Security.
6. National Institute of Standards and Technology. (2020). *NISTIR 8259: Foundational Cybersecurity Activities for IoT Device Manufacturers* (or related IoT guidance). NIST.

---



## Node Jamming in WSNs Attack Tree Diagram