In order to ensure that applications are resilient to an eventual attack and that they do not violate the principle of minimum requirements when sharing resources locally or remotely, app developers for the cloud & mobile ecosystem are recommended to incorporate *confinement mechanisms*, as well as those of access control or secure permissions.

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
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Privacy, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">integrity, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">authenticity, </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">immunity</span></td>
    <td class="tg-7zrl"><span style="font-weight:normal;font-style:normal;text-decoration:none">Both</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Confinement</span></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Sandboxing</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Application</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:normal;font-style:normal;text-decoration:none">Both</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Firewall</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:normal;font-style:normal;text-decoration:none">Both</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">DMZ</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">iOS</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Unix Permissions</span> </td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">iOS</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">iOS Capabilities</span> </td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
  </tr>
  <tr>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">iOS</span></td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:black">Hard-Coded Checks</span> </td>
    <td class="tg-7zrl"></td>
    <td class="tg-7zrl"></td>
  </tr>
</tbody>
</table>