In order to avoid or prevent *Malicious Insider, Sniffing, MiTM, Eavesdropping* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Data leakage and Breach</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a>, <a href="https://github.com/ukanth/afwall">AFWall+</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis </td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.securenetwork.it/docs/talks/2010-10_BlackHat-USA-2010_Virtually-Pwned.pdf">VASTO</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Stressing Testing (fuzzing)</td>
    <td class="tg-0lax"><a href="https://github.com/ovanr/webFuzz">Webfuzz</a>, <a ref="https://github.com/xmendez/wfuzz">Wfuzz</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax"><a href="https://www.acunetix.com/support/">Acunetix</a>, <a href="http://docs.w3af.org/en/latest/basic-ui.html">W3af</a, <a href="https://github.com/sullo/nikto">Nikto</a>,&nbsp;&nbsp;&nbsp;<a href="https://www.microfocus.com/media/data-sheet/webinspect_automated_dynamic_application_security_testing_ds.pdf">Fortify WebInspect</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax" colspan="2"><a href="https://www.tcpdump.org/">TCPDump</a>, <a href="https://www.wireshark.org/">Wireshark</a</td>
    <td class="tg-0lax">idb tool</td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dynamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://developer.android.com/studio/command-line/adb"></a>adb</td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>
