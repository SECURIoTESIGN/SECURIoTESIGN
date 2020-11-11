# Buffer Overflows Attack

As its name implies, buffer overflows occur when data exceeding its capacity is placed in a buffer. This occurs in programs implemented in C or C++, as these programming languages do not check if buffer limits are violated.


## Definition

Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code. Buffer overflow may result in erratic program behavior, including memory access errors, incorrect results, a crash, or a breach of system security. 
 
## Attacker Powers

 * Overwrite the return address of a procedure call;
 * Obtain control of a system;
 * Launch more virulent attacks, such DoS or DDoS.
 
 
## Buffer Overflows Attack Diagram


