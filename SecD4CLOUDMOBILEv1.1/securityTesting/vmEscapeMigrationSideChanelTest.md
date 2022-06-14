
In order to avoid or prevent *VM Escape, Side-Channels and VM Migration attacks*, the following security tests should be performed.

<table class="tg">
  <tr>
    <th class="tg-yla0" rowspan="2">Test Parameter</th>
    <th class="tg-0lax" rowspan="2"><br><span style="font-weight:bold">Test Approach</span></th>
    <th class="tg-yla0" rowspan="2">Test Method</th>
    <th class="tg-wa1i" colspan="3">Tools</th>
  </tr>
  <tr>
    <td class="tg-yla0">Both</td>
    <td class="tg-yla0">Android</td>
    <td class="tg-yla0">iOS</td>
  </tr>
  <tr>
    <td class="tg-cly1" rowspan="3">Leak, breach and data loss</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-cly1">Dinamic analysis via Proxies</td>
    <td class="tg-cly1">Wireshark</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-0lax">Dinamic Analysis via Penetration Testing</td>
    <td class="tg-0lax">VASTO</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-cly1">Dinamic Analysis via Stressing Testing (fuzzing)</td>
    <td class="tg-cly1">SPI Fuzzer, Wfuzz</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
</table>