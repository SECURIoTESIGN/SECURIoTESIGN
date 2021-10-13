# Session Hijacking Attack

An attacker impersonates a legitimate user through stealing or predicting a valid session ID.


## Definition

The Session Hijacking can be facilitated by the architectural
weakness of “not securing the storage of session identifiers”. As reported in the CVE-2002-0121, the PHP project vesions 4.0 through 4.1.1 suffered from this architectural flaw because its original design stored each data session in plain textual files in a temporary directory without using a security tactic to store these session files in a secure way (such as encryption).
 
## Attacker Powers

 * Steal Session ID;
 * Impersonation of a legitimate user and confidential information from a legitimate user.
 
 
## Session Hijacking Attack Diagram


