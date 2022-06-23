In order to avoid or prevent *Buffer Overflow* attacks, the following security tests should be performed.


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
    <td class="tg-0lax">Code quality</td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Dinamic Analysis</td>
    <td class="tg-0lax">Penetration Testing</td>
    <td class="tg-0lax"><a href="http://docs.w3af.org/en/latest/basic-ui.html">W3af</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Bytecode Scanner</td>
    <td class="tg-0lax"><a href="https://github.com/spotbugs/spotbugs">SpotBugs</a></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Source code analyser</td>
    <td class="tg-0lax"><a href="https://www.parasoft.com/products/parasoft-c-ctest/">PARASOFT C/C++ TEST</a>, <a href="https://security.web.cern.ch/recommendations/en/codetools/rats.shtml/">RATS</a>, <br><a href="https://clang-analyzer.llvm.org/scan-build.html">Clang Code Analyze</a></td> 
    <td class="tg-0lax"><a href="https://docs.angr.io/introductory-errata/install">Angr</a></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">White Box</td>
    <td class="tg-0lax">Static Analysis</td>
    <td class="tg-0lax">Binary code Scanner</td>
    <td class="tg-0lax">FxCop,   BugScam</td>
    <td class="tg-0lax"><a href = "https://github.com/JesusFreke/smali">baksmali</a></td>
    <td class="tg-0lax">class-dump-z, frida-ios-dump, <br>Damn   Vunerable iOS App</td>
  </tr>
</tbody>
</table>
