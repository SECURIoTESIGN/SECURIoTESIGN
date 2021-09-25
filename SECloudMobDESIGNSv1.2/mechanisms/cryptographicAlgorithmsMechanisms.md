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
    <th class="tg-iuxe"><span style="font-weight:700;font-style:normal;text-decoration:none;color:black;background-color:#A6A6A6">Layer</span></th>
  </tr>
</thead>
<tbody>
<tr>
<td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Privacy and confidentiality, authenticity, authorization</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Both</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Cryptographic algorithms and related mechanisms</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">TCP/TLS, HTTPS, XMPP, AES256-RSA, SSL/TLS, HTTPSCurve25519, AES-256, AES256-RSA2048</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Encrypted communications</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation and Application</span></td>

  </tr>

  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">MAC, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Digital Signatures</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Authentic communications</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">and Application</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">AES-GCM-256 or ChaCha20-</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Poly1305</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Confidentiality Algorithms</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">and Application</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">RSA (3072 bits and higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">ECDSA with NIST P-384</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Digital Signature Algorithms</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">and Application</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Integrity</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SHA-256, SHA-384, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">SHA-512, Blake2</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">and Application</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">RSA (3072 bits and higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">DH (3072 bits or higher), </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">ECDH with NIST P-384</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Key establishment algorithms</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Presentation </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">and Application</span></td>
  </tr>
</tbody>
</table>
