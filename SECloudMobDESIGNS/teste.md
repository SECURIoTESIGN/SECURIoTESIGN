
# Black Box Testing

The tests are derived from an external description of the software, for example, a description of its attack surface. It is a technique often used by individuals who are dedicated to looking for or discovering vulnerabilities..

## Definition

In this scenario, the term “black box testing” mean test methods that are not based directly on a program’s architecture source code. The term connotes a situation in which either the tester does not have access to the source code or the details of the source code are irrelevant to the properties being tested. This means that black box testing focuses on the externally visible behavior of the software. For example, it may be based on requirements, protocol specifications, APIs, or even attempted attacks.
  
## Characterization

Black box testing tools provide various types of automated support for testers. They help testers work more efficiently by automating whatever tasks can be automated, and they also help testers avoid making mistakes in a number of tasks where careful bookkeeping is needed. Their main roles include:

 * Test automation: providing automated support for the actual process of executing tests, especially tests that have already been run in the past but are being repeated
 * Test scaffolding: providing the infrastructure needed in order to test efficiently
 * Test management: various measurements and scheduling and tracking activities that are needed for efficient testing even though they are not directly involved in the execution of test cases

 
## Recommended Tools

 * NMAP;
 * Nessus;
 * SuperScan; 
 * Metasploit Framework.


# Black Box Testing
In this software testing paradigm, tests are derived from an external description of the software, e.g., a description of its attack surface. It is a technique widely used by individuals who are dedicated to locating vulnerabilities.

## Definition

Black Box testing  is a test methods that are not based directly on a program’s architecture source code. The term connotes a situation in which either the tester does not have access to the source code or the details of the source code are irrelevant to the properties being tested. This means that black box testing focuses on the externally visible behavior of the software. For example, it may be based on requirements, protocol specifications, APIs, or even attempted attacks.
  
## Characterization

Black box testing tools provide various types of automated support for testers. They help testers work more efficiently by automating whatever tasks can be automated, and they also help testers avoid making mistakes in a number of tasks where careful bookkeeping is needed. Their main roles include

 * Test automation: providing automated support for the actual process of executing tests, especially tests that have already been run in the past but are being repeated;
 * Test scaffolding: providing the infrastructure needed in order to test efficiently;
 * Test management: various measurements and scheduling and tracking activities that are needed for efficient testing even though they are not directly involved in the execution of test cases.

In order to avoid or prevent man-in-the-middle attacks, the following security tests should be performed:

|            Test Parameter           | Approach  |             Test Method             |                     Tools                     |                                 |     |
|:-----------------------------------:|-----------|:-----------------------------------:|:---------------------------------------------:|---------------------------------|-----|
|                                     |           |                                     | Ambos                                         | Android                         | iOS |
| Proper SSL usage, Use of encryption | White Box | Static Analysis via Forensic Mobile |            XTY, Cellebrite, OpenSSL           | AndroGuard, MalloDroid, apktool |     |
| Poor use of certificate parameters   | Black Box |     Dinamic analysis via Proxies    | NMAP, Nessus, SuperScan, Metasploit Framework |                                 |     |
| Data leakage                        | Grey Box  |     Dinamic analysis via Proxies    |                   Wireshark                   | tPacketCapturepro, DroidWall,   |     |
| Secure backup and logging           | Grey Box  | Dinamica Analysis via Proxies       |                                               |                                 | adb |
| Web Server connection               | Black Box | Manual Dinamic Analysis via Proxies | ITR, WebScarab, Paros                         |                                 |     |
| Web Server authentication           | Black Box | Dinamic Analysis via Proxies        | Wireshark                                     | tPacketCapturepro               |     |
