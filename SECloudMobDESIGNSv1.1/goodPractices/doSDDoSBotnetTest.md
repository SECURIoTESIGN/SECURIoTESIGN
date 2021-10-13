# Black Box Testing
In this software testing paradigm, tests are derived from an external description of the software, e.g., a description of its attack surface. It is a technique widely used by individuals who are dedicated to locating vulnerabilities.

## Definition
Black Box testing is a test methods that are not based directly on a program’s architecture source code. The term connotes a situation in which either the tester does not have access to the source code or the details of the source code are irrelevant to the properties being tested. This means that black box testing focuses on the externally visible behavior of the software. For example, it may be based on requirements, protocol specifications, APIs, or even attempted attacks.

## Characterization
Black box testing tools provide various types of automated support for testers. They help testers work more efficiently by automating whatever tasks can be automated, and they also help testers avoid making mistakes in a number of tasks where careful bookkeeping is needed. Their main roles include:
 * Test automation: providing automated support for the actual process of executing tests, especially tests that have already been run in the past but are being repeated;
 * Test scaffolding: providing the infrastructure needed in order to test efficiently;
 * Test management: various measurements and scheduling and tracking activities that are needed for efficient testing even though they are not directly involved
in the execution of test cases.

## White Box Testing
In this type of testing, the tests are derived from the application's source code. This approach is more demanding, but it also allows for better coverage than the previous one. This is an approach usually by companies dedicated to software development.

## Definition 
White box testing is performed based on the knowledge of how the system is implemented. White box testing includes analyzing data flow, control flow, information flow, coding practices, and exception and error handling within the system, to test the intended and unintended software behavior. White box testing can be performed to validate whether code implementation follows intended design, to validate implemented security functionality, and to uncover exploitable vulnerabilities.

## Characterization
The general outline of the white box testing process is as follows:
 * Perform risk analysis to guide the whole testing process. In Microsoft’s SDL process, this is referred to as threat modeling [Howard 06].
 * Develop a test strategy that defines what testing activities are needed to accomplish testing goals.
 * Develop a detailed test plan that organizes the subsequent testing process.
 * Prepare the test environment for test execution.
 * Execute test cases and communicate results.
 * Prepare a report.

## Grey Box Testing
The Gray Box test results from the combination of the Black Box and White Box approaches. Some tests are derived from the external description of the software, others from its source code. It is in a way the "best of both worlds", combining the simplicity of preparing black box tests with the best coverage of white box tests.

## Definition
Between black box and white box testing lies gray box testing, which uses limited knowledge of the program internals. In principle this could mean that the tester knows about some parts of the source code and not others, but in practice it usually just means that the tester has access to design artifacts more detailed than specifications or requirements. For example, the tests may be based on an architecture diagram or a state-based model of the program’s behavior.


In order to avoid or prevent *DoS, DDoS and Botnet attacks* the following security tests should be performed.

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
    <td class="tg-cly1">Add-ons</td>
    <td class="tg-0lax">Gray Box</td>
    <td class="tg-cly1">Static Analysis via Forensic Mobile</td>
    <td class="tg-cly1">Addons Detector</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
  <tr>
    <td class="tg-cly1">DoS and DDoS Attacks</td>
    <td class="tg-0lax">Black Box</td>
    <td class="tg-cly1">Dinamic Analysis via Penetration Test</td>
    <td class="tg-cly1">NMAP, , SlowBot Net, LOlC and Kali Linux</td>
    <td class="tg-cly1"></td>
    <td class="tg-cly1"></td>
  </tr>
</table>
