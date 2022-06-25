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
    <td class="tg-0lax"><a href="https://github.com/OWASP/OWASP-WebScarab">OWASP WebScarab</a>, <a href="https://github.com/sullo/nikto">Nikto</a>, <a href="https://github.com/sensepost/wikto">Wikto</a>, <a href="https://www.kali.org/tools/paros/">Paros Proxy</a>, <a href="https://www.spikeproxy.com/">Spike Proxy</a>, <br><a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and <br>Authorization, Access Control</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">PenetrationTesting</td>
    <td class="tg-0lax"><a href="https://nmap.org/">NMAP</a>, <a href="https://www.kali.org/">Kali Linux</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Exploit Database Vulnerabilities</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Manual Dynamic <br>Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://sqlitebrowser.org/">SQLite browser</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://developer.apple.com/xcode/">Xcode</a>, <a href="https://mac.install.guide/commandlinetools/index.html">Xcode <br>Command Line Tools</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Proper   SSL usage and Insecure <br>TLS Protectio, Use of encryption,</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://github.com/OWASP/OWASP-WebScarab">OWASP WebScarab</a>, <br><a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Use of encryption</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security#8-api-monitor---android-only">API monitor</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Validation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax"><a href="https://www.rapid7.com/products/nexpose/">Rapid7 Nexpose</a>,  <br><a href="https://www.manageengine.com/br/vulnerability-management/">Vulnerability Manager <br>Plus</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Find Bugs</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Bytecode Scanner</td>
    <td class="tg-0lax"><a href="https://github.com/AnthonyCalandra/bytecode-scanner">bytecode-scanner</a>, <br><a href="https://github.com/linkedin/qark/">QARK</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Source code analyser</td>
    <td class="tg-0lax"><a href="https://www.parasoft.com/products/parasoft-c-ctest/">PARASOFT C/C++ TEST</a>, <a href="https://security.web.cern.ch/recommendations/en/codetools/rats.shtml/">RATS</a>, <a href="https://clang-analyzer.llvm.org/scan-build.html">Clang Code Analyze</a></td> 
    <td class="tg-0lax"><a href="https://docs.angr.io/introductory-errata/install">Angr</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Binary code Scanner</td>
    <td class="tg-0lax"><a href="https://blackberry.qnx.com/en/software-solutions/blackberry-jarvis">BlackBerry Jarvis</a>, <br><a href="https://www.grammatech.com/codesonar-sast-binary">CodeSonar for Binaries</a>, <a href="https://sourceforge.net/projects/bugscam/">BugScam</a></td>
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
