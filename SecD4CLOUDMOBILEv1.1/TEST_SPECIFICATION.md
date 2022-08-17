# Final Security Test Specification and Tools Report  

|                           |                                                              |  
|  :--------                |  :---------                                                  |  
<<<<<<< HEAD
|  Mobile Plataform         |  IoT System                                                  |  
|  Application domain type  |  Smart Agriculture                                           |  
=======
|  Mobile Plataform         |  Hybrid Application                                          |  
|  Application domain type  |  m-Health                                                    |  
>>>>>>> 756a6f658e94ba3c11c4cd25afbb448e80592558
|  Authentication           |  Yes                                                         |  
|  Authentication schemes   |  Factors-based authentication ; ID-based authentication      |  
|  Has DB                   |  Yes                                                         |  
<<<<<<< HEAD
|  Type of data storage     |  Local Storage                                               |  
|  Which DB                 |                                                              |  
|  Type of data stored      |  Personal Information ; Confidential Data                    |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  The users will register themselves                          |  
|  Programming Languages    |  C/C++                                                       |  
|  Input Forms              |  No                                                          |  
|  Upload Files             |  No                                                          |  
=======
|  Type of data storage     |  SQL (Relational Database)                                   |  
|  Which DB                 |  SQLite                                                      |  
|  Type of data stored      |  Critical Data                                               |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  Will be an administrator that will register the users       |  
|  Programming Languages    |  HTML5                                                       |  
|  Input Forms              |  Yes                                                         |  
|  Upload Files             |  Yes                                                         |  
>>>>>>> 756a6f658e94ba3c11c4cd25afbb448e80592558
|  The system has logs      |  Yes                                                         |  
|  The system has regular updates|  Yes                                                         |  
|  The system has third-party|  Yes                                                         |  
|  System Cloud Environments|  Public Cloud                                                |  
|  Hardware Specification   |  Yes                                                         |  
|  HW Authentication        |  Basic Authentication (user/pass)                            |  
<<<<<<< HEAD
|  HW Wireless Tech         |  5G ; 3G ; 4G/LTE ; Bluetooth  ; Wi-Fi                       |  
=======
|  HW Wireless Tech         |  3G ; 4G/LTE ; 5G ; Wi-Fi  ; GPS  ; NFC                      |  
>>>>>>> 756a6f658e94ba3c11c4cd25afbb448e80592558
|  Data Center Phisical Access|  Yes                                                         |  

In order to avoid or prevent *DoS Jamming, Wi-Fi Jamming, Orbital Jamming, GPS Jamming, Flooding* attacks, the following security tests should be performed.



<table class="tg">
<thead>
  <tr>
    <th class="tg-amwm" rowspan="2">Test Parameter</th>
    <th class="tg-amwm" rowspan="2">Testing <br>Types</th>
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
<<<<<<< HEAD
    <td class="tg-0lax">Add-ons </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Forensic Mobile </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Addons Detector </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">DoS, DDoS Attacks </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Test </td>
    <td class="tg-0lax">NMAP, SlowBot Net, MetaSploit, LOlC and Kali Linux </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>





In order to avoid or prevent *Botnet, DoS, DDoS, Eavesdropping, Phishing, MITM, Spoofing and Sniffing Attacks*, the following security tests should be performed.

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
    <td class="tg-0lax">Mobile decryption, unpacking &amp; conversion </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Test Penetration </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Dex2jar </td>
    <td class="tg-0lax">Clutch </td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup and logging </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamica Analysis via Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">adb </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data leakage and Breach </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamic analysis via Proxies </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Wireshark</span></td>
    <td class="tg-0lax">tPacketCapturepro, AFWall+, </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Testing</td>
    <td class="tg-0lax">VASTO </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Dnamic Analysis via Stressing Testing (fuzzing) </td>
    <td class="tg-0lax">Webfuzz, SPI Fuzzer, Wfuzz </td>
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
=======
    <td class="tg-0lax">DoS and DDoS <br>Attacks</td>
>>>>>>> 756a6f658e94ba3c11c4cd25afbb448e80592558
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://nmap.org/book/man.html">NMAP</a>, <a href="https://www.sciencedirect.com/science/article/pii/S0167404816300086">SlowBot Net</a>, <a href="https://docs.rapid7.com/metasploit/">MetaSploit</a>, <a href="https://github.com/NewEraCracker/LOIC">LOIC</a>, <a href="https://www.kali.org/docs/introduction/">Kali Linux</a></td> 
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Web Server&nbsp;&nbsp;&nbsp;Authentication</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">DoS and DDoS Attacks</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis </td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="http://www.cydiasubstrate.com/">Cydia Substrate</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="http://www.cycript.org/">Cycript</a></td>
  </tr>
</tbody>
</table>




In order to avoid or prevent *Malicious Insider, Sniffing, MiTM, Eavesdropping* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Data leakage and Breach</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a>, <a href="https://github.com/ukanth/afwall">AFWall+</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis </td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.securenetwork.it/docs/talks/2010-10_BlackHat-USA-2010_Virtually-Pwned.pdf">VASTO</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Stressing Testing (fuzzing)</td>
    <td class="tg-0lax"><a href="https://github.com/ovanr/webFuzz">Webfuzz</a>, <a href="https://github.com/xmendez/wfuzz">Wfuzz</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax"><a href="https://www.acunetix.com/support/">Acunetix</a>, <a href="http://docs.w3af.org/en/latest/basic-ui.html">W3af</a>, <a href="https://github.com/sullo/nikto">Nikto</a>,&nbsp;&nbsp;&nbsp;<a href="https://www.microfocus.com/media/data-sheet/webinspect_automated_dynamic_application_security_testing_ds.pdf">Fortify WebInspect</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.tcpdump.org/">TCPDump</a>, <a href="https://www.wireshark.org/">Wireshark</a</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/adb">adb</a></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>


In order to avoid *MiTM, Eavesdropping, Side-Channel, VM Escape,  Wi-Fi SSID Tracking, Rogue Access Point, Cellular Rogue Base Station, Sniffing, Cryptanalysis, Audit Log Manipulation Attacks, Byzantine, On-Off, Brute Force*, the following security tests should be perform.
<table class="tg">
	<thead>
		<tr>
        <th class="tg-amwm" rowspan="2"><br><br>Test Parameter</th>
        <th class="tg-1wig" rowspan="2"><br><br>Testing <br>Types</th>
        <th class="tg-1wig" rowspan="2"><br><br>Testing Analysis</th>
        <th class="tg-amwm" rowspan="2"><br><br>Method</th>
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
        <td class="tg-0lax">Proper SSL usage and <br>Insecure TLS Protection, <br>Use of encryption</td>
        <td class="tg-0lax">White Box</td>
        <td class="tg-0lax">Static analysis</td>
        <td class="tg-0lax">Forensic Mobile</td>
			<td class="tg-0lax"><a href="https://www.msab.com/product/xry-extract/">XRY</a>, <a ></a><a href="https://cellebrite.com/en/ufed/">UFED Touch</a>, <a href="https://www.openssl.org/">OpenSSL</a></td>
        <td class="tg-0lax"><a href="https://github.com/androguard/androguard">AndroGuard</a>, <a href="https://github.com/sfahl/mallodroid">MalloDroid</a>, <a href="https://github.com/iBotPeaches/Apktool">apktool</a>, <a href="https://dl.acm.org/doi/10.1145/3183575">Amandroid</a></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Interception of   network</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Hybrid</td>
        <td class="tg-0lax">Penetration Testing</td>
        <td class="tg-0lax"><a href="https://portswigger.net/burp">Burp Suite</a>, <a href="https://www.wireshark.org/">Wireshark</a>, <br><a href="https://github.com/bettercap/bettercap">bettercap</a></td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Interception of network</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxy</td>
        <td class="tg-0lax"><a href="https://github.com/jrmdev/mitm_relay">mitm-relay</a>, <a href="https://www.kali.org/docs/introduction/">Kali Linux</a>, <a href="https://portswigger.net/burp">Burp Suite</a></td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Poor use of   certificate <br>parameters</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax"><a href="https://nmap.org/">NMAP</a>, <a href="https://www.tenable.com/products/nessus">Nessus</a>,  <br> <a href="https://www.metasploit.com/">Metasploit Framework</a></td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Data leakage</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Dynamic analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
        <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a>, <a href="https://github.com/ukanth/afwall">AFWall+</a></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Secure backup,   logging <br>and Insecure Data Storage</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxies, Penetration <br>Testing</td>
        <td class="tg-0lax"><a href="https://frida.re/">Frida</a></td>
        <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/adb">adb</a></td>
        <td class="tg-0lax"><a href="https://www.passfab.net/products/iphone-backup-unlocker.html?gclid=CjwKCAjwwdWVBhA4EiwAjcYJEIEe_MT87RuDw5L6Pl-frG5MrdUTW2mbj61faoJpXIEWjB7MCSQfXxoCXV8QAvD_BwE">PassFab iPhone <br> Backup Unlocker</a></td>
      </tr>
      <tr>
        <td class="tg-0lax">Secure backup,   <br>logging and <br>Insecure Data <br>Storage</td>
        <td class="tg-0lax">White Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Mobile Forensic</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/logcat">Logcat</a></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Web Server <br>connection</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Manual Dynamic Analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax"><a href="https://github.com/OWASP/OWASP-WebScarab">OWASP WebScarab</a>, <br><a href="https://www.zaproxy.org/">OWASP ZAP</a>,   <a href="https://www.kali.org/tools/paros/">Paros</a></td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Web Server Authentication</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a>, <a href="https://github.com/CERTCC/tapioca">CERT Tapioca</a></td>
        <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
      <td class="tg-0lax">Dynamic binary analysis</td>
      <td class="tg-0lax">Black Box</td>
      <td class="tg-0lax">Dinamic Analysis</td>
      <td class="tg-0lax">Penetration Testing</td>
      <td class="tg-0lax"></td>
      <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-Android">Introspy-Android</a></td>
      <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-iOS">Introspy-iOS</a></td>
      </tr>
	</tbody>
</table>


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
    <td class="tg-0lax"><a href="https://github.com/OWASP/OWASP-WebScarab">OWASP WebScarab</a>, <br><a href="https://www.zaproxy.org/">OWASP ZAP</a>,   <a href="https://www.kali.org/tools/paros/">Paros</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Validation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.bitdefender.com/solutions/total-security.html">Bitdefender</a>, <a href="https://pt.norton.com/ps/3up_norton360_ns_nd_np_Reading_tw_nb.html?nortoncountry=pt&om_sem_cid=hho_sem_sy:pt:ggl:pt:e:br:kw0000004480:465830486375:c:google:195269073:16491667593:kwd-15050890&nortoncountry=PT&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEDbwnLOm9cCLQw62JluesRsIz13dGLcGR3g22Rl1TpjQLRqybwbYHRoCbTMQAvD_BwE&gclsrc=aw.ds">Norton</a>, <a href="https://www.mcafee.com/consumer/pt-pt/landing-page/direct/sem/mtp-family/desktop/brand-ad.html?csrc=google&csrcl2=brand&cctype=[PT-PT][Search][Brand]McAfee&ccstype=&ccoe=direct&ccoel2=sem&affid=1485&culture=PT-PT&utm_source=google&utm_medium=paidsearch&utm_campaign=[PT-PT][Search][Brand]McAfee&utm_content=[brand][exact]mcafee&utm_term=mcafee&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEB9Z6QxypEvqzc3LCPYisQUsFVCnowFSUXK73SOjadoDZa8H8jkVLBoC_hsQAvD_BwE">McAfee</a>, <a href="https://www.kaspersky.co.uk/home-security?ignoreredirects=true">Kaspersky</a></td>
    <td class="tg-0lax"><a href="http://sanddroid.xjtu.edu.cn/">SandDroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dynamic binary&nbsp;&nbsp;&nbsp;analysis</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-Android">Introspy-Android</a></td>
      <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-iOS">Introspy-iOS</a></td>
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
    <td class="tg-0lax"><a href="https://www.bitdefender.com/solutions/total-security.html">Bitdefender</a>, <a href="https://pt.norton.com/ps/3up_norton360_ns_nd_np_Reading_tw_nb.html?nortoncountry=pt&om_sem_cid=hho_sem_sy:pt:ggl:pt:e:br:kw0000004480:465830486375:c:google:195269073:16491667593:kwd-15050890&nortoncountry=PT&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEDbwnLOm9cCLQw62JluesRsIz13dGLcGR3g22Rl1TpjQLRqybwbYHRoCbTMQAvD_BwE&gclsrc=aw.ds">Norton</a>, <a href="https://www.mcafee.com/consumer/pt-pt/landing-page/direct/sem/mtp-family/desktop/brand-ad.html?csrc=google&csrcl2=brand&cctype=[PT-PT][Search][Brand]McAfee&ccstype=&ccoe=direct&ccoel2=sem&affid=1485&culture=PT-PT&utm_source=google&utm_medium=paidsearch&utm_campaign=[PT-PT][Search][Brand]McAfee&utm_content=[brand][exact]mcafee&utm_term=mcafee&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEB9Z6QxypEvqzc3LCPYisQUsFVCnowFSUXK73SOjadoDZa8H8jkVLBoC_hsQAvD_BwE">McAfee</a>, <a href="https://www.kaspersky.co.uk/home-security?ignoreredirects=true">Kaspersky</a></td>
    <td class="tg-0lax"><a href="http://sanddroid.xjtu.edu.cn/">SandDroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data&nbsp;&nbsp;&nbsp;Leakage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and Authorization, <br>Use of Encryption</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://github.com/sinpolib/nfcspy">NFCSpy</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Encryption,   Authentication and <br>Authorization, Web Server <br>Authentication, Access Control</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.kali.org/docs/introduction/">Kali Linux</a>, <a href="https://github.com/MillerTechnologyPeru/hcitool">hcitool</a></td>
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
    <td class="tg-0lax"><a href="https://androguard.readthedocs.io/en/latest/intro/gettingstarted.html">BlackBag Blacklight</a>, <a href="https://security.opentext.com/encase-forensic">Encase Forensics</a>, <a href="https://www.oxygen-forensic.com/es/">Oxygen Forensic Suite</a> </td>
    <td class="tg-0lax"><a href="https://androguard.readthedocs.io/en/latest/intro/gettingstarted.html">Androguard</a>
, <a href="https://labs.f-secure.com/assets/BlogFiles/mwri-drozer-user-guide-2015-03-23.pdf">Drozer</a>, <a href="https://github.com/spotbugs/spotbugs">SpotBugs</a>,&nbsp;&nbsp;&nbsp;<a href="https://github.com/den4uk/andriller">Andriller</a></td> 
    <td class="tg-0lax"><a href="https://www.elcomsoft.com/eift.html">Elcomsoft iOS Forensic Toolkit</a></td>
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
    <td class="tg-0lax">Malware and Privacy Scanners </td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.bitdefender.com/solutions/total-security.html">Bitdefender</a>, <a href="https://pt.norton.com/ps/3up_norton360_ns_nd_np_Reading_tw_nb.html?nortoncountry=pt&om_sem_cid=hho_sem_sy:pt:ggl:pt:e:br:kw0000004480:465830486375:c:google:195269073:16491667593:kwd-15050890&nortoncountry=PT&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEDbwnLOm9cCLQw62JluesRsIz13dGLcGR3g22Rl1TpjQLRqybwbYHRoCbTMQAvD_BwE&gclsrc=aw.ds">Norton</a>, <a href="https://www.mcafee.com/consumer/pt-pt/landing-page/direct/sem/mtp-family/desktop/brand-ad.html?csrc=google&csrcl2=brand&cctype=[PT-PT][Search][Brand]McAfee&ccstype=&ccoe=direct&ccoel2=sem&affid=1485&culture=PT-PT&utm_source=google&utm_medium=paidsearch&utm_campaign=[PT-PT][Search][Brand]McAfee&utm_content=[brand][exact]mcafee&utm_term=mcafee&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEB9Z6QxypEvqzc3LCPYisQUsFVCnowFSUXK73SOjadoDZa8H8jkVLBoC_hsQAvD_BwE">McAfee</a>, <a href="https://www.kaspersky.co.uk/home-security?ignoreredirects=true">Kaspersky</a></td>
    <td class="tg-0lax"><a href="http://sanddroid.xjtu.edu.cn/">SandDroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data&nbsp;&nbsp;&nbsp;Leakage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a>, <a href="https://github.com/ukanth/afwall">AFWall+</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and Authorization, <br>Use of Encryption</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://github.com/sinpolib/nfcspy">NFCSpy</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Encryption,   Authentication and <br>Authorization, Web Server <br>Authentication, Access Control</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.kali.org/docs/introduction/">Kali Linux</a>, <a href="https://github.com/MillerTechnologyPeru/hcitool">hcitool</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Use of   encryption, Secure backup, <br>logging and Insecure Data Storage</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.sleuthkit.org/index.php">Slueth Kit + <br>Autopsy Browser</a></td>
    <td class="tg-0lax"><a href="https://github.com/androguard/androguard">AndroGuard</a>, <a href="https://labs.f-secure.com/assets/BlogFiles/mwri-drozer-user-guide-2015-03-23.pdf">Drozer</a>, <br><a href="https://github.com/iBotPeaches/Apktool">apktool</a>, <a href="https://dl.acm.org/doi/10.1145/3183575">Amandroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dynamic&nbsp;&nbsp;&nbsp;binary analysis: debugging, tracing</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Hybrid Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax"><a href="https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security">RMS</a></td>
    <td class="tg-0lax"><a href="https://labs.f-secure.com/assets/BlogFiles/mwri-drozer-user-guide-2015-03-23.pdf">Drozer</a>, <a href="https://github.com/FSecureLABS/drozer/releases/download/2.3.4/sieve.apk">Sieve</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax"><a href="https://pypi.org/project/iOSbackup/">iOSbackup</a></td>
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
    <td class="tg-0lax"><a href="https://github.com/NationalSecurityAgency/ghidra">Ghidra</a></td>
    <td class="tg-0lax"><a href="https://github.com/pxb1988/dex2jar">Dex2jar</a>, <a href="https://github.com/java-decompiler/jd-gui/releases">JD-GUI</a>, <br><a href="http://newandroidbook.com/tools/dextra.html">Dextra</a></td>
    <td class="tg-0lax"><a href="https://github.com/KJCracks/Clutch">Clutch</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Mobile   decryption, <br>unpacking &amp; conversion</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://github.com/MobSF/Mobile-Security-Framework-MobSF">MobSF</a></td>
    <td class="tg-0lax"><a href="https://github.com/shivsahni/APKEnum">APKEnum</a></td>
    <td class="tg-0lax"><a href="https://damnvulnerableiosapp.com/">Damn Vulnerable <br>iOS App</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,   <br>logging and Insecure <br>Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/adb">adb</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Static binary   analysis: <br>disassembly, decompilation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Manual (Reversed) <br>Code Review</td>
    <td class="tg-0lax"><a href="https://github.com/bambooeric/r2ghidra-dec">r2ghidra-dec</a>,<a href="https://github.com/radareorg/r2ghidra">r2frida</a>, <br><a href="https://github.com/radareorg/radare2">Radare2</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://www.hopperapp.com/">Hooper</a></td>
  </tr>
</tbody>
</table>


In order to avoid or prevent *Malware as a Service, Side-Channel and Botnets* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Use of   encryption, Secure backup, <br>logging and Insecure Data Storage</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.sleuthkit.org/index.php">Slueth Kit + Autopsy Browser</a></td>
    <td class="tg-0lax"><a href="https://github.com/androguard/androguard">AndroGuard</a>, <a href="https://labs.f-secure.com/assets/BlogFiles/mwri-drozer-user-guide-2015-03-23.pdf">Drozer</a>, <a href="https://github.com/iBotPeaches/Apktool">apktool</a>, <a href="https://dl.acm.org/doi/10.1145/3183575">Amandroid</a></td>
    <td class="tg-0lax"></td>
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
    <td class="tg-0lax"><a href="https://play.google.com/store/apps/details?id=com.denper.addonsdetector&hl=pt_PT&gl=US">Addons Detector</a></td>
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
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">DoS and DDoS Attacks</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis </td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="http://www.cydiasubstrate.com/">Cydia Substrate</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="http://www.cycript.org/">Cycript</a></td>
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
    <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-Android">Introspy-Android</a></td>
    <td class="tg-0lax"><a href="https://github.com/iSECPartners/Introspy-iOS">Introspy-iOS</a></td>
  </tr>
</tbody>
</table>
