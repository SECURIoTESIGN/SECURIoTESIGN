# Cross Site Scripting Attacks

In short, Cross Site Scripting (XSS) allows an attacker to execute a browser script bypassing access control mechanisms such as the same origin policy. During this attack a malicious script is injected into web content and user considering it to be authentic executes it over its own machine, thus giving either control of the machine or exposure of confidential information to the attacker.

## Definition

Being an attack that exploits vulnerabilities in web applications, the attacker in this type of attack executes malicious database claims, exploiting improper validation of data flowing from the user to the database. The attacker's goal is to access the intended party's confidential data by inserting malicious code into the user's web page in order to redirect them to their site. There are two ways to forge this type of attack:

 * Stored XSS (uninterruptedly stores malicious code in a resource managed by the web application);
 * Reflective XSS (promptly reflects malicious code against the user and therefore does not store it permanently;
 * XSS based on DOM (Document Object Model).
 
## Technical Impact
 * Gain Privileges or Assume Identity;
 * Bypass Protection Mechanism; 
 * Read Application Data; 
 * Modify Application Data; 
 * DoS: Crash, Exit, or Restart.
 
## Risk Analysis
 * Critical Risk.
 
## Likelihood of Exploit
 * Medium.
 
## Attacker Powers
 * Circumvent the policy of same origin;
 * Impersonate you to websites and/or web applications you regularly use by obtaining/altering/destroying various types of content.

## Recommendations

To ensure that the mobile application is resilient or immune to XSS attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed to ensure authenticity, integrity, privacy and authenticity of the data.

## References
1. [https://cwe.mitre.org/data/definitions/352.html];
2. [https://www.first.org/cvss/v3.1/examples]

## Cross Site Scripting Attacks Diagram


