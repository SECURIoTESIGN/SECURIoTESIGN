
In order to avoid or prevent *Man-in-the-Middle* attacks, the following security tests should be performed.

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
    <td class="tg-cly1">Proper SSL usage, Use of encryption</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-cly1">Static Analysis via Forensic Mobile</td>
    <td class="tg-cly1">XTY, Cellebrite, OpenSSL</td>
    <td class="tg-cly1">AndroGuard, MalloDroid, apktool, Amandroid</td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Poor use of certificate parameters</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic analysis via Proxies</td>
    <td class="tg-0lax">NMAP, Nessus, SuperScan, Metasploit Framework</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-cly1">Data leakage</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-cly1">Dinamic analysis via Proxies</td>
    <td class="tg-cly1">Wireshark, , ettercap, sslsniff, mitmproxy</td>
    <td class="tg-cly1">tPacketCapturepro, AFWall+,</td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup and logging</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Dinamica Analysis via Proxies</td>
    <td class="tg-0lax">ettercap, sslsniff</td>
    <td class="tg-0lax">adb</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Web Server connection</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Manual Dinamic Analysis via Proxies</td>
    <td class="tg-0lax">ITR, WebScarab, Paros</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Web Server authentication</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis via Proxies</td>
    <td class="tg-0lax">Wireshark</td>
    <td class="tg-0lax">tPacketCapturepro</td>
    <td class="tg-0lax"></td>
  </tr>
</table>
