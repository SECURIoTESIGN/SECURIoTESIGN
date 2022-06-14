In order to avoid *XSS, SQLi, CSRF, Session Fixation, Session Hijacking, Access Point Hijacking, Command Injection, Code Injection, Botnet, Malware as a Service, Spoofing, Pharming, Phishing, GPS Spoofing, Rogue Access Point, Cellular Rogue Base Station and SSRF Attacks*, the following security tests should be perform.

<table class="tg">
<thead>
  <tr>
    <th class="tg-amwm" rowspan="2">Test Parameter</th>
    <th class="tg-amwm" rowspan="2">Testing Types</th>
    <th class="tg-amwm" rowspan="2">Testing Analysis</th>
    <th class="tg-amwm" rowspan="2">Method</th>
    <th class="tg-amwm" colspan="3">Tools</th>
  </tr>
  <tr>
    <th class="tg-amwm">Both</th>
    <th class="tg-amwm">Android</th>
    <th class="tg-amwm">iOS</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Authentication&nbsp;&nbsp;&nbsp;and Authorization</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax">OWASP WebScarab, Nikto, <br>Wikto, Paros Proxy, Spike <br>Proxy, OWASP ZAP</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and <br>Authorization, Access Control</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">PenetrationTesting</td>
    <td class="tg-0lax">NMAP and Kali Linux</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Exploit Database Vulnerabilities</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Manual Dynamic <br>Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">SQLite browser</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Xcode, Xcode <br>Command Line Tools</td>
  </tr>
  <tr>
    <td class="tg-0lax">Proper   SSL usage and Insecure <br>TLS Protectio, Use of encryption,</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax">OWASP WebScarab, <br>OWASP ZAP</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Use of encryption</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">API monitor</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Validation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax">Rapid7 Nexpose,  <br>Vulnerability Manager <br>Plus</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Find Bugs</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Bytecode Scanner</td>
    <td class="tg-0lax">Bytecode Scanner, <br>QARK</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Source code analyser</td>
    <td class="tg-0lax">PARASOFT C/C++ TEST, <br>RATS, Clang   Code Analyze, <br>Androbug</td>
    <td class="tg-0lax">Angr</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Binary code Scanner</td>
    <td class="tg-0lax">BugScan of LogicLab Co., <br>FxCop   BugScam</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input&nbsp;&nbsp;&nbsp;validation of user SID</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Manual Dynamic Analysis</td>
    <td class="tg-0lax">Checking input fields in GUI</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>