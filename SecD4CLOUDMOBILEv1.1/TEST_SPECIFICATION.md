# Final Security Test Specification and Tools Report  

|                           |                                                              |  
|  :--------                |  :---------                                                  |  
|  Mobile Plataform         |  Hybrid Application                                          |  
|  Application domain type  |  m-Payment                                                   |  
|  Authentication           |  Yes                                                         |  
|  Authentication schemes   |  Biometric-based authentication ; Factors-based authentication ; ID-based authentication|  
|  Has DB                   |  Yes                                                         |  
|  Type of data storage     |  SQL                                                         |  
|  Which DB                 |  MySQL                                                       |  
|  Type of data stored      |  Personal Information ; Confidential Data ; Critical Data    |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  Will be an administrator that will register the users       |  
|  Programming Languages    |  HTML5 ; Javascript ; PHP                                    |  
|  Input Forms              |  Yes                                                         |  
|  Upload Files             |  No                                                          |  
|  The system has logs      |  Yes                                                         |  
|  The system has regular updates|  Yes                                                         |  
|  The system has third-party|  No                                                          |  
|  System Cloud Environments|  Private Cloud                                               |  
|  Hardware Specification   |  Yes                                                         |  
|  HW Authentication        |  Basic Authentication (user/pass)                            |  
|  HW Wireless Tech         |  3G ; 4G/LTE ; 5G ; Bluetooth  ; Wi-Fi  ; GPS  ; NFC         |  
|  Data Center Phisical Access|  Yes                                                         |  



In order to avoid or prevent *SQLi, XSS, CSRF, SSRF, Command Injection, Code Injection* attacks, the following security tests should be performed.

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
    <td class="tg-0lax">Web Server <br>connection</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Manual Dynamic <br>Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax">ITR and OWASP WebScarab, <br>OWASP ZAP, Paros</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Validation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax">Snoopwall Privacy App, Clueful,&nbsp;&nbsp;&nbsp;AVG Antivirus Security</td>
    <td class="tg-0lax">Recap vulnerability scanner</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dynamic binary&nbsp;&nbsp;&nbsp;analysis</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Introspy-Android</td>
    <td class="tg-0lax">Introspy-iOS</td>
  </tr>
</tbody>
</table>


In order to avoid or prevent *Malware as a Service, Malicious QR Code, Botnet, Spoofing and Eavesdroping, NFC Payment Replay, Bynzantine, Bluesnarfing, Bluejacking* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Malware   and Privacy Scanners </td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax">Snoopwall Privacy App, <br>Clueful,   AVG Antivirus <br>Security</td>
    <td class="tg-0lax">Recap vulnerability <br>scanner </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data&nbsp;&nbsp;&nbsp;Leakage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax">Wireshark</td>
    <td class="tg-0lax">tPacketCapturepro</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and Authorization, <br>Use of Encryption</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">NFCSpy</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Encryption,   Authentication and <br>Authorization, Web Server <br>Authentication, Access Control</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">Kali Linux, hcitool</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>

In order to avoid or prevent *Bypassing Physical Security, Physical Theft and VM Migration attacks*, the following security tests should be performed.

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
    <td class="tg-0lax">Data leakage&nbsp;&nbsp;&nbsp;and Breach</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax">BlackBag Blacklight, Encase&nbsp;&nbsp;&nbsp;Forensics</td>
    <td class="tg-0lax">AndroGuard, Drozer, FindBugs,&nbsp;&nbsp;&nbsp;Andriller</td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>

In order to avoid or prevent *Malware as a Service, Malicious QR Code, Botnets, Spoofing, Eavesdroping, NFC Payment Replay, Bynzantine, Bluesnarfing, Bluejacking, Side-Channel, Flooding attacks*, the following security tests should be performed.


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
    <td class="tg-0lax">Malware   and Privacy Scanners </td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax">Snoopwall Privacy App, <br>Clueful,   AVG Antivirus <br>Security</td>
    <td class="tg-0lax">Recap vulnerability <br>scanner </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data&nbsp;&nbsp;&nbsp;Leakage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax">Wireshark</td>
    <td class="tg-0lax">tPacketCapturepro</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and Authorization, <br>Use of Encryption</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">NFCSpy</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Encryption,   Authentication and <br>Authorization, Web Server <br>Authentication, Access Control</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">Kali Linux, hcitool</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Use of   encryption, Secure backup, <br>logging and Insecure Data Storage</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax">Slueth Kit and <br>Autopsy Browser</td>
    <td class="tg-0lax">AndroGuard, Drozer, <br>apktool,   Amandroid</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dynamic&nbsp;&nbsp;&nbsp;binary analysis: debugging, tracing</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Hybrid Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax">RMS</td>
    <td class="tg-0lax">Drozer, Sieve</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax">iOSbackup</td>
  </tr>
</tbody>
</table>

In order to avoid or prevent *Spoofing, Eavesdropping, Sniffing, Botnets, MiTM, Flooding, Reverse Enginnering attacks*, the following security tests should be performed.


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
    <td class="tg-0lax">Mobile   decryption, <br>unpacking &amp; conversion</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">Ghidra</td>
    <td class="tg-0lax">Dex2jar, JD-GUI, <br>Dextra</td>
    <td class="tg-0lax">Clutch</td>
  </tr>
  <tr>
    <td class="tg-0lax">Mobile   decryption, <br>unpacking &amp; conversion</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">MobSF</td>
    <td class="tg-0lax">APKEnum</td>
    <td class="tg-0lax">Damn Vulnerable <br>iOS App</td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,   <br>logging and Insecure <br>Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">adb</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Static binary   analysis: <br>disassembly, decompilation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Manual (Reversed) <br>Code Review</td>
    <td class="tg-0lax">r2ghidra-dec,r2frida, <br>Radare2</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Hooper</td>
  </tr>
</tbody>
</table>

In order to avoid *Malware as a Service, Eavesdropping, Botnets* attacks, the following security tests should be perform.


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
    <td class="tg-0lax">Dynamic&nbsp;&nbsp;&nbsp;binary analysis: debugging, tracing</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Hybrid Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax">RMS</td>
    <td class="tg-0lax">Drozer, Sieve</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax">iOSbackup</td>
  </tr>
</tbody>
</table>

In order to avoid or prevent *Phishing, Botnet, Malware as a Service* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Add-ons</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Addons Detector</td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>

In order to avoid or prevent *Spoofing, Eavesdrooping, Botnets, Flooding* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Web Server&nbsp;&nbsp;&nbsp;Authentication</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax">Wireshark</td>
    <td class="tg-0lax">tPacketCapturepro</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">DoS and DDoS Attacks</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis </td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">Cydia Substrate</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Cycript</td>
  </tr>
</tbody>
</table>

In order to avoid *SQLi, Command Injection, Session Hijacking, Botnets, AP Hijacking, Brute Force, Phishing, Spoofing, MiTM, Buffer Overflow, Sniffing, CSRF, VM Migration* attacks, the following security tests should be perform.

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
    <td class="tg-0lax">Dynamic binary&nbsp;&nbsp;&nbsp;analysis</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Introspy-Android</td>
    <td class="tg-0lax">Introspy-iOS</td>
  </tr>
</tbody>
</table>