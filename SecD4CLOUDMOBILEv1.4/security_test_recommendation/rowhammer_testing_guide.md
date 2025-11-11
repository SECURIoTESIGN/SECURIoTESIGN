# Security Testing setup for Rowhammer Attacks

## 1. Overview

Rowhammer is a hardware/DRAM failure phenomenon where repeatedly activating ("hammering") certain DRAM rows causes bit flips in adjacent rows. Those bit flips can be induced from software and exploited for privilege escalation, cross-VM attacks, or data corruption  including practical attacks from JavaScript, Android apps, and co-located VMs. Rowhammer continues to be relevant as DRAM scales and remains a realistic attack surface in cloud, desktop, mobile and some IoT platforms.

---

## 2. High-level Testing Workflow / Objectives

1. **Scope & threat model** &mdash; enumerate devices and contexts where DRAM is present and trusted: cloud hypervisors / VMs, edge gateways, mobile devices (Android), IoT devices with DRAM, and browser-based clients. Identify assets that would be impacted by bit flips (kernel pages, crypto keys, page tables, VM page caches).
2. **Baseline & instrumentation** &mdash; ensure test systems have full logging, kernel crash dumps, performance counters available (e.g., `perf`), and remote logging to a secured collector. Snapshot images for fast rollback.
3. **Static & source review (SAST)** &mdash; review code paths that rely on DRAM integrity (hypervisor memory isolation, page deduplication, memory deduplication, kernel modules) and note high-value targets (e.g., page caches used by privileged processes).
4. **Controlled dynamic testing (DAST)** &mdash; run Rowhammer test suites (safe/authorized, in lab) to detect whether a given DRAM module / platform exhibits bit flips and whether flips can be exploited to alter privileged data. Test different hammering patterns (single-sided, double-sided, one-location) and degrees of aggressiveness.
5. **Exploitability assessment** &mdash; attempt end-to-end demonstration in a controlled environment: userland to kernel privilege escalation, VM escape (Flip Feng Shui style), or mobile privilege escalation (Drammer). Only do this with explicit authorization and in an isolated lab.
6. **Detection & monitoring tests** &mdash; validate whether available mitigations and telemetry (hardware mitigations, ECC, TRR, increased refresh, OS mitigations, performance counter anomalies) detect hammering or flips. Measure false positive/false negative tradeoffs.
7. **Reporting & remediation** &mdash; produce prioritized findings (vulnerable modules, required mitigations, compensating controls) and validate fixes (firmware updates, OS/hypervisor patches, disabling risky features like page deduplication, enabling ECC/targeted refresh).

---

## 3. Security Test Approaches & Tools 


<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Test approach</th>
      <th>Analysis Type</th>
      <th>Approach name</th>
      <th>Testing Tool</th>
      <th>Tool Hyperlink</th>
      <th>Platform</th>
    </tr>
  </thead>
  <tbody>
    <!-- Characterization / measurement -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>DRAM vulnerability detection (hammer tests)</td>
      <td>Google / CMU rowhammer-test / antmicro rowhammer-tester</td>
      <td><a href="https://github.com/google/rowhammer-test">Google / CMU rowhammer-test</a></td>
      <td>Both</td>
    </tr>
    <!-- Browser-based remote attack proof-of-concept -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Remote JS hammer (research / PoC)</td>
      <td>rowhammer.js (research implementation)</td>
      <td><a href="https://github.com/IAIK/rowhammer.js">rowhammer.js (research implementation)</a></td>
      <td>Both</td>
    </tr>
    <!-- Mobile-specific Rowhammer testing -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Android deterministic Rowhammer testing / exploitability</td>
      <td>Drammer (vusec) + Drammer repo</td>
      <td><a href="https://github.com/vusec/drammer">Drammer (vusec) + Drammer repo</a></td>
      <td>Android</td>
    </tr>
    <!-- Cloud/VM attack demonstrators -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Cross-VM disturbance / Flip Feng Shui-style tests</td>
      <td>Flip Feng Shui artifacts / testbed (research)</td>
      <td><a href="https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_razavi.pdf">Flip Feng Shui artifacts</a></td>
      <td>Both (cloud hypervisor)</td>
    </tr>
    <!-- Low-level hardware tests and test suites -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Hardware/firmware test and mitigation validation</td>
      <td>antmicro rowhammer-tester, CMU Rowhammer repo</td>
      <td><a href="https://github.com/antmicro/rowhammer-tester">antmicro rowhammer-tester</a></td>
      <td>Both</td>
    </tr>
    <!-- Stress / memory tools to shape memory allocations -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Memory allocator shaping (force desired physical placement)</td>
      <td>custom allocators, hugepages, memtester, stress-ng</td>
      <td><a href="https://github.com/ckolivas/stress-ng">tress-ng</a></td>
      <td>Both</td>
    </tr>
    <!-- Monitoring / detection -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Performance counter & telemetry monitoring for hammering</td>
      <td>perf / Intel PCM / OS counters / kernel instrumentation</td>
      <td><a href="https://perf.wiki.kernel.org/">perf</a></td>
      <td>Both</td>
    </tr>
    <!-- Fuzz / code review -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Code review of OS/hypervisor features (page dedup, copy-on-write)</td>
      <td>Semgrep / CodeQL / manual code review</td>
      <td><a href="https://semgrep.dev/">Semgrep</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 4. Practical Testbed &mdash; Minimum Safe Configuration

* **Isolated lab network:** fully air-gapped or VLAN + physical isolation with snapshot/rollback capability. Do **not** run any exploitative tests on production systems.
* **Test hardware:** representative systems for each target class: cloud host (hypervisor + guest VMs), Android phones (for Drammer-style tests), edge gateways/IoT devices with DRAM (if applicable). Keep identical hardware to production where possible.
* **DRAM characterization tools:** Google/CMU rowhammer-test, Antmicro rowhammer-tester, CMU Rowhammer repo.
* **Exploit PoCs (research only):** rowhammer.js (for browser tests), Drammer (Android). Only use published PoCs to evaluate whether vulnerabilities are exploitable in your environment &mdash; with permission. 
* **Monitoring & telemetry:** kernel crash dumps, `perf` counters, PCM, syslogs forwarded to a secure collector (Elastic/Splunk).
* **Controlled allocation tools:** stress-ng, memtester, custom allocators/hugepages to shape physical placement and reduce noise.
* **Snapshots and rollback:** VM snapshots and physical disk images so tests are non-destructive and recoverable.

---

## 5. Step-by-step Test Procedures

### A. Preparation

1. Get written authorization and define scope: targeted hosts, permitted PoCs, data handling rules.
2. Prepare snapshots / backups for all DUTs (devices under test). Enable full kernel logging and collect baseline performance counters.
3. Ensure lab isolation &mdash; no accidental internet exposure, and emergency kill switches (power or VM pause).

### B. Characterize susceptibility (non-exploit test)

1. Run `rowhammer-test` / `antmicro rowhammer-tester` on the target host to determine whether bit-flips can be induced and at what aggressiveness thresholds (hammer count, refresh intervals). Record flip patterns (addresses, rows, timing). 
2. Repeat at different temperatures, DRAM frequencies and voltages to map sensitivity (Rowhammer depends on physical conditions). 

### C. Allocation shaping & exploitability

1. Use memory shaping techniques (hugepages, allocation patterns) to co-locate attacker memory with victim pages (for Flip Feng Shui and VM attacks). Research artifacts (Flip Feng Shui) detail techniques for influencing physical placement.
2. Attempt controlled PoC (only inside lab): e.g., run a guest VM hammering rows to see whether you can flip bits in a co-located victim VM (if scope authorizes cross-VM tests). Log progress and abort if unintended behavior occurs.

### D. Mobile tests (Android)

1. On an Android test device, run Drammer per the research instructions to test deterministic hammering on ARM/Android platforms. Verify whether privilege escalation (PoC) is possible **only** if explicitly in scope &mdash; otherwise run non-exploit detection-only mode. 

### E. Browser tests

1. As an additional measurement, run controlled rowhammer.js tests on a test browser/device to evaluate remote attack feasibility. Note that browser vendors mitigate aggressively; results will vary. 

### F. Detection validation

1. Monitor performance counters (cache miss rates, DRAM row activations) and test detection heuristics (e.g., high activation rates, abnormal `perf` metrics). Evaluate whether telemetry reliably signals hammering and whether flip events are visible in logs. 

### G. Mitigation verification

1. Validate deployed mitigations: ECC memory corrects single-bit flips (verify via induced flips), targeted refresh (TRR) or vendor features, disabling page deduplication (KSM), kernel mitigations, or OS / hypervisor patches. Test that mitigations prevent exploitability under comparable hammering conditions. 

---

## 6. References

1. Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., ... & Mutlu, O. (2014). Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. *ACM SIGARCH Computer Architecture News*, 42(3), 361-372. [https://doi.org/10.1145/2678373.2665726](https://doi.org/10.1145/2678373.2665726).
2. Seaborn, M., & Dullien, T. (2015). Exploiting the DRAM rowhammer bug to gain kernel privileges. *Black Hat*, 15(71), 2.
3. Gruss, D., Maurice, C., Mangard, S. (2016). Rowhammer.js: A Remote Software-Induced Fault Attack in JavaScript. In: Caballero, J., Zurutuza, U., Rodríguez, R. (eds) Detection of Intrusions and Malware, and Vulnerability Assessment. DIMVA 2016. *Lecture Notes in Computer Science*, vol 9721. Springer, Cham. [https://doi.org/10.1007/978-3-319-40667-1_15](https://doi.org/10.1007/978-3-319-40667-1_15).
4. Van Der Veen, V., Fratantonio, Y., Lindorfer, M., Gruss, D., Maurice, C., Vigna, G., Bos, H., Razavi, K. & Giuffrida, C. (2016). Drammer: Deterministic rowhammer attacks on mobile platforms. In *Proceedings of the 2016 ACM SIGSAC conference on computer and communications security* (pp. 1675-1689). [https://doi.org/10.1145/2976749.2978406](https://doi.org/10.1145/2976749.2978406).
5. Razavi, K., Gras, B., Bosman, E., Preneel, B., Giuffrida, C., & Bos, H. (2016). Flip feng shui: Hammering a needle in the software stack. In *25th USENIX Security Symposium (USENIX Security 16)* (pp. 1-18). [https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/razavi](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/razavi).
6. Mutlu, O., & Kim, J. S. (2019). Rowhammer: A retrospective. *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, 39(8), 1555-1571. [10.1109/TCAD.2019.2915318](10.1109/TCAD.2019.2915318).