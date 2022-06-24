In order to avoid or prevent *Malware as a Service, Malicious QR Code, Botnets, Spoofing, Eavesdroping, NFC Payment Replay, Bynzantine, Bluesnarfing, Bluejacking, Side-Channel, Flooding attacks*, the following security tests should be performed.


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
    <td class="tg-0lax">Malware and Privacy Scanners </td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.bitdefender.com/solutions/total-security.html">Bitdefender</a>, <a href="https://pt.norton.com/ps/3up_norton360_ns_nd_np_Reading_tw_nb.html?nortoncountry=pt&om_sem_cid=hho_sem_sy:pt:ggl:pt:e:br:kw0000004480:465830486375:c:google:195269073:16491667593:kwd-15050890&nortoncountry=PT&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEDbwnLOm9cCLQw62JluesRsIz13dGLcGR3g22Rl1TpjQLRqybwbYHRoCbTMQAvD_BwE&gclsrc=aw.ds">Norton</a>, <a href="https://www.mcafee.com/consumer/pt-pt/landing-page/direct/sem/mtp-family/desktop/brand-ad.html?csrc=google&csrcl2=brand&cctype=[PT-PT][Search][Brand]McAfee&ccstype=&ccoe=direct&ccoel2=sem&affid=1485&culture=PT-PT&utm_source=google&utm_medium=paidsearch&utm_campaign=[PT-PT][Search][Brand]McAfee&utm_content=[brand][exact]mcafee&utm_term=mcafee&gclid=CjwKCAjwwdWVBhA4EiwAjcYJEB9Z6QxypEvqzc3LCPYisQUsFVCnowFSUXK73SOjadoDZa8H8jkVLBoC_hsQAvD_BwE">McAfee</a>, <a href="https://www.kaspersky.co.uk/home-security?ignoreredirects=true">Kaspersky</a></td>
    <td class="tg-0lax"><a href="http://sanddroid.xjtu.edu.cn/">SandDroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Data&nbsp;&nbsp;&nbsp;Leakage</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td class="tg-0lax"><a href="https://www.taosoftware.co.jp/en/android/packetcapture/">tPacketCapturepro</a>, <a href="https://github.com/ukanth/afwall">AFWall+</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Authentication   and Authorization, <br>Use of Encryption</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Proxies</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><a href="https://github.com/sinpolib/nfcspy">NFCSpy</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Encryption,   Authentication and <br>Authorization, Web Server <br>Authentication, Access Control</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="https://www.kali.org/docs/introduction/">Kali Linux</a>, <a href="https://github.com/MillerTechnologyPeru/hcitool">hcitool</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Use of   encryption, Secure backup, <br>logging and Insecure Data Storage</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Forensic Mobile</td>
    <td class="tg-0lax"><a href="https://www.sleuthkit.org/index.php">Slueth Kit + <br>Autopsy Browser</a></td>
    <td class="tg-0lax"><a href="https://github.com/androguard/androguard">AndroGuard</a>, <a href="https://labs.f-secure.com/assets/BlogFiles/mwri-drozer-user-guide-2015-03-23.pdf">Drozer</a>, <br><a href="https://github.com/iBotPeaches/Apktool">apktool</a>, <a href="https://dl.acm.org/doi/10.1145/3183575">Amandroid</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dynamic&nbsp;&nbsp;&nbsp;binary analysis: debugging, tracing</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Hybrid Analysis</td>
    <td class="tg-0lax">Vulnerability Scanner</td>
    <td class="tg-0lax">RMS</td>
    <td class="tg-0lax">Drozer, Sieve</td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Secure backup,&nbsp;&nbsp;&nbsp;logging and Insecure Data Storage</td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Mobile Forensic</td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax"> </td>
    <td class="tg-0lax">iOSbackup</td>
  </tr>
</tbody>
</table>
