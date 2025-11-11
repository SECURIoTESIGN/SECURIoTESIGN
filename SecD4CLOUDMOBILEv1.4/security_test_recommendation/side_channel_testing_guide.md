# Security Testing Setup for Side-Channel Attacks 
## 1. Overview

**Goal:** Measure and mitigate leakage (power, EM, timing, cache) that can reveal secrets (cryptographic keys, credentials) across cloud, mobile and IoT components.

**Scope:** cloud VMs/HSMs, mobile apps (Android/iOS), IoT edge devices (Raspberry Pi/ESP32), network links.

---

## 2. Key Test Categories

* **Timing analysis** &mdash; check for variable-time crypto or API calls.
* **Cache attacks** &mdash; flush+reload / prime+probe on shared hosts.
* **Power & EM** &mdash; measure device emissions to recover keys (edge devices, smartcards).
* **Network timing correlation** &mdash; infer operations via request/response timing.
* **Code review** &mdash; find non-constant time code, unsafe libraries, or shared-resource patterns.

---

## 3. Compact Testing Tools


<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr style="background-color:#f2f2f2;">
      <th>Test Approach</th>
      <th>Analysis Type</th>
      <th>Approach Name</th>
      <th>Testing Tool</th>
      <th>Tool Hyperlink</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Physical Security Measures Review</td>
      <td>ChipWhisperer</td>
      <td><a href="https://chipwhisperer.io/">ChipWhisperer</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Code Review / Timing Analysis</td>
      <td>CacheAudit</td>
      <td><a href="https://github.com/secure-software-engineering/CacheAudit">CacheAudit</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Fuzzing / Input Timing Testing</td>
      <td>American Fuzzy Lop (AFL)</td>
      <td><a href="https://lcamtuf.coredump.cx/afl/">AFL</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Electromagnetic and Power Analysis</td>
      <td>Riscure Inspector</td>
      <td><a href="https://www.riscure.com/security-tools/inspector/">Riscure Inspector</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Code Security Scanner / Constant-Time Verification</td>
      <td>ctgrind (Valgrind plugin)</td>
      <td><a href="https://github.com/agl/ctgrind">ctgrind</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Network Packet Sniffing / Timing Correlation</td>
      <td>Wireshark</td>
      <td><a href="https://www.wireshark.org/">Wireshark</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Code Review for Cache Leakage</td>
      <td>LLVM-based DataFlow Sanitizer</td>
      <td><a href="https://clang.llvm.org/docs/DataFlowSanitizer.html">LLVM-based DataFlow</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>


---

## 4. Minimal Testbed & Quick Steps

1. **Isolate lab** (air-gapped or VLAN). snapshot/backup targets.
2. **Baseline**: capture normal timing/power/EM traces.
3. **Attack**: run cache/timing tests and power/EM captures (ChipWhisperer) against crypto operations.
4. **Code review**: search for non-constant time ops, secret-dependent branching. Use ctgrind / static checks.
5. **Detect**: monitor `perf` / counters, timing variance, unusual cache misses; alert via SIEM.
6. **Mitigate & retest**: apply constant-time libs, masking, noise, HSMs/secure enclaves — then repeat tests.

---

## 5. References

1. Mangard, S., Oswald, E., & Popp, T. (2007). Power analysis attacks: Revealing the secrets of smart cards. Boston, MA: *Springer US*.
2. Yarom, Y., & Falkner, K. (2014). {FLUSH+ RELOAD}: A high resolution, low noise, l3 cache {Side-Channel} attack. In *23rd USENIX security symposium (USENIX security 14)* (pp. 719-732).
3. Genkin, D., Shamir, A., Tromer, E. (2014). RSA Key Extraction via Low-Bandwidth Acoustic Cryptanalysis. In: Garay, J.A., Gennaro, R. (eds) Advances in Cryptology – CRYPTO 2014. CRYPTO 2014. *Lecture Notes in Computer Science*, vol 8616. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-662-44371-2_25](https://doi.org/10.1007/978-3-662-44371-2_25)

