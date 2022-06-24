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
			<td class="tg-0lax"><a href="https://www.msab.com/product/xry-extract/">XRY</a>, <a ></a><a href="https://cellebrite.com/en/ufed/">UFED Touch</a>, <a href="https://www.openssl.org/">OpenSSL</a></td>
        <td class="tg-0lax"><a href="https://github.com/androguard/androguard">AndroGuard</a>, <a href="https://github.com/sfahl/mallodroid">MalloDroid</a>, <a href="https://github.com/iBotPeaches/Apktool">apktool</a>, <a href="https://dl.acm.org/doi/10.1145/3183575">Amandroid</a></td>
        <td class="tg-0lax"></td>
      </tr>
      <tr>
        <td class="tg-0lax">Interception of   network</td>
        <td class="tg-0lax">Grey Box</td>
        <td class="tg-0lax">Hybrid</td>
        <td class="tg-0lax">Penetration Testing</td>
        <td class="tg-0lax"><a href="https://portswigger.net/burp">Burp Suite</a>, <a href="https://www.wireshark.org/">Wireshark</a>, <br>bettercap</td>
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
        <td class="tg-0lax">Data leakag</td>
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
        <td class="tg-0lax">ITR, <a href="https://github.com/OWASP/OWASP-WebScarab">OWASP WebScarab</a>, <br><a href="https://www.zaproxy.org/">OWASP ZAP</a>,   <a href="https://www.kali.org/tools/paros/">Paros</a></td>
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
