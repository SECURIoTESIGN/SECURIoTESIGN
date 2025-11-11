# GPS Spoofing Attacks Models
**GPS Spoofing Attacks** involve broadcasting counterfeit GPS signals to deceive receivers into calculating incorrect positions, times, or velocities. These attacks compromise systems that depend on GNSS (Global Navigation Satellite Systems), affecting everything from autonomous vehicles to time-sensitive cloud operations.

- **Cloud**: Disrupts time synchronization and geofencing-based access.
- **Mobile**: Misleads navigation, location-based services, and emergency response.
- **IoT**: Affects drones, smart logistics, and industrial automation.

---

## Attack Categories

| Category               | Description                                                                 | Target Ecosystem     |
|------------------------|-----------------------------------------------------------------------------|-----------------------|
| **Signal Injection**   | Transmits fake satellite signals to override legitimate ones                | Mobile, IoT           |
| **Replay Attacks**     | Replays recorded GPS data to simulate false movement or location            | IoT, Cloud            |
| **Software Manipulation** | Alters firmware or apps to report false GPS data                         | Mobile, IoT           |
| **Time Spoofing**      | Manipulates GPS time to disrupt synchronization                             | Cloud, IoT            |
| **Multi-Vector Spoofing** | Combines spoofing with jamming or cyber attacks                          | All                   |

---

## Attack Mitigations

- **Cryptographic GNSS Authentication**: Use authenticated signals like Galileo OS-NMA or GPS M-code.
- **Multi-Sensor Fusion**: Combine GPS with inertial, visual, or cellular data.
- **Spoofing Detection Algorithms**: Monitor signal strength, angle of arrival, and consistency.
- **Time and Location Validation**: Cross-check with trusted sources or reference stations.
- **Firmware Integrity Checks**: Prevent unauthorized software modifications.

---

## DREAD Risk Assessment

| DREAD Component     | Definition                                                                 | Score (1–10) | Assessment |
|---------------------|----------------------------------------------------------------------------|--------------|------------|
| **Damage Potential**| Extent of harm caused to systems and users                                 | 9            | High       |
| **Reproducibility** | Ease with which the attack can be repeated                                 | 7            | High       |
| **Exploitability**  | Effort required to launch the attack                                       | 8            | High       |
| **Affected Users**  | Number of users or systems impacted                                        | 7            | High       |
| **Discoverability** | Likelihood of the attack being detected or noticed                         | 5            | Medium     |

**Overall Risk Score:** 36/50 = 7.2; **Ranking:** High.

---

## References

1. Dang, Y., Benzaïd, C., Yang, B., Taleb, T., & Shen, Y. (2022). Deep-ensemble-learning-based GPS spoofing detection for cellular-connected UAVs. *IEEE Internet of Things Journal*, 9(24), 25068–25085.
2. Tohidi, S., & Mosavi, M. R. (2020, January). Effective detection of GNSS spoofing attack using a multi-layer perceptron neural network classifier trained by PSO. In 2020 25th international computer conference, *computer society of iran (CSICC)* (pp. 1-5). IEEE..
3. Tippenhauer, N. O., Pöpper, C., Rasmussen, K. B., & Capkun, S. (2011, October). On the requirements for successful GPS spoofing attacks. In *Proceedings of the 18th ACM conference on Computer and communications security* (pp. 75-86).

---

## GPS Spoofing Attack Tree Diagram


