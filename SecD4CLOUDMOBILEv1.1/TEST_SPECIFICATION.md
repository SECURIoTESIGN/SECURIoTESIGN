# Final Security Test Specification and Tools Report  

|                           |                                                              |  
|  :--------                |  :---------                                                  |  
|  Mobile Platform          |  Hybrid Application                                          |  
|  Application domain type  |  m-Health                                                    |  
|  Authentication           |  Yes                                                         |  
|  Authentication schemes   |  Biometric-based authentication ; ID-based authentication    |  
|  Has DB                   |  Yes                                                         |  
|  Type of database         |  SQL (Relational Database)                                   |  
|  Which DB                 |  MySQL                                                       |  
|  Type of information handled|  Personal Information ; Confidential Data ; Critical Data    |  
|  Storage Location         |  Both                                                        |  
|  User Registration        |  Yes                                                         |  
|  Type of Registration     |  The users will register themselves                          |  
|  Programming Languages    |  HTML5 + CSS + JavaScript                                    |  
|  Input Forms              |  Yes                                                         |  
|  Upload Files             |  Yes                                                         |  
|  The system has logs      |  Yes                                                         |  
|  The system has regular updates|  Yes                                                         |  
|  The system has third-party|  Yes                                                         |  
|  System Cloud Environments|  Public Cloud                                                |  
|  HW Authentication        |  Basic Authentication (user/pass)                            |  
|  HW Wireless Tech         |  3G ; 4G/LTE ; 5G ; Bluetooth  ; Wi-Fi  ; GPS  ; NFC         |  
|  Device or Data Center Physical Access|  Yes                                                         |  

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
    <td class="tg-0lax">DoS and DDoS <br>Attacks</td>
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
    <td class="tg-0lax"><a href="https://www.parasoft.com/products/parasoft-c-ctest/">PARASOFT C/C++ TEST</a>, <a href="https://security.web.cern.ch/recommendations/en/codetools/rats.shtml/">RATS</a>, <a href="https://clang-analyzer.llvm.org/scan-build.html">Clang Code Analyze</a>, <a href="https://github.com/AndroBugs/AndroBugs_Framework">AndroBugs</a></td> 
    <td class="tg-0lax"><a href="https://docs.angr.io/introductory-errata/install">Angr</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Binary code Scanner</td>
    <td class="tg-0lax"><a href="https://blackberry.qnx.com/en/software-solutions/blackberry-jarvis">BlackBerry Jarvis</a>, <br><a href="https://www.grammatech.com/codesonar-sast-binary">CodeSonar for Binaries</a>, <a href="https://sourceforge.net/projects/bugscam/">BugScam</a>, <a href="https://www.veracode.com/products/binary-static-analysis-sast">SAST</a></td>
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


In order to avoid or prevent *Spoofing, Eavesdropping, Sniffing, Botnets, MiTM, Flooding, Reverse Engineering attacks*, the following security tests should be performed.


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
