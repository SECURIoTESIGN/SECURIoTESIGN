In order to ensure that the data shared and exchanged between two or more authorized entities are reliable, complete, authentic and only accessible to these entities, it is recommended that software developers for the mobile ecosystem incorporate *cryptographic protocols* in the implementation and codification phase of the software development process, as described below.


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-iuxe{background-color:#A6A6A6;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Requirement</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Plataform</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Mechanism</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Mechanism Type</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Description</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Layer</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Cryptographic </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Protocols over </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SCTP/UDP</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SSL/TLS, DTLS</span> </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Protocols that can be used </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">or implemented over a network </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">to ensure secure data transmission over</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black"> UDP and SCTP</span> </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Application, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Session</span> </td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Wireless </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Cryptographic </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Protocols</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">WEP, WPA, 802.11i (WPA2), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">EAP, PSK, TKIP, PEAP, EAP-TTLS, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">EAP-PSK, EAP-SIM, EAP-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">AKA, AES-CCMP</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Security Protocols than can </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">be used or im- plemented specifically </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">for wireless networks</span> </td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Transport</span> </td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Cryptographic </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Protocols over </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">IP Protocol</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">IPSec, PEAP, EAP-TLS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Protocols that ensure data packet </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">encryption and authentication over </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">the IP Protocol</span> <br></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Network and </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Data Link</span> </td>
  </tr>
</tbody>
</table>
