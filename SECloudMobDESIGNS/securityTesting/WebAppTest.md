
In order to avoid or prevent *SQLi, XMLi, XSS, CSRF and Buffer Overflows attacks*, the following security tests should be performed.

<table class="tg">
  <tr>
    <th class="tg-yla0">Test Parameter</th>
    <th class="tg-0lax"><br><span style="font-weight:bold">Test Approach</span></th>
    <th class="tg-yla0">Test Method</th>
    <th class="tg-wa1i">Tools</th>
  </tr>
  <tr>
    <td class="tg-cly1">Authentication and Authorization</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-cly1">Dinamic Analysis via Vulnerability Scanner</td>
    <td class="tg-cly1">OWASP WebScarab, OWASPBerretta, OWASP ZAP, Nikto, Wikto, Paros Proxy, Spike Proxy, EOR, Pantera</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">Access Control</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Test</td>
    <td class="tg-0lax">NMAP and Kali Linux</td>
  </tr>
  <tr>
    <td class="tg-0lax">White Box</td>
    <td class="tg-cly1">Manual Dinamic Analysis via Attack Injection</td>
    <td class="tg-cly1">Wireshark, , ettercap, sslsniff</td>
  </tr>
  <tr>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Dinamic Analysis via Fuzzers</td>
    <td class="tg-0lax">SPIKE</td>
  </tr>
  <tr>
    <td class="tg-0lax">Proper SSL usage, Use of encryption</td>
    <td class="tg-0lax">Black |Box</td>
    <td class="tg-0lax">Dinamic Analysis via Proxies</td>
    <td class="tg-0lax">WebScarab, OWASP ZAP</td>
  </tr>
  <tr>
    <td class="tg-0lax">Database frangibility scanner</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Dinamic Analisys via Vulnerability Scanner</td>
    <td class="tg-0lax">Database Scanner of Internet Security Systems Co. and MetaCortex, sqlmap</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">Find Bugs or Quality Code</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via Bytecode Scanner</td>
    <td class="tg-0lax">FindBugs, BugScan of LogicLab Co.</td>
  </tr>
  <tr>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via source code Analyser</td>
    <td class="tg-0lax">C++Test, RATS, C Code nalyzer(CCA)</td>
  </tr>
  <tr>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via Binary code Scanner</td>
    <td class="tg-0lax">BugScan of LogicLab Co. and FxCop;BugScam</td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Validation of User SID</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Manual Dinamic Analysis Checking input fields in GUI</td>
    <td class="tg-0lax"></td>
  </tr>
</table>
