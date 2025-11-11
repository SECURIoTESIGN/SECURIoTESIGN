# Security Testing for Malicious Insider Attacks

## 1. Overview

Insider threats (malicious or negligent) pose major risks in cloud/mobile/IoT environments because insiders often already have valid access, and their attacks may span devices (mobile, IoT), apps, network, and cloud services. Detection is hard because activities can look legitimate. Studies highlight the increased complexity when IoT devices and mobile endpoints are involved.

---

## 2. High-level Testing Workflow / Setup

1. **Define scope & roles**: Identify devices (IoT sensors, gateways, mobile clients), mobile apps (Android/iOS), cloud services/accounts, user roles (employees, contractors), access levels, data flows.
2. **Baseline behaviour & logs**: Capture normal user/device behaviour: login patterns, file accesses, device onboarding, firmware updates, cloud API calls, mobile app telemetry.
3. **Access control and role review**: Examine permissions, user-roles, least-privilege compliance, mobile/IoT device enrolment and provisioning processes.
4. **Static analysis (SAST)**: Review code/configs for mobile apps & IoT firmware, check for excessive privileges, hard-coded credentials, insecure APIs, backdoors.
5. **Dynamic testing (DAST/eb)**: Simulate insider activity: elevated access, data exfiltration via mobile or IoT, lateral movement from IoT to cloud, unauthorized firmware changes. Monitor detection.
6. **Network & endpoint monitoring tests**: Use network sniffing and endpoint logging to see if unusual insider-type behaviours are captured (large file transfers, unusual login times, mobile device abnormal use).
7. **Cloud component tests**: Test compromised cloud credentials or insider misuse of APIs (mobile backend, IoT device management), see how telemetry/alerting responds.
8. **IoT / mobile device tests**: Simulate an insider leveraging mobile or IoT devices (for example, a mobile app pre-installed with extra privileges, an IoT device compromised by a trusted insider).
9. **Reporting and remediation**: Identify control gaps (policy, logging, detection, alerting, privilege management), recommend improvements (user & entity behavior analytics, fine-grained role separation, mobility/IoT device management).

---

## 3. Security Testing Aproach & Tools


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
      <td>Code review / Privilege & role permissions review</td>
      <td>SonarQube / CodeQL</td>
      <td><a href="https://www.sonarqube.org/">SonarQube</a> / <a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Both (mobile + cloud backend)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile app instrumentation & runtime behaviour monitoring</td>
      <td>Frida</td>
      <td><a href="https://frida.re/">Frida</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Endpoint monitoring & user activity simulation</td>
      <td>OSQuery</td>
      <td><a href="https://osquery.io/"></a></td>
      <td>Both (devices & gateways)</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Network packet sniffing & unusual transfer detection</td>
      <td>Wireshark / Zeek</td>
      <td><a href="https://www.wireshark.org/">Wireshark</a> / <a href="https://www.zeek.org/">Zeek</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Cloud function & API scanning & review</td>
      <td>Snyk / Semgrep</td>
      <td><a href="https://snyk.io/">Snyk</a> / <a href="https://semgrep.dev/">Semgrep</a></td>
      <td>Cloud + Backend</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>User & Entity Behaviour Analytics (UEBA) simulation</td>
      <td>Splunk UBA / Elastic UEBA</td>
      <td><a href="https://www.splunk.com/">Splunk UBA</a>" / <a href="https://www.elastic.co/elastic-stack/">Elastic UEBA</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>IoT firmware & device configuration review</td>
      <td>Binwalk / Firmadyne</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a> / <a href="https://github.com/firmadyne/firmadyne">Firmadyne</a></td>
      <td>IoT</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Simulated insider data exfiltration via mobile/IoT device</td>
      <td>Netcat / Curl / Custom script</td>
      <td><a href="https://netcat.sourceforge.net/">Netcat</a> / <a href="https://curl.se/">Curl</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>


---

## 4. Practical Testbed / Setup Checklist

* **Identity & access logs**: collect login/logoff events, privilege escalations, API usage, device enrolment/dis-enrolment, file access logs.
* **Mobile device lab**: invest in Android and iOS test devices; install endpoint monitoring agents; simulate user roles (regular user vs privileged).
* **IoT device lab**: capture firmware images, device logs, connectivity patterns to cloud; simulate insider modifying device config or firmware.
* **Cloud backend**: enable full audit logs (API calls, resource provisioning, data movement, identity changes). Ensure logs are forwarded to SIEM/UEBA system.
* **Behavioral analytics setup**: configure UEBA engine to learn baseline for users/devices; feed logs from mobile/IoT/cloud; simulate insider scenarios (late-night access, large downloads, device provisioning and deprovisioning) to test detection.
* **Network monitoring**: mirror mobile/IoT network traffic to sniffers (Zeek, Wireshark) for unusual patterns (large outbound transfers, odd protocols).
* **Simulated insider attacks**:

  * A user with privileged access exports data via mobile device or IoT gateway to external destination.
  * A contractor installs malicious firmware or config change on IoT device that communicates with cloud.
  * A mobile app acting as a legitimate client is used to change backend settings (via cloud API) that facilitate data siphoning.
* **Policy & control validation**: test least-privilege enforcement, device enrolment/un-enrolment workflows, cloud change-management auditing, mobile & IoT device hardening.
* **Reporting**: summary of gaps (logs missing, user behaviour not baseline-profiled, mobile/IoT devices not monitored, cloud API changes not audited). Recommend remediation: stronger role separation, device management, behavioural monitoring, cloud audit pipelines.

---

## 5. References

1. Kim, A., Kim, H., & Choi, I. (2020). Kim, A., Oh, J., Ryu, J., & Lee, K. (2020). A review of insider threat detection approaches with IoT perspective. *IEEE Access*, 8, 78847-78867.
2. Ali, A., Husain, M., & Hans, P. (2025). Real-time detection of insider threats using behavioral analytics and deep evidential clustering. *arXiv preprint arXiv:2505.15383*.
3. Callegati, F., Giallorenzo, S., Melis, A., & Prandini, M. (2018). Cloud-of-Things meets Mobility-as-a-Service: An insider threat perspective. *Computers & Security*, 74, 277-295.
4. Duncan, A. J., Creese, S., & Goldsmith, M. (2012, June). Insider attacks in cloud computing. In *2012 IEEE 11th international conference on trust, security and privacy in computing and communications* (pp. 857-862). IEEE.
5. Khan, A. Y., Latif, R., Latif, S., Tahir, S., Batool, G., & Saba, T. (2019). Malicious insider attack detection in IoTs using data analytics. IEEE Access, 8, 11743-11753.