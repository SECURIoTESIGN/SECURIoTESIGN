
In order to avoid or prevent *MITM, Sniffing, Side-Channel and VM-Escape attacks*, the following security tests should be performed.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Test Parameter</span></th>
    <th class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Types</span></th>
    <th class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Testing Methods</span></th>
    <th class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Tools</span></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">Android</span></td>
    <td class="tg-0pky"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black">iOS</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Proper SSL usage, Usage of encryption</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">White Box</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Static analysis via Forensic Mobile</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">XTY, Cellebrite, OpenSSL</span><br></td>
    <td class="tg-0pky">AndroGuard and MalloDroid, apktool </td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Interception of network </td>
    <td class="tg-0pky">Grey Box </td>
    <td class="tg-0pky">Static and Dinamic Analysis via Test Penetration </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">BurpSuite</span></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Poor use of certificate parameters </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0pky">Dinamic analysis via Proxies </td>
    <td class="tg-0pky">NMAP, Nessus, SuperScan, Metasploit Framework </td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Data leakage </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0pky">Dinamic Analysis via Proxies</td>
    <td class="tg-0pky">Wireshark</td>
    <td class="tg-0pky">tPacketCapturepro, DroidWall</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Secure backup and logging </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Grey Box</span> </td>
    <td class="tg-0pky">Dinamic Analysis via Proxies or Test Penetration </td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">adb </td>
    <td class="tg-0pky">iPhone Backup Unlocker</td>
  </tr>
  <tr>
    <td class="tg-0pky">Web Server connection </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0pky">Manual Dinamic Analysis via Proxies </td>
    <td class="tg-0pky">ITR and WebScarab, Paros</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Web Server authentication </td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Black Box</span></td>
    <td class="tg-0pky">Dinamic Analysis via Proxies</td>
    <td class="tg-0pky">Wireshark </td>
    <td class="tg-0pky">tPacketCapturepro </td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>