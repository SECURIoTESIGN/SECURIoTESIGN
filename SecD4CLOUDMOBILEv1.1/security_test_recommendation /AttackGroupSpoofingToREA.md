In order to avoid or prevent *Spoofing, Eavesdropping, Sniffing, Botnets, MiTM, Flooding, Reverse Engineering attacks*, the following security tests should be performed.


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
    <td class="tg-0lax"><a href="https://github.com/NationalSecurityAgency/ghidra">Ghidra</a></td>
    <td class="tg-0lax"><a href="https://github.com/pxb1988/dex2jar">Dex2jar</a>, <a href="https://github.com/java-decompiler/jd-gui/releases">JD-GUI</a>, <br><a href="http://newandroidbook.com/tools/dextra.html">Dextra</a></td>
    <td class="tg-0lax"><a href="https://github.com/KJCracks/Clutch">Clutch</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Mobile   decryption, <br>unpacking &amp; conversion</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://github.com/MobSF/Mobile-Security-Framework-MobSF">MobSF</a></td>
    <td class="tg-0lax"><a href="https://github.com/shivsahni/APKEnum">APKEnum</a></td>
    <td class="tg-0lax"><a href="https://damnvulnerableiosapp.com/">Damn Vulnerable <br>iOS App</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,   <br>logging and Insecure <br>Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/adb">adb</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Static binary   analysis: <br>disassembly, decompilation</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Manual (Reversed) <br>Code Review</td>
    <td class="tg-0lax"><a href="https://github.com/bambooeric/r2ghidra-dec">r2ghidra-dec</a>,<a href="https://github.com/radareorg/r2ghidra">r2frida</a>, <br><a href="https://github.com/radareorg/radare2">Radare2</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://www.hopperapp.com/">Hooper</a></td>
  </tr>
</tbody>
</table>
