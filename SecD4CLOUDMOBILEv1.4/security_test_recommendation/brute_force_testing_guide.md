## Security Testing set-up for Brute-Force Attacks


## 1. Overview

Validate how resilient your cloud APIs, mobile apps and IoT gateways/devices are to automated guessing (credential brute-force, credential-stuffing, PIN/PATTERN attempts, protocol-level password guessing) and verify detection + throttling/lockout controls.

---

## 2. Security Test Approach & Tools


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
      <td>Black-box</td>
      <td>DAST</td>
      <td>Online credential brute-force / credential stuffing</td>
      <td>Hydra (THC-Hydra)</td>
      <td><a href="https://github.com/vanhauser-thc/thc-hydra">Hydra</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Protocol login brute (SSH/Telnet/FTP)</td>
      <td>Ncrack</td>
      <td><a href="https://nmap.org/ncrack/">Ncrack</a></td>
      <td>Both (IoT heavy)</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Web UI / API fuzzing & automated attack</td>
      <td>Burp Suite (Intruder) / OWASP ZAP</td>
      <td><a href="https://portswigger.net/burp">Burp Suite</a> / <a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Custom login flows & throttling test</td>
      <td>Patator (multi-module brute)</td>
      <td><a href="https://github.com/lanjelot/patator">Patator</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Static review for auth logic & rate-limiting bugs</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Cloud & mobile</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Offline hash cracking (captured hashes)</td>
      <td>Hashcat / John the Ripper</td>
      <td><a href="https://hashcat.net/">Hashcat</a> / <a href="https://www.openwall.com/john/">John the Ripper</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile PIN/credential test & instrumentation</td>
      <td>Frida / Drozer (Android) / TestFlight + MDM (iOS)</td>
      <td><a href="https://frida.re/">Frida</a> / <a href="https://github.com/FSecureLABS/drozer">Drozer</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>IoT default creds & factory password scanning</td>
      <td>Shodan (discovery) + custom scripts</td>
      <td><a href="https://www.shodan.io/">Shodan</a></td>
      <td>IoT</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Detection & monitoring validation</td>
      <td>Zeek / Suricata + ELK / Splunk</td>
      <td><a href="https://www.zeek.org/">Zeek</a> / <a href="https://suricata.io/"> Suricata</a> / <a href="https://www.elastic.co/">Splunk</a></td>
      <td>Cloud / Network</td>
    </tr>
  </tbody>
</table>

---

## 3. Minimal Testbed & Quick Step-by-step

**Preconditions (must):** written authorization, staging environment that mirrors production auth flows (rate limits, DB, captive portals), backups/snapshots, and escalation/kill procedure.

1. **Inventory & threat modelling**

   * Enumerate endpoints that accept credentials (web logins, APIs, device management ports, telnet/SSH, mqtt broker logins, mobile PIN entry flows, OTA agent endpoints). Note account lockout/policy settings.

2. **Baseline & logging**

   * Enable authentication logging, WAF logs, and SIEM ingestion. Record normal failed/successful login rates and typical IP ranges.

3. **Automated credential stuffing (low-rate)**

   * Use a curated test credential list (do not use real stolen credentials) and run Hydra/Patator against staging login endpoints, starting with low request rates to validate rate-limit handling. Monitor for account lockouts and SIEM alerts.

4. **Protocol brute & default credential checks (IoT)**

   * Test device protocols (Telnet/SSH/FTP/HTTP admin) with Ncrack/Hydra and common default credential lists (manufacturer defaults). For discovery use controlled Shodan queries in permitted scope.

5. **Mobile PIN & instrumentation tests**

   * For Android: use Frida or Drozer to instrument and attempt automated PIN entry on test devices or verify lockout thresholds. For iOS use MDM test profiles to verify lockout and wipe policies (iOS blocks brute for PIN via hardware limits).

6. **Offline hash cracking (if hashes available in scope)**

   * If you have database dumps in scope (sanitized/test data), run Hashcat/John with appropriate wordlists and rules to measure password strength and expected compromise time.

7. **Rate-limit & throttling verification**

   * Verify backend enforces exponential backoff, per-account and per-IP throttling, CAPTCHAs after threshold, progressive delays, and account lockout policies (with safe rollback for tests).

8. **Detection validation**

   * Confirm SIEM/WAF/IDS alerts on sudden spike of failed auth attempts, IP reputation hits, many credential fails across many accounts (credential stuffing), or unusual geo-pattern (rapid geolocation changes).

9. **Remediation testing**

   * Verify MFA enrollment/requirement prevents takeover, implement IP reputation blocking, enforce strong password policies and breach-credential checking (haveibeenpwned API or similar), then re-run tests to ensure mitigation.

---

## 4. References

1. Florencio, D., & Herley, C. (2007, May). A large-scale study of web password habits. In *Proceedings of the 16th international conference on World Wide Web* (pp. 657-666).
2. Sequeiros, J. B., Chimuco, F. T., Samaila, M. G., Freire, M. M., & Inácio, P. R. (2020). Attack and system modeling applied to IoT, cloud, and mobile ecosystems: Embedding security by design. *ACM Computing Surveys (CSUR)*, 53(2), 1-32.
5. Bonneau, J., & Preibusch, S. (2010, June). The Password Thicket: Technical and Market Failures in Human Authentication on the Web. In *WEIS*.
