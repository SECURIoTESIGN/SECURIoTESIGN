In order to guarantee the confidentiality, availability and privacy of shared data and  data freshness, at rest, in use or in transit by legitimate users and communications, as well as the integrity and authenticity of data and communications, developers are recommended of apps for the cloud & mobile platform incorporate *secure backup mechanisms* in the implementation and codification phase of the software development process, as described below.


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
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Integrity, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authenticity and </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">privacy, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authorization, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">availability, data </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">freshness</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Backup</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Local and remote </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">encrypted storage </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">using modern and </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">secure encryption </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">schemes</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">To incorporate remote </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authentication mechanisms, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">that is, access to stored </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">data should only be possible </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">through remote authentication</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Data Link</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Using NIDS, NIPS, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">HIDS, HIPS</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Allow to guarantee the </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">defense in depth</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Network</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">To incorporate </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">hybrid authentication </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">mechanisms for </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">accessing applications </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">from the mobile device </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">(e.g., fingerprint and PIN, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">face recognition and PIN </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">or voice and PIN recognition, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">iris recognition and PIN or PIN)</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Application</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">To incorporate access </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">control mechanisms </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">that ensure application </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">data isolation and </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">user session management</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Application</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Installing IPS and IDS </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">on mobile devices, in order</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black"> to guarantee the perimeter </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">security of user data stored </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">locally</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Network</span></td>
  </tr>
</tbody>
</table>
