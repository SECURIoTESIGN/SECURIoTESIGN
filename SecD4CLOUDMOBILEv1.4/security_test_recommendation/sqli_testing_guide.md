# Security Testing for SQL Injection

## 1. Overview

A SQL Injection attack is a code injection technique that allows attackers to manipulate a database through insecure user input. Security testing is essential to detect and prevent these vulnerabilities, protecting sensitive data and ensuring application integrity.

---

## 2. Security Test & Approach

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
      <td>Automated SQLi discovery & exploitation</td>
      <td>sqlmap</td>
      <td><a href="https://sqlmap.org/">sqlmap</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Intercept & manipulate requests (manual testing)</td>
      <td>Burp Suite (Intruder, Repeater)</td>
      <td><a href="https://portswigger.net/burp">Burp Suite</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Automated web scanning (includes SQLi checks)</td>
      <td>OWASP ZAP</td>
      <td><a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Web app vulnerability discovery (fuzzing)</td>
      <td>w3af / nikto</td>
      <td><a href="https://w3af.org/">w3af</a> / <a href="https://cirt.net/Nikto2">nikto</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Source review for unsafe DB calls / concatenation</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</td>
      <td>Cloud & mobile backend</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>API fuzzing & parameter testing</td>
      <td>Postman + Fuzzers (Boomerang, RESTler)</td>
      <td><a href="https://www.postman.com/">Postman</a> / <a href="https://github.com/microsoft/restler-fuzzer">Fuzzers</a></td>
      <td>Both (APIs)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Database & query monitoring (detect abnormal queries)</td>
      <td>DB audit logs / SIEM (Elastic/Splunk)</td>
      <td><a href="https://www.elastic.co/">DB audit logs</a> / <a href="https://www.splunk.com/">SIEM</a></td>
      <td>Cloud</td>
    </tr>
  </tbody>
</table>

---

## 3. Minimal Testbed & Quick Steps

1. **Scope & inventory** &mdash; list endpoints that accept input: web forms, API params, MQTT/CoAP fields forwarded to DB, mobile app inputs, IoT gateway admin interfaces.
2. **Backup & isolate** &mdash; run tests in staging or isolated environment; snapshot DBs and apps.
3. **Baseline capture** &mdash; enable DB auditing (slow query log, general log) and capture normal traffic.
4. **Automated scan** &mdash; run `sqlmap` and ZAP against targets to find obvious SQLi. Use authenticated scans for API endpoints (bearer tokens / session cookies).
5. **Manual verification** &mdash; use Burp Suite (Repeater/Intruder) to craft payloads, test blind/time-based SQLi, boolean blind, and stacked queries. Observe DB/log responses & side effects.
6. **API/mobile checks** &mdash; fuzz API parameters (Postman + RESTler/Boomerang) and test mobile app inputs (intercept with Burp/mitmproxy or instrument mobile app).
7. **DB & app log review** &mdash; correlate suspicious requests with DB logs; verify whether parameterized queries are used or unsafe concatenation.
8. **Fix & retest** &mdash; apply prepared statements/ORM parameterization, input validation, least privilege DB accounts, and retest. Use WAF as compensating control if immediate code fixes are infeasible.

---

## 4. References

1. Alsalamah, M., Alwabli, H., Alqwifli, H., & Ibrahim, D. M. (2021). A review study on SQL injection attacks, prevention, and detection.
2. Paul, A., Sharma, V., & Olukoya, O. (2024). SQL injection attack: Detection, prioritization & prevention. *Journal of Information Security and Applications*, 85, 103871.
3. Ojagbule, O., Wimmer, H., & Haddad, R. J. (2018, April). Vulnerability analysis of content management systems to SQL injection using SQLMAP. *In SoutheastCon 2018* (pp. 1-7). IEEE.
4. Bouafia, R., Benbrahim, H., & Amine, A. (2023, October). Automatic protection of web applications against sql injections: An approach based on acunetix, burp suite and sqlmap. In *2023 9th International Conference on Optimization and Applications (ICOA)* (pp. 1-6). IEEE.
5. Liu, M., Li, K., & Chen, T. (2020, July). DeepSQLi: Deep semantic learning for testing SQL injection. *In Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis* (pp. 286-297).