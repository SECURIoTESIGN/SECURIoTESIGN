# Meltdown Attack Model

## Definition

**Meltdown** is a microarchitectural, speculative-execution side-channel vulnerability that allows unprivileged code to infer contents of privileged memory (kernel, hypervisor, or co-tenant memory) by exploiting out-of-order execution side effects. In cloud, mobile and IoT contexts it threatens confidentiality of keys, credentials and sensitive data in co-resident VMs/containers, native mobile components, and embedded device firmware/processes.

---

## Relevant attack categories (cloud / mobile / IoT specifics)

* **Co-tenant VM/container attacks (cloud):** attacker runs crafted native code in a VM/container on a shared host to read host/kernel or other guest memory.
* **Guest→host or guest→guest leakage (hypervisor weakness):** compromises secrets across tenant boundaries on vulnerable hosts.
* **Native/mobile app exploitation:** apps with native code (or JIT engines) on mobile devices that can execute crafted sequences to leak OS or other app memory (mitigations vary by OS).
* **Compromised IoT firmware / local code execution:** where an attacker can run code locally (malware, compromised service, or rogue update) to read kernel or other process memory on embedded devices.
* **Chained attacks:** use leaked secrets (API keys, tokens) to escalate to cloud control planes, provisioned services, or lateral movement across IoT fleets.

---

## Mitigations & defensive controls

* **Apply vendor patches & microcode updates** (KPTI, microcode fixes) promptly on servers, mobile OS, and device firmware.
* **Cloud tenancy controls:** use dedicated hosts for high-sensitivity tenants, enforce cloud provider isolation features, and prefer VMs over weaker isolation when needed.
* **Disable SMT/Hyperthreading** on hosts where strict confidentiality is required (trade-off: performance).
* **Harden execution environments:** minimize native/untrusted code execution, restrict JIT usage in untrusted contexts, disable features that expose high-resolution timers.
* **Browser & mobile hardening:** update browsers/webviews (site isolation, JIT mitigations), apply OS updates and vendor mitigations.
* **IoT hardening:** secure boot, signed firmware, network segmentation, restrict ability to run arbitrary native code, and decommission unpatchable devices.
* **Operational:** inventory vulnerable CPU families, track patch/microcode deployment status, and monitor for anomalous post-leak behaviors (unexpected credential use).

---

## DREAD Risk Assessment (scores 0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                       |
| ---------------- | -----------: | ------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |            9 | Can expose kernel secrets, cryptographic keys and cross-tenant secrets — leading to large breaches.                             |
| Reproducibility  |            8 | Well-documented PoCs exist and techniques are reproducible on vulnerable platforms.                                             |
| Exploitability   |            7 | Requires ability to execute native/unprivileged code on target (achievable in many cloud, IoT, or compromised mobile contexts). |
| Affected Users   |            8 | Multi-tenant cloud hosts, fleets of IoT devices, or many mobile users (depending on app/native code exposure) can be impacted.  |
| Discoverability  |            6 | Vulnerable hardware/firmware presence is discoverable, but detecting active exploitation is difficult (side-channel stealth).   |

**Digit-by-digit arithmetic (explicit):**
Sum = 9 + 8 + 7 + 8 + 6 = 38.
Average = 38 / 5 = 7.6.

**DREAD average = 7.6**; Rating: **High / Critical**

### Detection signals & short playbook

**Detection signals:** unexpected use of stolen credentials, sudden abnormal accesses post-exploit, inventory of unpatched hosts, or anomaly in process/kernel timing (detection of exploitation itself is very hard).
**Immediate (0–6 hrs):** confirm patch/microcode status across estate, isolate unpatched high-value hosts (dedicated hosts or pause co-tenants), apply mitigations (KPTI, microcode), and disable SMT where required.
**Short term (days–weeks):** deploy patches broadly, update browsers/OS/firmware, review service exposure to native code execution, and require dedicated hosts for critical workloads.
**Long term:** retire vulnerable CPU generations where feasible, integrate speculative-execution risk into architecture decisions, and maintain continuous patch/microcode monitoring.

---

## References

1. Lipp, M., Schwarz, M., Gruss, D., Prescher, T., Haas, W., Fogh, A., Horn, J., Mangard, S., et al. (2018). *Meltdown: Reading kernel memory from user space.* In *Proceedings of the 27th USENIX Security Symposium* (pp. 973–990). USENIX Association. [https://www.usenix.org/conference/usenixsecurity18/presentation/lipp](https://www.usenix.org/conference/usenixsecurity18/presentation/lipp)
2. Google Project Zero. (2018). *Meltdown & Spectre* (research website). [https://meltdownattack.com/](https://meltdownattack.com/)
3. National Vulnerability Database. (2018). *CVE-2017-5754 — Rogue Data Cache Load (Meltdown).* NVD. [https://nvd.nist.gov/vuln/detail/CVE-2017-5754](https://nvd.nist.gov/vuln/detail/CVE-2017-5754)
4. Intel Corporation. (2018). *Rogue Data Cache Load (Meltdown) — advisory and software mitigations.* Intel. [https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/advisory-guidance/rogue-data-cache-load.html](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/advisory-guidance/rogue-data-cache-load.html)

---
          |

## Meltdown Attack Tree Diagram

