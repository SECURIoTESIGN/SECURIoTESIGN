# Security Testing for Hardware Integrity Attacks

## 1. Overview

Hardware integrity attacks (hardware Trojans, supply-chain implants, fault/glitch injection, side-channel exfiltration, physical tampering and counterfeiting) can be introduced during design, fabrication, distribution, or deployment and are difficult to detect with software-only testing; so hardware-focused validation and supply-chain controls are required.

---

## 2. Testing Setup

1. **Threat modelling & asset inventory**

   * Inventory components (MCU/SoC, radio modules, power management, secure elements, bootloader, firmware, enclosures, connectors) and define trust boundaries (cloud, gateway, mobile client, device hardware). Use SBOMs and HW provenance records where possible. 

2. **Golden-reference & baseline creation**

   * Maintain golden designs/firmware images and expected side-channel / performance baselines for comparison (voltage, current, power traces, timing). Baselines enable anomaly detection for implants or tampered silicon.

3. **Pre-silicon & supply-chain controls**

   * Design reviews, IP vetting, EDA flow checks, provenance tracking, secure procurement and QA audits. (Mitigates insertion during design/fab/distribution.) 

4. **Static analysis (SAST) of RTL/firmware**

   * RTL/netlist checks, EDA tool logs, firmware source code review, secure-boot validation, digital signatures and SBOM verification.

5. **Dynamic hardware testing (DAST / post-silicon)**

   * Side-channel analysis (power, EM) versus baseline, fault-injection (voltage/clock/glitch, EM, laser if available), JTAG/Debug port probing, bus sniffing, physical tamper / enclosure stress testing.

6. **Firmware reverse engineering & runtime instrumentation**

   * Extract firmware (if possible), perform binary analysis, fuzz firmware interfaces, emulate where feasible, use runtime instrumentation (Frida, dynamic hooks) on mobile apps that interact with devices.

7. **Reverse engineering & physical inspection**

   * X-ray, decap / optical inspection, PCB trace audit, component authenticity checks, BGA inspection, and microprobing where resources allow.

8. **Monitoring & runtime integrity**

   * Deploy runtime monitors, TPM/secure element attestation, anomaly detection in cloud telemetry (unusual behavior from a device), and continuous re-validation (periodic re-attestation).

9. **Reporting & remediation**

   * Triage anomalies into firmware patch, revocation / recall, procurement policy changes, or forensics / disclosure.



---

## 3. Security Testing Approach & Tools

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
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>RTL / Netlist review</td>
      <td>Formal/Static EDA checks (e.g., SpyGlass, Custom scripts)</td>
      <td><a href="https://www.synopsys.com">Formal/Static EDA checks</a></td>
      <td>Both (HW-level)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Side-channel analysis (SCA)</td>
      <td>ChipWhisperer</td>
      <td><a href="https://chipwhisperer.io/">ChipWhisperer</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Fault / Glitch injection</td>
      <td>ChipWhisperer (glitch), Riscure Fault Injection lab (commercial)</td>
      <td><a href="https://chipwhisperer.io/">ChipWhisperer (glitch)</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Debug / JTAG port enumeration</td>
      <td>JTAGulator</td>
      <td><a href="https://www.grandideastudio.com/jtagulator">JTAGulator</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / SCA</td>
      <td>Bus sniffing / protocol analysis</td>
      <td>Bus Pirate, Saleae Logic</td>
      <td><a href="https://dangerousprototypes.com/docs/Bus_Pirate">Bus Pirate</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST / DAST</td>
      <td>Firmware extraction & analysis</td>
      <td>Binwalk, Firmadyne, Ghidra</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Runtime instrumentation / mobile ↔ device</td>
      <td>Frida</td>
      <td><a href="https://frida.re/"></a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Platform / OS HW checks</td>
      <td>chipsec (Intel)/Platform diagnostics</td>
      <td><a href="https://github.com/chipsec/chipsec">chipsec (Intel)</a></td>
      <td>Both (x86 targets; limited ARM support)</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Firmware fuzzing</td>
      <td>TriforceAFL / RPFuzzer / GraphFuzz (research)</td>
      <td>Relevant repos/papers (TriforceAFL variants) / arXiv (GraphFuzz)</td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical tamper & enclosure testing</td>
      <td>EM probe, thermal imaging, mechanical tamper tools</td>
      <td>See vendor sites (e.g., Keysight, Tektronix)</td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Supply-chain provenance & SBOM checks</td>
      <td>SBOM tools (CycloneDX/SPDX tooling), procurement auditing</td>
      <td><a href="https://cyclonedx.org/">SBOM tools</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Reverse engineering / PCB inspection</td>
      <td>X-ray, microscope, decap labs, PCB inspection tools</td>
      <td>Laboratory services & vendors (e.g., TEK/Keysight/third-party labs)</td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 4. Practical Testbed Setup

* **Hardware lab:** ChipWhisperer kit, high-speed oscilloscope (≥100 MS/s for power traces), EM probe, programmable power supply, glitching module (voltage/clock), JTAGulator, Bus Pirate, Saleae logic analyzer, bench microscope, hot-air rework station, X-ray / decap access via external lab (if required).
* **Firmware & analysis workstation:** Kali/Ubuntu, Ghidra, Binwalk, Firmadyne, IDA/objdump, radare2, custom scripts.
* **Mobile test devices:** rooted/jailbroken Android and iOS test phones (for instrumentation), Frida + adb/ideviceinstaller.
* **Cloud side:** telemetry ingestion, attestation verification services, automated anomaly detection (compare device behavior vs golden baseline).
* **Supply-chain tooling:** SBOM generation (CycloneDX/SPDX), procurement provenance database, certificate-based attestation for secure elements.
* **Safety & compliance:** ESD-safe bench, documented chain of custody procedures for examined devices, legal sign-offs for destructive analysis and export-controlled equipment.

---

## 5. Quick Example Test Scenarios

1. **Side-channel detection of hardware Trojan**

   * Capture power traces from device running known workload; compare statistical features to golden reference; use ChipWhisperer + PCA / ML anomaly detector.

2. **Glitch injection to bypass secure boot**

   * Apply clock/voltage glitch at boot to see if bootloader signature checks can be bypassed; perform repeated tests, correlate with golden logs. 

3. **JTAG port discovery & firmware dump**

   * Use JTAGulator to locate debug pins, use OpenOCD to read memory/flash; analyze firmware with Ghidra and binwalk. 

4. **Supply-chain & provenance audit**

   * Validate SBOM; check component lot numbers and compare with expected suppliers; run counterfeit part checks (visual / X-ray if suspicious). 

---

## 6. References

1. Sidhu, S., Mohd, B. J., & Hayajneh, T. (2019). Hardware security in IoT devices with emphasis on hardware Trojans. *Journal of Sensor and Actuator Networks*, 8(3), 42. [https://doi.org/10.3390/jsan8030042](https://doi.org/10.3390/jsan8030042).
2. Chen, D., Xu, Y., Liu, X., Zhang, F., He, G., & Chen, Y. (2020). Hardware Trojans in chips: A survey for detection and prevention. *Sensors* (Basel), 20(18), 5165. [https://doi.org/10.3390/s20185165](https://doi.org/10.3390/s20185165).
3. Rao, A., Priya, A., Richardson, M., Dorey, P. & Brown R. (2022). Securing the Internet of Things supply chain. *IoT Security Foundation*. [https://www.iotsecurityfoundation.org/](https://www.iotsecurityfoundation.org/). 
4. Chatterjee, D., Maitra, S., Mishra, N., Shukla, S., & Mukhopadhyay, D. (2025). Hardware security in the connected world. *Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery*, 15(3), e70034.
5. Situ, L., Zhang, C., Guan, L., Zuo, Z., Wang, L., Li, X., Liu, P. & Shi, J. (2023). Physical devices-agnostic hybrid fuzzing of IoT firmware. *IEEE Internet of Things Journal*, 10(23), 20718-20734.