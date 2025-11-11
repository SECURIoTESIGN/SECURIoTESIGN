# Rowhammer Attack 

## Definition

**Rowhammer** is a microarchitectural hardware fault-induction attack that repeatedly accesses (*hammers*) DRAM rows to cause bit-flips in adjacent memory rows. Attackers exploit these induced flips to corrupt data or flip security-critical bits (e.g., page tables, permissions) and thereby escalate privileges, break isolation between tenants, or tamper firmware/keys. Variants run locally (native code), in sandboxed environments (JIT/JavaScript), or via malicious firmware on IoT devices.

---

## Attack Categories 

* **Local native Rowhammer:** attacker executes tight memory access patterns in an unprivileged process (VM/ container) to flip kernel or co-tenant data. (Cloud multi-tenancy threat.)
* **Browser / JIT variants (remote):** using high-resolution timers and JIT optimizations (Rowhammer.js) to perform attack from JavaScript — impacts mobile browsers and webviews.
* **Firmware / embedded Rowhammer:** malware on IoT devices or malicious firmware triggers bit flips to alter device behaviour or extract secrets.
* **Cross-VM/tenant attacks:** co-resident VMs or containers on same physical host cause bit-flips in neighbor VMs (cloud confidentiality/integrity risk).
* **Targeted data corruption:** precise targeting of page table entries, crypto key material or attestation state to subvert trust anchors.

---

## Mitigations & Defensive Controls

**Hardware & platform**

* **ECC DRAM:** use ECC memory (correctable and detectable errors) in servers and critical gateways. (Note: ECC may not prevent all flips but reduces risk.)
* **Memory controller mitigations:** enable vendor TRR/targeted row refresh, increased DRAM refresh rates, or other hardware fixes where supported.
* **Dedicated hosts / CPU pinning:** avoid untrusted co-residency (dedicated physical hosts for sensitive tenants/services).

**OS / hypervisor / runtime**

* **Physical isolation:** place untrusted workloads in separate NUMA/physical banks when possible.
* **Memory allocation hardening:** avoid predictable placement of security-critical structures adjacent to attacker-controlled pages; use guard rows / hole-punching for sensitive allocations.
* **Disable or restrict JIT/High-res timers:** restrict JIT compilation and high-resolution timers in untrusted web contexts (browsers implemented mitigations after Rowhammer.js).
* **Process / container hardening:** limit unprivileged processes’ ability to do repeated cache bypassing; use kernel-level throttles on memory access patterns if feasible.

**IoT / mobile**

* **Firmware updates:** apply microcode/firmware and SoC vendor mitigations where available.
* **Hardened device design:** prefer SoCs with hardware rowhammer mitigations, use secure boot/attestation so flipped bits cannot subvert measured boot, and isolate critical keys in secure elements.
* **Limit native code exposure:** avoid installing unknown native modules; enforce app store vetting and runtime integrity checks on mobile/embedded platforms.

**Detection & monitoring**

* Monitor corrected ECC counts, DRAM error rates and sudden bursts of correctable errors; set alerts for anomalous error patterns.
* Watch for suspicious high-frequency memory access patterns from a process or VM, unexplained crashes, or integrity verification failures (measured boot mismatches).

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                                     |
| ---------------- | -----------: | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **9** | Can yield privilege escalation, cross-tenant data compromise, and persistent integrity subversion (kernel, hypervisor, keys).                 |
| Reproducibility  |        **7** | Proven in many DRAM generations and across platforms; success depends on specific DRAM chips, placement and noise — reproducible with effort. |
| Exploitability   |        **7** | Requires ability to execute tight memory access patterns or run JIT code (feasible in many cloud, browser and some IoT contexts).             |
| Affected Users   |        **8** | Multi-tenant cloud services, fleets of IoT devices, and mobile users (via browsers) can be impacted at scale.                                 |
| Discoverability  |        **5** | Silent bit-flips are stealthy; detection relies on ECC/monitoring or integrity checks — active exploitation can be hard to observe.           |

**Digit-by-digit arithmetic (explicit):**
Sum = 9 + 7 + 7 + 8 + 5 = **36**.
Average = 36 / 5 = **7.2**.

**DREAD average = 7.2**; Rating: **High Risk**.

---

## References

1. Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., et al. (2014). *Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors.* Proceedings of the 41st International Symposium on Computer Architecture (ISCA).
2. Seaborn, M., & Dullien, T. (2015). *Exploiting the DRAM Rowhammer Bug to Gain Kernel Privileges.* (Technical report / exploit write-up).
3. Gruss, D., Maurice, C., & Mangard, S. (2016). *Rowhammer.js: A Remote Software-Induced Fault Attack in JavaScript.* (Conference/whitepaper describing JIT/browser variant).
4. Bitar, N., Heninger, N., Lipp, M., et al. (2019). *Survey and Mitigations for DRAM Disturbance and Rowhammer.* (Survey and mitigation recommendations).

---


## Rowhammer Attack Tree Diagram