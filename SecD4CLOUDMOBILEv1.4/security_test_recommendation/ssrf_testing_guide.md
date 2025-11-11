# Security Testing for Server-Side Request Forgery

---

## 1. Overview

Server-Side Request Forgery (SSRF) lets an attacker coerce a server to make network requests it should not (internal services, cloud metadata, IoT endpoints), which is especially dangerous in cloud environments (IMDS / instance metadata).

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
      <td>Automated SSRF fuzzing</td>
      <td>SSRFmap</td>
      <td><a href="https://github.com/swisskyrepo/SSRFmap">SSRFmap</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Blind SSRF detection (out-of-band)</td>
      <td>Burp Collaborator / Interactsh</td>
      <td><a href="https://portswigger.net/">Burp Collaborator</a> / <a href="https://github.com/projectdiscovery/interactsh">Interactsh</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Manual request inspection & manipulation</td>
      <td>Burp Suite / OWASP ZAP</td>
      <td><a href="https://portswigger.net/burp">Burp Suite</a> / <a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Code review for unsafe URL handling</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Cloud & backend</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Internal port / service discovery via SSRF</td>
      <td>Custom HTTP probes + timing/response analysis (curl, httpx)</td>
      <td><a href="https://github.com/projectdiscovery/httpx">httpx</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST/DAST</td>
      <td>Cloud metadata / IMDS safety checks</td>
      <td>Cloud vendor docs & IMDS probes</td>
      <td>See AWS / Azure IMDS docs</td>
      <td>Cloud</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Network detection / logging</td>
      <td>Zeek / ELK / Splunk</td>
      <td><a href="https://www.zeek.org/">Zeek</a> / <a href="https://www.elastic.co/">ELK</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 3. Minimal Testbed & Quick Procedure

1. **Authorization & isolation** &mdash; run all tests in staging / isolated VLAN; snapshot systems and get written approval.
2. **Inventory** &mdash; list endpoints that accept external URLs or hostnames: image fetchers, webhooks, URL previews, redirects, server-side fetch endpoints on mobile/gateways.
3. **Baseline logging** &mdash; enable HTTP logs, backend request logs, and cloud audit logs; configure an Interactsh/Burp Collaborator domain to catch OOB callbacks. 
4. **Automated fuzz** &mdash; run SSRFmap (or similar) against parameters identified as URL/host inputs to detect open fetch behaviors and common bypasses. 
5. **Blind SSRF detection** &mdash; inject Collaborator / Interactsh payloads and monitor for DNS/HTTP/SMTP callbacks (use for blind SSRF where response not returned to user). 
6. **Metadata & internal service checks** &mdash; probe for cloud metadata endpoints (e.g., AWS IMDS v1/v2), internal hosts (`localhost`, `169.254.169.254`, `169.254.169.254/latest/meta-data/`), and common internal ports/services via SSRF to confirm exposure (do not request sensitive data unless authorized). 
7. **Manual exploit & bypass testing** &mdash; use Burp Suite/ZAP to try different payload encodings, alternate protocols (file://, gopher://, ftp://), DNS rebinding techniques and filter bypasses. 
8. **Detection validation** &mdash; ensure SIEM detects unusual outbound internal requests, repeated parametrized fetches, or OOB callbacks; log findings and assign severity.
9. **Remediate & retest** &mdash; apply allow-lists, require URL validation, enforce network egress controls, enforce IMDS v2 and metadata access restrictions, and retest. 

---

## 4. References

1. Wang, E., Chen, J., Xie, W., Wang, C., Gao, Y., Wang, Z., ... & Wang, B. (2024, May). Where urls become weapons: Automated discovery of ssrf vulnerabilities in web applications. In 2024 IEEE Symposium on Security and Privacy (SP) (pp. 239-257). IEEE.
2. Altulaihan, E. A., Alismail, A., & Frikha, M. (2023). A survey on web application penetration testing. Electronics, 12(5), 1229.
3. Luo, H. (2019, July). SSRF vulnerability attack and prevention based on php. In 2019 International Conference on Communications, Information System and Computer Engineering (CISCE) (pp. 469-472). IEEE.
4. Jabiyev, B., Mirzaei, O., Kharraz, A., & Kirda, E. (2021, March). Preventing server-side request forgery attacks. In Proceedings of the 36th Annual ACM Symposium on Applied Computing (pp. 1626-1635).