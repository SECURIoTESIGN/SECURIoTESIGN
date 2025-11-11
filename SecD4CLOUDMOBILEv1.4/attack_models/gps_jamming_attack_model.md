# GPS (GNSS) Jamming Attack Model

## Definition
**GPS jamming** is the deliberate transmission of radio-frequency noise or interfering signals that overwhelm or mask legitimate Global Navigation Satellite System (GNSS) signals (e.g., GPS, GLONASS, Galileo). The effect is loss or degradation of positioning, navigation, and timing (PNT) services for receivers in the interference footprint.

---

## Attack Categories (examples)

- **Noise jamming (barrage/spot/sweep):** Broadband or narrowband noise that raises the noise floor and prevents receivers from tracking satellites.
- **Repeater/DRFM jamming:** Re-transmission of GNSS signals with distortions to confuse receivers.
- **Localized tactical jamming:** Small portable jammers (vehicle-mounted or handheld) targeting nearby receivers.
- **Wide-area/military-grade jamming:** High-power emitters or coordinated networks that affect large regions (airports, coastlines, cities).
- **Hybrid jamming + spoofing campaigns:** Jamming to deny then spoofing to inject false PNT once receivers lose lock.

---

## Mitigation & Controls
**Detection & situational awareness**: continuous monitoring of GNSS signal strength, SNR, satellite count, and sudden Time/Position discontinuities; deploy spectrum monitoring stations.

**Receiver-level measures**: use multi-constellation, multi-frequency receivers; implement RAIM/RAIM+ and anomaly detection; integrate INS/odometry for short-term holdover; use antenna gain, shielding, and directional/null-steering antennas (CRPA).

**Network & system-level**: diversify PNT sources (GNSS + terrestrial timing sources, e.g., eLoran or network time), deploy centralized monitoring/alerting, and use authenticated GNSS services where available (OSNMA for Galileo).

**Operational**: produce contingency procedures and training (aviation, maritime); coordinate with regulators, CERTs and spectrum authorities; plan exclusion zones and rapid response to identified jammers.

---

## DREAD Risk Assessment (0-10)
| Factor | Score | Rationale |
|---|---:|---|
| Damage Potential | 8 | Critical for safety-of-life systems (aviation, maritime, emergency services) and infrastructure (telecom, finance) where accurate PNT is required. |
| Reproducibility | 7 | Low-cost jammers exist and techniques are well-known; large-scale jamming requires more resources but is feasible. |
| Exploitability | 7 | Requires access to jammers or attackers with RF expertise; misuse of available devices common. |
| Affected Users | 7 | Localized to regional impacts typically, but can affect many users in the footprint (aircraft, ships, vehicles). |
| Discoverability | 8 | Targets are discoverable (airports, ports, critical infrastructure), ongoing interference is detectable via signal metrics. |

**Average DREAD = (8+7+7+7+8)/5 = 7.4**; Rating: **High**

**Priority:** High — implement monitoring and short-term mitigations (INS holdover, antenna upgrades), and coordinate regulatory/operational responses.

---

## References (select)
1. [GNSS Interference](https://www.icao.int/filebrowser/download/5520?fid=5520&utm_source=chatgpt.com).
2. [GNSS Outage and Alterations Leading to Communication](https://ad.easa.europa.eu/blob/EASA_SIB_2022_02_R3.pdf/SIB_2022-02R3_1?utm_source=chatgpt.com).
3. [Space threat landscape - ENISA](https://www.enisa.europa.eu/sites/default/files/2025-03/Space_Threat_Landscape_Report_fin.pdf?utm_source=chatgpt.com). 
4. [initial assessment of the potential impact from a jamming](https://www.ntia.gov/files/ntia/publications/ntiatechnicalmemorandum_10_468.pdf?utm_source=chatgpt.com). 
5. [GNSS under attack: Recognizing and mitigating jamming](https://www.gpsworld.com/gnss-under-attack-recognizing-and-mitigating-jamming-and-spoofing-threats/?utm_source=chatgpt.com). 
6. [Toughen GPS to resist jamming and spoofing](https://www.gpsworld.com/toughen-gps-to-resist-jamming-and-spoofing/?utm_source=chatgpt.com). 

---

## GPS Jamming Attack Tree Diagram