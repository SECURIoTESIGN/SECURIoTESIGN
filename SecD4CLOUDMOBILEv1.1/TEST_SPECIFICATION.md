# Final Security Test Specification and Tools Report  

|                           |                                                              |  
|  :--------                |  :---------                                                  |  
|  Mobile Plataform         |  Web Application                                             |  
|  Application domain type  |  m-Health                                                    |  
|  Authentication           |  Yes                                                         |  
|  Authentication schemes   |  Biometric-based authentication ; Factors-based authentication|  
|  Has DB                   |  Yes                                                         |  
|  Type of data storage     |  SQL                                                         |  
|  Which DB                 |  MySQL                                                       |  
|  Type of data stored      |  Personal Information ; Confidential Data ; Critical Data    |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  The users will register themselves                          |  
|  Programming Languages    |  HTML5 ; PHP ; Javascript                                    |  
|  Input Forms              |  Yes                                                         |  
|  Upload Files             |  Yes                                                         |  
|  The system has logs      |  Yes                                                         |  
|  The system has regular updates|  Yes                                                         |  
|  The system has third-party|  Yes                                                         |  
|  System Cloud Environments|  Private Cloud                                               |  
|  Hardware Specification   |  Yes                                                         |  
|  HW Authentication        |  Basic Authentication (user/pass)                            |  
|  HW Wireless Tech         |  3G ; 4G/LTE ; 5G ; Wi-Fi  ; GPS                             |  
|  Data Center Phisical Access|  Yes                                                         |  




In order to avoid or prevent *SQLi, XSS, Spoofing and CSRF attacks*, the following security tests should be performed.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Test Parameter</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Types</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Methods</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Tools</span></th>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Android</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">iOS</span></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Authentication and Authorization </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamic analysis via Vulnerability Scanner </td>
    <td class="tg-0lax">OWASP WebScarab, OWASP Berretta, Nikto, Wikto, Paros Proxy, Spike Proxy, EOR, Pantera</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Access Control </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Test</td>
    <td class="tg-0lax">NMAP and Kali Linux </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>



In order to avoid or prevent *Botnet, Spoofing and Sniffing attacks*, the following security tests should be performed.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Test Parameter</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Types</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Methods</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Tools</span></th>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Android</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">iOS</span></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Exploit Database Vulnerabilities </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Manual Dinamic Analysis via Penetration Test </td>
    <td class="tg-0lax">SQLite browser </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Xcode </td>
  </tr>
  <tr>
    <td class="tg-0lax">Proper SSL usage and Use of encryption </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0lax">Dinamic Analysis via Proxies</td>
    <td class="tg-0lax">WebScarab </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Database frangibility scanner </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamic Analisys via Vulnerability Scanner </td>
    <td class="tg-0lax">Database Scanner of Internet Security Systems Co. and MetaCortex </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Find Bugs </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Bytecode Scanner</td>
    <td class="tg-0lax">FindBugs, BugScan of LogicLab Co. </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via source code Analyser </td>
    <td class="tg-0lax">C++Test, RATS, C Code Analyzer(CCA) </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Binary code Scanner </td>
    <td class="tg-0lax">BugScan of Logi- cLab Co. and Fx- Cop;BugScam </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input validation of user SID </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Manual Dinamic Analysis Checking input fields in GUI</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>

  <tr>
    <td class="tg-0lax">Runtime manipulation: code injection, patching </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span></td>
    <td class="tg-0lax">Static Analysis via Test Penetration </td>
    <td class="tg-0lax">Cydia Substrate </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Cycript </td>
  </tr>
</tbody>
</table>

  





In order to avoid or prevent *Malicious Insider and VM-Migration attacks*, the following security tests should be performed.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Test Parameter</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Types</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Methods</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Tools</span></th>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Android</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">iOS</span></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Input validation </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Static Analysis via Forensic Mobile</td>
    <td class="tg-0lax">Slueth Kit+Autopsy Browser</td>
    <td class="tg-0lax">AndroGuard, Drozer, apktool, Amandroid </td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>



In order to avoid or prevent *Malware injection and Side-channel Attacks*, the following security tests should be performed.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Test Parameter</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Types</span></th>
    <th class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Methods</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Tools</span></th>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Android</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">iOS</span></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Debug flag </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Forensic Mobile </td>
    <td class="tg-0lax">BlackBag Blacklight, Encase forensics</td>
    <td class="tg-0lax">AndroGuard, Drozer, FindBugs, Andriller </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Content providers</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Forensic Mobile</td>
    <td class="tg-0lax">Slueth Kit+Autopsy Browser</td>
    <td class="tg-0lax">AndroGuard, Drozer, apktool </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Code quality </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Static Analysis via Byte- code Scanner</span></td>
    <td class="tg-0lax">FindBugs, BugScan of LogicLab Co. </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via source code Analyser </td>
    <td class="tg-0lax">C++Test, RATS, C Code Analyzer(CCA) </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via source code Analyser </td>
    <td class="tg-0lax">BugScan of LogicLab Co. and Fx- Cop, BugScam </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">class-dump-z </td>
  </tr>
</tbody>
</table>



In order to avoid or prevent *physical attacks*, the following security tests should be performed.

<table class="tg">
  <tr>
    <th class="tg-yla0" rowspan="2">Test Parameter</th>
    <th class="tg-0lax" rowspan="2"><br><span style="font-weight:bold">Test Approach</span></th>
    <th class="tg-yla0" rowspan="2">Test Method</th>
    <th class="tg-wa1i" colspan="3">Tools</th>
  </tr>
  <tr>
    <td class="tg-yla0">Both</td>
    <td class="tg-yla0">Android</td>
    <td class="tg-yla0">iOS</td>
  </tr>
  <tr>
    <td class="tg-cly1">Debug flag, Content providers, Code quality</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-cly1">Static Analysis via Forensic Mobile</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1">AndroGuard, Drozer, FindBugs</td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-cly1">Leak, Breach and data Loss</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-cly1">Manual Dinamic Analysis Checking input fields from device and GUI</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
</table>