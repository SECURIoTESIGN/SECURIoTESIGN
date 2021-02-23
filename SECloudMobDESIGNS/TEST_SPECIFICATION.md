# Final Security Test Specification and Tools Report  

|                           |                                                              |  
|  :--------                |  :---------                                                  |  
|  Architecture             |  Android App                                                 |  
|  Application domain type  |  m-Health                                                    |  
|  Authentication           |  Username and Password                                       |  
|  Has DB                   |  Yes                                                         |  
|  Type of data storage     |  SQL                                                         |  
|  Which DB                 |  SQLite                                                      |  
|  Type of data stored      |  Personal Information ; Confidential Data ; Critical Data    |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  The users will register themselves                          |  
|  Programming Languages    |  Java                                                        |  
|  Input Forms              |  Yes                                                         |  
|  Upload Files             |  Yes                                                         |  
|  The system has logs      |  Yes                                                         |  
|  The system has regular updates|  Yes                                                         |  
|  The system has third-party|  Yes                                                         |  
|  System Cloud Environments|  Public Cloud                                                |  
|  Hardware Specification   |  Yes                                                         |  
|  HW Authentication        |  Basic Authentication (user/pass)                            |  
|  HW Wireless Tech         |  3G ; 4G/LTE ; 5G ; Bluetooth  ; Wi-Fi  ; GPS  ; NFC         |  
|  Data Center Phisical Access|  Yes                                                         |  




In order to avoid or prevent *Botnet, DoS and DDoS Attacks*, the following security tests should be performed.

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





In order to avoid or prevent *Botnet, DoS, DDoS, Phishing, MITM, Spoofing and Sniffing Attacks*, the following security tests should be performed.

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



In order to avoid or prevent *Sniffing, Botnet, Phishing and Spoofing Attacks*, the following security tests should be performed.

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
    <td class="tg-0lax">Use of encryption </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0lax">Static Analysis via Forensic Mobile </td>
    <td class="tg-0lax">OpenSSL </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Poor use of certificate parameters </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span></td>
    <td class="tg-0lax">Dinamic analysis via Vulnerability Scanner </td>
    <td class="tg-0lax">Acunetix, Web3af, Nikto, IBM Security AppScan Standard and HP WebInspect </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span></td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Test</td>
    <td class="tg-0lax">TCPDump, Wireshak </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">idb tool </td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup and logging </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0lax">Dinamic Analysis via Proxies </td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">adb </td>
    <td class="tg-0lax"></td>
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


