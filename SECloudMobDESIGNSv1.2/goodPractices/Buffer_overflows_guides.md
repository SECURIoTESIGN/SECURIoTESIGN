# Buffer Overflows Vulnerability Countermeasures

## Buffer Overflows
Buffer overflows is anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.

## Effects

Buffer overflow may result in erratic program behavior, including memory access errors, incorrect results, a crash, or a breach of system security.

## Recommendations:

 * Use programming languages immune to buffer overflow vulnerabilities, such as, Java or C#;
 * In the event that it is not feasible to use languages ​​that are immune to buffer overflow vulnerabilities, defensive programming should consist of:
   * Always check the limits of buffers;
   * Avoid using dangerous functions that do not check these limits (eg, gets, strcpy, sprintf and scanf) or handle such functions well if they are even indispensable;
   * Use safer versions of each of the previously referenced functions, such as strncpy, strncat and snprintf;
 * Correct use of library functions according to their intrinsic hazard level.