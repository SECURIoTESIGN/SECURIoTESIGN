# Buffer Overflows Attack

As its name implies, buffer overflows occur when data exceeding its capacity is placed in a buffer. This occurs in programs implemented in C or C++, as these programming languages do not check if buffer limits are violated.


## Definition

Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code. Buffer overflow may result in erratic program behavior, including memory access errors, incorrect results, a crash, or a breach of system security.

## Technical Impact
 * Modify Memory; 
 * Execute Unauthorized Code or Commands.

## Risk Analysis
 * High Risk

## Likelihood of Exploit
 * High.
 
## Attacker Powers

 * Overwrite the return address of a procedure call;
 * Obtain control of a system;
 * Launch more virulent attacks, such DoS or DDoS.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the buffer overflows attack, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed.

## References
 1. [https://cwe.mitre.org/data/definitions/120.html];
 2. [https://www.first.org/cvss/calculator/3.1#CVSS:3.1/];
 3. [https://www.first.org/cvss/v3.1/examples].
 
 
## Buffer Overflows Attack Diagram


