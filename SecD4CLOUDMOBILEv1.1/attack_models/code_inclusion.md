# Code Inclusion Attacks

Unlike code injection, in this type of attack, an attacker exploits a weakness in the target in order to force arbitrary code to be retrieved locally or from a remote location and executed.

## Definition

 Code inclusion differs from code injection in that code injection involves the direct inclusion of code whereas code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of some application's code. A successful attack of this type has the technical impact of executing unauthorised code or commands, affecting the confidentiality, integrity and availability of the system data~\cite{CAPECVersion3.6}. This type of attack can be executed locally or remotely, as follows:

 * Local Code Inclusion
   * PHP Local File Inclusion;
   * Inclusion of Code in Existing Process;
   * Root/Jailbreak Detection Evasion via Hooking.
 * Remote Code Inclusion
   * Server Side Include (SSI) Injection;
   * PHP Remote File Inclusion;
   * WebView Injection.  

## Typical Severity

* Very High.
 
## Technical Impact
* Execute Unauthorized Code or Commands;
* Read Data;
* Modify Data;
* Gain Privileges;
* Bypass Protection Mechanism.

## Risk Analysis
  * Very High Risk.

## Likelihood of Exploit
  * Medium.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the Code Inclusion attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. [CAPEC-175: Code Inclusion](https://capec.mitre.org/data/definitions/175.html).

## Code Inclusion Attacks Diagram


