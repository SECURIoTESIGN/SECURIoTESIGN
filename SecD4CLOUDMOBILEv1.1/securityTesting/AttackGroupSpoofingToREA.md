In order to avoid or prevent *Spoofing, Eavesdropping, Sniffing, Botnets, MiTM, Flooding, Reverse Enginnering attacks*, the following security tests should be performed.


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
    <td class="tg-0lax">Ghidra</td>
    <td class="tg-0lax">Dex2jar, JD-GUI, <br>Dextra</td>
    <td class="tg-0lax">Clutch</td>
  </tr>
  <tr>
    <td class="tg-0lax">Mobile   decryption, <br>unpacking &amp; conversion</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax">MobSF</td>
    <td class="tg-0lax">APKEnum</td>
    <td class="tg-0lax">Damn Vulnerable <br>iOS App</td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,   <br>logging and Insecure <br>Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">adb</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Static binary   analysis: <br>disassembly, decompilation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Manual (Reversed) <br>Code Review</td>
    <td class="tg-0lax">r2ghidra-dec,r2frida, <br>Radare2</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Hooper</td>
  </tr>
</tbody>
</table>