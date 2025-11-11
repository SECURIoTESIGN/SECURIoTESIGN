# Security Testing for Pharming Attacks

1. Overview

**Pharming** redirects legitimate user traffic to attacker-controlled sites (or services) by tampering with name resolution or local host mappings (DNS cache poisoning, router DNS setting changes, host-file modification) so victims unknowingly give credentials or the attacker injects malicious payloads. This is more scalable than classic phishing because it affects many users at once. In cloud–mobile–IoT ecosystems pharming can be especially damaging because: devices and mobile apps often rely on DNS, device provisioning and OTA endpoints; compromise of DNS or local resolver can redirect device/cloud traffic (telemetry, firmware updates, auth endpoints) to malicious servers. Testing must therefore cover DNS, routers, devices (mobile & IoT), and cloud backend behaviour and telemetry.

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
    <!-- Network-level DNS tests -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>DNS cache poisoning & response tampering tests</td>
      <td>Scapy, dnschef</td>
      <td><a href="https://scapy.net/">Scapy</a></td>
      <td>Both</td>
    </tr>
    <!-- Router / gateway config tampering -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Router / DHCP/DNS config tamper simulation</td>
      <td>Router firmware testbench / OpenWrt + scripting</td>
      <td><a href="https://openwrt.org/">OpenWrt</a></td>
      <td>Both</td>
    </tr>
    <!-- Host-based pharming (hostfile) -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Local host file & resolver poisoning tests</td>
      <td>Metasploit modules, custom host-file scripts</td>
      <td><a href="https://www.metasploit.com/">Metasploit</a></td>
      <td>Android (rooted), iOS (jailbroken), Desktop</td>
    </tr>
    <!-- IoT device resolver tests -->
    <tr>
      <td>Gray-box</td>
      <td>SAST/DAST</td>
      <td>IoT firmware review for hard-coded DNS / insecure resolver policy</td>
      <td>Binwalk, Ghidra</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a> / <a href="https://ghidra-sre.org/">Ghidra</a></td>
      <td>IoT</td>
    </tr>
    <!-- Mobile app network trust test -->
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Mobile app network validation & hostname verification</td>
      <td>MobSF, Frida</td>
      <td><a href="https://mobsf.github.io/">MobSF</a> / <a href="https://frida.re/">Frida</a></td>
      <td>Android, iOS</td>
    </tr>
    <!-- Cloud backend & certificate handling -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud API & TLS / certificate validation review</td>
      <td>Semgrep, CodeQL, sslscan</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</a> / <a href="https://github.com/rbsec/sslscan">sslscan</a></td>
      <td>Cloud</td>
    </tr>
    <!-- Traffic monitoring / detection -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Network sniffing & DNS anomaly detection</td>
      <td>Zeek, Wireshark, Elastic Stack</td>
      <td><a href="https://www.zeek.org/">Zeek</a> / <a href="https://www.wireshark.org/">Wireshark</a> / <a href="https://www.elastic.co/elastic-stack/">Elastic Stack</a></td>
      <td>Both</td>
    </tr>
    <!-- DNSSEC, DoH/DoT policy checks -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Resolver & DNSSEC/DoT/DoH configuration audit</td>
      <td>dnssec-tools, doh-proxy, validators</td>
      <td><a href="https://www.dnssec-tools.org/">dnssec-tools</a></td>
      <td>Both</td>
    </tr>
    <!-- Machine learning detection / dataset experiments -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Pharming detection using ML on DNS logs</td>
      <td>Python, ELK + ML modules</td>
      <td><a href="https://scikit-learn.org/">scikit-learn</a> / <a href="https://www.tensorflow.org/">scikit-learn</a></td>
      <td>Cloud</td>
    </tr>
  </tbody>
</table>

---

## 2. Testbed & Step-by-step Testing Workflow

### A. Testbed components (minimal)

* **Isolated lab network** (VLAN or air-gapped) with: DNS resolver(s), DHCP server, test router (OpenWrt), gateway that IoT devices use.
* **Test devices**: representative IoT devices (ESP32, Linux gateways), Android (emulator or rooted device), iOS test device (developer/jailbroken if needed), desktops.
* **Cloud test instance**: staging API endpoints, TLS certs, telemetry ingestion (Elastic / Splunk).
* **Tools**: Scapy/dnschef for DNS spoofing, Wireshark/Zeek for capture, Binwalk/Ghidra for firmware, MobSF/Frida for mobile app checks, Semgrep/CodeQL/sslscan for cloud code/TLS checks.

### B. Steps (ordered, safe: run inside isolated test environment)

1. **Baseline collection**

   * Capture normal DNS answers, device hostnames, endpoints, and TLS cert chains. Record device DNS settings (e.g., DHCP vs static) and any hard-coded resolver in firmware.
2. **Host-file pharming test (host-based)**

   * On test mobile/desktop, modify the hosts file (or simulate via an MDM policy) to point a trusted hostname to a malicious staging IP. Verify the app & OS perform proper certificate/hostname verification and fail when server cert mismatch occurs. Use Frida/MobSF to instrument mobile app flows to see if hostname verification is enforced.
3. **Local router / DHCP DNS tampering**

   * Configure OpenWrt test router to hand out malicious DNS server (via DHCP) or to rewrite DNS responses (dnsmasq rules). Observe whether devices accept new resolver and whether traffic goes to attacker staging server. Monitor cloud backend logs for unexpected client IPs/requests.
4. **DNS cache poisoning simulation**

   * Using dnschef/Scapy, craft spoofed DNS responses for frequently requested domains (test-only) and inject into resolver cache. Validate whether devices receive poisoned answers and whether detection (Zeek/IDS/ELK) flags unusual TTLs or multiple authoritative answers.
5. **Firmware/hard-coded DNS review**

   * Extract firmware images (Binwalk) from IoT devices; search for hard-coded hostnames or resolvers, backdoor update endpoints, or lack of TLS pinning. If firmware hard-codes a server IP, test what happens when that IP is hijacked. ([iosrjournals.org][3])
6. **Cloud API resilience checks**

   * Use sslscan / semgrep to confirm TLS configuration (cert pinning, HSTS) and backend rejects requests when Host header mismatch or client cert absent. Try replaying captured requests with redirected Host header to staging server&mdash;verify server checks Host and rejects.
7. **Detection & ML experiments**

   * Feed DNS logs to Elastic/Zeek and run anomaly detection: unusual NXDOMAIN patterns, sudden changes in resolver usage, or TTL anomalies. Optionally run ML detection experiments per literature (ensemble learning on DNS features).

### C. Test scenarios (examples)

* **Scenario 1 &mdash; Host-file pharming on mobile**: alter host file or emulator DNS config; verify mobile wallet or IoT provisioning app rejects mismatched certificates or prompts for re-auth.
* **Scenario 2 &mdash; Rogue DHCP/DNS from compromised gateway**: router gives out malicious DNS server; verify devices DNS queries are resolved to attacker server; observe cloud telemetry anomalies.
* **Scenario 3 &mdash; Firmware-level hardcoded DNS redirect**: change targeted IP behind hardcoded name; see whether devices accept update or telemetry from attacker server; verify firmware signing prevents malicious updates.
* **Scenario 4 &mdash; DNS cache poisoning (simulated)**: poison resolver cache with fake answers for a test domain and check how quickly systems detect & recover.

---

## 3. References

1. Azeez, N. A., Oladele, S. S., & Ologe, O. (2022). **Identification of pharming in communication networks using ensemble learning**. *Nigerian Journal of Technological Development*, 19(2), 172-180.
2. Chimuco, F.T., Sequeiros, J.B.F., Lopes, C.G. et al. **Secure cloud-based mobile apps: attack taxonomy, requirements, mechanisms, tests and automation**. *International. Journal of Information Security*. 22, 833–867.
3. Singh, N., Buyya, R., & Kim, H. (2024). **Securing cloud-based internet of things: challenges and mitigations**. *Sensors*, 25(1), 79.
4. Krishna, T. B. M., Praveen, S. P., Ahmed, S., & Srinivasu, P. N. (2023). **Software-driven secure framework for mobile healthcare applications in IoMT**.*Intelligent Decision Technologies*, 17(2), 377-393.
