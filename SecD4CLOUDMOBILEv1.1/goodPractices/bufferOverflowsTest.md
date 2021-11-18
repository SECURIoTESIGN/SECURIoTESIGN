In order to avoid or prevent *Buffer Overflows* attacks, the following security tests should be performed.

<table class="tg">
  <tr>
    <th class="tg-yla0" rowspan="2">Test Parameter</th>
    <th class="tg-0lax" rowspan="2"><br><span style="font-weight:bold">Test Type</span></th>
    <th class="tg-yla0" rowspan="2">Test Approach</th>
    <th class="tg-wa1i" colspan="3">Tools</th>
  </tr>
  <tr>
    <td class="tg-yla0">Both</td>
    <td class="tg-yla0">Android</td>
    <td class="tg-yla0">iOS</td>
  </tr>
  <tr>
    <td class="tg-cly1">Input Validation</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-cly1">Dinamic Analysis Checking Input Fields in GUI</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-cly1"></td>
    <td class="tg-0lax">Grey Box</td>
    <td class="tg-cly1">Dinamic Analysis via Fuzzers </td>
    <td class="tg-cly1">Sharefuzz</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via Bytecode Scanner</td>
    <td class="tg-0lax">FindBugs, BugScan of LogicLab Co.</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via Source Code Analyser </td>
    <td class="tg-0lax">C++Test, RATS, C Code nalyzer(CCA)</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis via Binary Code Scanner </td>
    <td class="tg-0lax">BugScan of LogicLab Co. and FxCop;BugScam</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</table>