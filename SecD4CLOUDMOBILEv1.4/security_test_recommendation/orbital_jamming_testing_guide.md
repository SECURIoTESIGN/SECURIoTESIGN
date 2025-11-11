# Security Testing for Orbital Jamming Attacks

## 1. Overview

* In the scenario involving *Orbital Jamming attacks*, attackers intentionally create radio frequency (RF) interference or hostile emissions that disrupt satellite signals used for Global Navigation Satellite Systems (GNSS) and satellite communications (SATCOM). This interference can lead to outages or spoofing, resulting in timing errors that affect mobile devices, Internet of Things (IoT) gateways, and cloud-connected services.
* **Why it matters for cloud-mobile-IoT:** many IoT nodes, mobile apps and cloud systems depend on GNSS timing/position and satcom backhaul. Jamming or spoofing upstream or at LEO/MEO/HEO links can cause device location/timestamp corruption, loss of connectivity, or cascading service degradation.
* Testing are done in **controlled labs** with GNSS/SATCOM simulators, SDRs and shielded chambers (or via vendor test services) to emulate jammers/spoofers and measure resiliency. Commercial GNSS simulators and high-end SATCOM emulators are commonly used for realistic orbital/propagation scenarios.

---

## 2. Security Test Approaches & Tools


<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Test approach</th>
      <th>Analysis Type</th>
      <th>Approach name</th>
      <th>Testing Tool</th>
      <th>Tool Hyperlink</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <!-- Lab-grade GNSS / SATCOM simulation -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>GNSS / SATCOM scenario simulation (orbit, propagation, interferer)</td>
      <td>Rohde & Schwarz GNSS & Vector Signal Generators / Spirent GSS9000</td>
      <td><a href="https://www.rohde-schwarz.com/">Rohde & Schwarz GNSS</a> / <a href="https://www.spirent.com/">Spirent GSS9000</a></td>
      <td>Both</td>
    </tr>
    <!-- Open-source GNSS emulation -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Open-source GNSS signal generation for lab testing</td>
      <td>GPS-SDR-SIM / GNSS-SDR</td>
      <td><a href="https://github.com/osqzss/gps-sdr-sim">PS-SDR-SIM</a> / <a href="https://github.com/gnss-sdr/gnss-sdr">GNSS-SDR</a></td>
      <td>Both</td>
    </tr>
    <!-- SDR transmitters for interferer/emulation (lab only) -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Controlled jamming / directed interference (lab, shielded)</td>
      <td>USRP (Ettus) / HackRF One + GNU Radio</td>
      <td><a href="https://www.ettus.com/">USRP (Ettus)</a> / <a href="https://github.com/mossmann/hackrf">HackRF One</a> / <a href="https://www.gnuradio.org/">GNU Radio</a></td>
      <td>Both</td>
    </tr>
    <!-- GNSS interference & anti-jam testing -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Anti-jamming / antenna nulling & CRPA testing</td>
      <td>High-end vector signal generators + CRPA testbeds (R&S / Spirent)</td>
      <td><a href="https://www.rohde-schwarz.com/">Rohde-Schwarz</a> / <a href="https://www.spirent.com/">Spirent</a></td>
      <td>Both</td>
    </tr>
    <!-- Spectrum analysis & detection -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Spectrum monitoring & RFI detection</td>
      <td>Spectrum analyzer (Keysight, Rigol), RTL-SDR, RF-Explorer</td>
      <td><a href="https://www.keysight.com/">Keysight</a> / <a href="https://www.rigolna.com/">Rigol</a> / <a href="https://www.rtl-sdr.com/">RTL-SDR</a></td>
      <td>Both</td>
    </tr>
    <!-- Satellite link & modem testing -->
    <tr>
      <td>White-box</td>
      <td>SAST/DAST</td>
      <td>Satellite terminal/modem conformance and link emulation</td>
      <td>Skydel / GSG GNSS & SATCOM emulators</td>
      <td><a href="https://skydel.com/">Skydel</a> / <a href="https://safran-navigation-timing.com/">Safran - Navigation & Timing</a></td>
      <td>Both</td>
    </tr>
    <!-- On-orbit interference monitoring -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>On-orbit / spacecraft RF monitoring & telemetry analysis</td>
      <td>OPS-SAT test experiments / satellite telemetry ingest</td>
      <td><a href="https://commons.erau.edu/ops-sat/">OPS-SAT</a> / <a href="https://ntrs.nasa.gov/">Satellite telemetry</a></td>
      <td>Both</td>
    </tr>
    <!-- GNSS receiver resilience testing -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Receiver performance under jamming/spoofing</td>
      <td>GPS/GNSS receiver test suites (R&S, Spirent) / GNSS-SDR</td>
      <td><a href="https://www.rohde-schwarz.com/">Rohde-Schwarz</a> / <a href="https://github.com/gnss-sdr/gnss-sdr">GNSS-SDR</a></td>
      <td>Both</td>
    </tr>
    <!-- Network / cloud impact testing -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>End-to-end service disruption simulation (mobile/IoT → cloud)</td>
      <td>Testbed orchestration: Docker, ns3, tc (traffic control), Zeek</td>
      <td><a href="https://www.zeek.org/">Zeek</a> / <a href="https://www.nsnam.org/">ns-3</a></td>
      <td>Both</td>
    </tr>
    <!-- Legal / compliance & site shielding -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Regulatory compliance & RF shielding validation</td>
      <td>Anechoic chamber / RF attenuators / licensed test range</td>
      <td>Vendor labs (Keysight, ETS-Lindgren)</td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Representative Test Scenarios

1. **GNSS jamming tolerance:** in chamber, increase broadband noise near L1/L5 and measure GNSS receiver time-to-first-fix, PNT degradation, and fallover behavior for IoT devices and mobile phones. Record application impacts (e.g., time stamps, scheduled tasks).
2. **Directed narrowband jammer against SATCOM uplink:** simulate carrier nulling or narrowband interference on satellite uplink frequency (lab only) and measure SATCOM modem BER, link margin, and reconnection time. Use vendor emulators for precise link budgets.
3. **Spoofing + replay hybrid:** use GNSS simulator to create plausible false GNSS constellation (time/position ramp) to test mobile wallet / IoT geofencing and cloud time sync robustness. Validate RAIM/receiver anti-spoofing or application checks.
4. **CRPA nulling & anti-jam verification:** test multi-antenna anti-jam systems with injected interferer to validate beamforming/nulling performance and verify position/timing recovery.
5. **End-to-end cloud impact test:** while GNSS degraded, simulate how IoT fleet telemetry, mobile app features and cloud scheduling reliant on PNT behave&mdash;check logs, alert triggers, and failure modes. Use ns3 / Docker testbed to emulate large-scale effects.

---

## 4. References

1. Tedeschi, P., Sciancalepore, S., & Di Pietro, R. (2022). Satellite-based communications security: A survey of threats, solutions, and research challenges. *Computer Networks*, 216, 109246. 
2. Olsson, G. K., Nilsson, S., Axell, E., Larsson, E. G., & Papadimitratos, P. (2023, April). Using mobile phones for participatory detection and localization of a gnss jammer. In *2023 IEEE/ION Position, Location and Navigation Symposium (PLANS)* (pp. 536-541). IEEE.
3. Otay, H., Humadi, K., & Kurt, G. K. (2023, November). Dark Side of HAPS Systems: Jamming Threats towards Satellites. In *2023 IEEE Future Networks World Forum (FNWF)* (pp. 1-6). IEEE.
3. Pirayesh, H., & Zeng, H. (2022). Jamming attacks and anti-jamming strategies in wireless networks: A comprehensive survey. *IEEE communications surveys & tutorials*, 24(2), 767-809.
4. Troglia Gamba, M., Polidori, B. D., Minetto, A., Dovis, F., Banfi, E., & Dominici, F. (2024). GNSS radio frequency interference monitoring from LEO satellites: An in-laboratory prototype. Sensors*, 24(2), 508.
5. Gilabert, R., Gutierrez, J., & Dill, E. (2024, September). GPS Multipath Emulation using Software Generated Signals. In *2024 AIAA DATC/IEEE 43rd Digital Avionics Systems Conference (DASC)* (pp. 1-6). IEEE.