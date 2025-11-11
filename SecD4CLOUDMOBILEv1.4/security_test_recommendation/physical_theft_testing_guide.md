# Security Testing for Physical Theft Attacks

## 1. Overview

In IoT-mobile-cloud ecosystems, physical theft of devices (sensors, gateways, mobile devices) or mobile endpoints allows attackers to bypass many software protections: they may extract keys, remove storage media, implant malware, clone devices, or misuse devices as trusted network endpoints. Research reviews of IoT threat models highlight physical attacks and theft as major vectors. Testing the resilience of devices, encryption at rest, secure boot, tamper-evidence, remote wipe, and backend recognition of stolen nodes is therefore critical.

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
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Firmware code review for secure boot / key storage</td>
      <td>Ghidra / Binwalk</td>
      <td><a href="https://ghidra-sre.org/">Ghidra</a></td>
      <td>IoT node / gateway</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile device theft simulation & remote wipe verification</td>
      <td>Mobile Device Management (MDM) test suite / custom script</td>
      <td> &mdash; Custom test  </td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical device removal & insertion in network (stolen node test)</td>
      <td>Test fleet of devices + network monitoring (Zeek/Wireshark)</td>
      <td><a href="https://www.zeek.org/">Zeek</a></td>
      <td>IoT node / gateway</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Mobile app review for stolen device authentication bypass</td>
      <td>MobSF / Frida</td>
      <td><a href="https://mobsf.github.io/">MobSF</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud backend review for stolen-device detection & revocation logic</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a></td>
      <td>Cloud</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Key extraction / memory dump from stolen device</td>
      <td>ChipWhisperer / JTAGulator</td>
      <td><a href="https://chipwhisperer.io/">ChipWhisperer</a></td>
      <td>IoT node / mobile</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical tamper-evidence test (tamper seals, enclosure breach)</td>
      <td>Visual inspection kit / tamper-switch test rig</td>
      <td>&mdash; hardware test rig </td>
      <td>IoT node / gateway</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Network traffic monitoring for stolen-node behaviour (new MAC/IP)</td>
      <td>Elastic Stack / Splunk</td>
      <td><a href="https://www.elastic.co/elastic-stack/">Elastic Stack</a></td>
      <td>Cloud/mobile/IoT</td>
    </tr>
  </tbody>
</table>

---

## 3. Testing Setup & Workflow

### Components & Setup

* **Test device pool:** IoT sensor/gateway units identical to production devices; mobile smartphones/tablets used by users; cloud backend simulation environment.
* **Physical theft scenarios:** designate a set of devices as stolen &mdash; these will be removed from lab, tampered or replaced, then reintroduced.
* **Monitoring/logging:** network monitoring (Zeek/Wireshark) at gateway; cloud logging of device IDs, firmware version, last-seen timestamp, telemetry.
* **Firmware & mobile code review:** obtain firmware images (if available) for key extraction & secure boot checks; mobile apps for remote wipe and device-loss handling.
* **Revocation & detection logic:** cloud backend should have logic to revoke lost/stolen device IDs, monitor abnormal behaviour (new IPs, duplicate IDs, out-of‐region connections).
* **Physical test rig:** use tamper-switch test rig, visual inspection kits, JTAG/USB debug port exposure test.

### Step-by-step Workflow

1. **Baseline capture:** deploy all devices in lab; take inventory (device ID, firmware version, MAC/IP, geolocation if applicable) and capture normal telemetry & network flows.
2. **Firmware/mobile review:** run Ghidra/Binwalk on node firmware; check for secure boot, key storage, debug ports. Review mobile app for remote wipe, device registration, lost-device handling.
3. **Stolen device simulation:**

   * Remove one IoT node from lab and later re-connect it (either tampered or unchanged) &mdash; monitor how the backend handles it.
   * On mobile device branch: simulate lost/stolen handset; test remote wipe, account logout, device block.
4. **Key extraction test:** With stolen node in lab, attempt JTAG/USB debug access to extract keys or firmware. Use ChipWhisperer/JTAGulator in controlled environment.
5. **Reintroduction & network test:** Reconnect the stolen/tampered device to network. Monitor for abnormal behaviour (new IP, duplicate ID, unexpected traffic patterns) and ensure backend revokes/quarantines device.
6. **Tamper-evidence test:** Open device enclosure, trigger tamper switch or remove internal components, re-connect; verify if device logs a tamper event or locked.
7. **Mobile lost device test:** Simulate user lost phone; ensure remote wipe works, apps do not auto-log back in, MFA required, device cannot access IoT/gateway/cloud.
8. **Reporting & remediation:** Document which devices lacked tamper-evidence, which mobile apps lacked remote-wipe or lockout logic, and which backend lacked revocation capability. Provide remedial recommendations: asset tagging, secure boot, encrypted storage, remote wipe, tamper monitoring, endpoint inventory.

---

## 4. References

1. Mehari Msgna, A. (2022). Anatomy of attacks on IoT systems: review of attacks, impacts and countermeasures. *Journal of Surveillance, Security and Safety*, 3, 150-173. [https://doi.org/10.20517/jsss.2022.07](https://doi.org/10.20517/jsss.2022.07).
2. Kumar Sikder, A., Petracca, G., Aksu, H., Jaeger, T., & Uluagac, A. S. (2018). A Survey on Sensor-based Threats to Internet-of-Things (IoT) Devices and Applications. *arXiv preprint arXiv:1802.02041*.
3. Islam, M. R., & Aktheruzzaman, K. M. (2020). An analysis of cybersecurity attacks against internet of things and security solutions. *Journal of Computer and Communications*, 8(04), 11.