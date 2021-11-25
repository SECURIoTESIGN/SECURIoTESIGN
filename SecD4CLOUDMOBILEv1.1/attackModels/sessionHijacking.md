# Session Hijacking Attack

An attacker impersonates a legitimate user through stealing or predicting a valid session ID.

## Definition

The necessary condition for the session hijacking attack to occur is the existence of architectural vulnerabilities in the absence of protection for the storage of session identifiers. This vulnerability generally occurs in web applications written in PHP in previous versions (e.g., PHP 4.0 to PHP 4.1.2), As described in CVE-2002-0121.

## Technical Impact
* Read Application Data; 
* Gain Privileges or Assume Identity; 
* Execute Unauthorized Code or Commands.

## Risk Analysis
* Critical.

## Likelihood of Exploit
* High.

## Attacker Powers

 * Steal Session ID;
 * Impersonation of a legitimate user and confidential information from a legitimate user.

## References
1. [https://www.cvedetails.com/cve/CVE-2002-0121/];
2. [https://cwe.mitre.org/data/definitions/287.html];
3. [https://capec.mitre.org/data/definitions/593.html].
 
 
## Session Hijacking Attack Diagram


