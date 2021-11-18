In order to guarantee the confidentiality and privacy of data shared, at rest or in transit by legitimate users and communications, as well as the integrity, authenticity of data and communications, it is recommended to developers of apps for the cloud & mobile platform to incorporate the algorithms cryptographic and related mechanisms in the implementation and codification phase of the software development process, as described below.


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-iuxe{background-color:#A6A6A6;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Requirement</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Plataform</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Mechanism</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Mechanism Type</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Description</span></th>
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Leyer</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Privacy, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">confidentiality, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authenticity, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authorization</span></td>
    <td class="tg-7zrl">Both</td>
    <td class="tg-0lax">Cryptographic<br> algorithms and <br>related   mechanisms</td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">TCP/TLS,HTTPS, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">XMPP, AES256-RSA, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SSL/TLS, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">HTTPSCurve25519, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">AES-256, AES256-RSA2048</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Encrypted </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">communications</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">MAC, Digital Signatures</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Authentic </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">communications</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">AES-GCM-256 or </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">ChaCha20-Poly1305</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Confidentiality </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Algorithms</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SA (3072 bits and higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">ECDSA with NIST P-384</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Digital Signature </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Algorithms</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Integrity</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SHA-256, SHA-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">384, SHA-512, Blake2</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">RSA (3072 bits and higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">DH (3072 bits or higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">ECDH with NIST P-384</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Key establishment </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">algorithms</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Communication</span></td>
  </tr>
</tbody>
</table>
