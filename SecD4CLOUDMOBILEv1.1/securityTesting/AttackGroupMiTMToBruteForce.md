In order to avoid *MiTM, Eavesdropping, Side-Channel, VM Escape,  WiFi SSID Tracking, Rogue Access Point, Cellular Rogue Base Station, Sniffing, Cryptanalysis, Audit Log Manipulation Attacks, Byzantine, On-Off, Brute Force*, the following security tests should be perform.
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
        <td class="tg-0lax">Proper SSL usage and <br>Insecure TLS Protectio, <br>Use of encryption</td>
        <td class="tg-0lax">White Box</td>
        <td class="tg-0lax">Static analysis</td>
        <td class="tg-0lax">Forensic Mobile</td>
        <td class="tg-0lax">XTY, Cellebrite, OpenSSL</td>
        <td class="tg-0lax">AndroGuard and <br>MalloDroid, apktool, <br>Amandroid</td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Interception of   network</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Hybrid</td>
        <td class="tg-0lax">Penetration Testing</td>
        <td class="tg-0lax">Burp Suite, Wireshark, <br>bettercap</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Interception of network</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxy</td>
        <td class="tg-0lax">mitm-relay, Kali Linux, <br>Burp   Suite</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Poor use of   certificate <br>parameters</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax">NMAP, Nessus, SuperScan,  <br> Metasploit Framework</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Data leakag</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Dynamic analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax">Wireshark</td>
        <td class="tg-0lax">tPacketCapturepro, <br>AFWall+</td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Secure backup,   logging <br>and Insecure Data Storage</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxies, Penetration <br>Testing</td>
        <td class="tg-0lax">Frida</td>
        <td class="tg-0lax">adb</td>
        <td class="tg-0lax">iPhone Backup, <br>Unlocker</td>
      </tr>
      <tr>
        <td class="tg-0lax">Secure backup,   <br>logging and <br>Insecure Data <br>Storage</td>
        <td class="tg-0lax">White Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Mobile Forensic</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax">Logcat</td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Web Server <br>connection</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Manual Dynamic Analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax">ITR, OWASP WebScarab, <br>OWASP ZAP,   Paros</td>
        <td class="tg-0lax"></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Web Server Authentication</td>
        <td class="tg-0lax">Black Box</td>
        <td class="tg-0lax">Dynamic Analysis</td>
        <td class="tg-0lax">Proxies</td>
        <td class="tg-0lax">Wireshark,Tapioca</td>
        <td class="tg-0lax">tPacketCapturepro</td>
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