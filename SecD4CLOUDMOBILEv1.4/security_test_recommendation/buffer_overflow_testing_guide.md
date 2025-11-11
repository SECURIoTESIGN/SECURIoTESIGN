# Security Testing Setup for Buffer Overflow Attacks

## 1. Overview 

Always run these tests in an isolated lab or on systems you own / have explicit written authorization for. Buffer overflow testing (fuzzing, exploit development, emulation) can crash devices and services and may cause data loss &mdash; back up firmware and images and follow the lab safety checklist below.

**High-level Testing objective**

Find, reproduce and classify buffer overflow vulnerabilities (heap, stack, global) in:

* cloud services / server binaries (C/C++ backends),
* mobile native code / native libraries used by Android/iOS (NDK code, shared libraries),
* IoT firmware and embedded binaries (MIPS/ARM/etc).
  Use a mix of **white-box** (SAST + instrumented builds), **gray-box** (coverage-guided fuzzing), and **black-box** (binary-only fuzzing, network fuzzing, emulation-based) methods. Use sanitizers & instrumentation for faster triage and debugging. Key techniques: static analysis, compile-time instrumentation (ASan/UBSan), coverage-guided fuzzing (AFL/libFuzzer/honggfuzz/AFL++), emulation (QEMU/FIRMADYNE), dynamic analysis (Valgrind), and runtime hooking (Frida / gdbserver) for mobile/IoT.

Key references that motivated this plan (fuzzing / ASLR / StackGuard / emulation): Manès et al. (fuzzing survey), Shacham et al. (ASLR effectiveness), Cowan et al. (StackGuard), Liang & Sekar (buffer overflow signatures), Chen et al. (FIRMADYNE for firmware emulation).

---

## 2. Lab & instrumentation

* Isolated cloud project(s) and VLANs; separate test accounts for cloud workloads.
* Device pool: Android devices (real + emulator), iOS test devices (if you have tooling to instrument), IoT devices or firmware images.
* Build environment: ability to build instrumented binaries (clang/llvm with `-fsanitize=address,undefined`), or instrumented QEMU images. Use OSS-Fuzz style instrumentation when possible. (ASan + coverage is essential for modern fuzzing.)
* Emulation: QEMU + Firmadyne / firmware-analysis tooling to run embedded images and attach fuzzers.
* Monitoring: PCAP (SPAN/mirror) point, central logging (ELK/Splunk), snapshot/restore ability for devices/firmware images.
* Safety: backups of firmware, power control to reset devices after crashes, ESD & electrical safety when opening hardware.

---

## 3. Practical Testing Workflow

Phase A &mdash; **Recon & target selection**

* Inventory binaries, versions, exposed services, relevant native libraries (NDK .so files), and firmware images.

Phase B &mdash; **Source / SAST / build hardening** (White-box)

* Run source static analysis on C/C++ (clang-analyzer, Coverity if available) and compile instrumented builds with AddressSanitizer / UBSan / SanitizerCoverage for fuzzing targets. Use `-g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer`.

Phase C &mdash; **Fuzzing (gray/white-box)**

* For library functions and APIs: use **libFuzzer** (in-process) or **AFL++/AFL** or **honggfuzz** for binary/executable fuzzing; seed corpora, enable ASan to catch OOB & use-after-free quickly. For network services, wrap input harnesses or use AFL-NET/aflplusplus network modes.

Phase D &mdash; **Binary + firmware emulation fuzzing (black/gray-box)**

* Extract firmware (Binwalk), rehost/emulate in Firmadyne / QEMU, and run AFL++/honggfuzz or integrate libFuzzer harnesses into emulated environment; capture crashes & triage with ASan/Valgrind and GDB.

Phase E &mdash; **Runtime triage & debugging**

* Use AddressSanitizer/Valgrind to identify root cause of crashes; use GDB (gdbserver for remote/mobile), `pwndbg`/`gef` for exploit triage and stack analysis. For mobile: use `gdbserver` (Android) + Frida for hooking in runtime.

Phase F &mdash; **Exploit simulation & detection validation**

* Once the bug is confirmed, simulate controlled exploitation in a sandbox (do NOT deploy exploits in production), generate detections (SIEM/IDS), and document required mitigations (bounds checking, ASan failures, safe libs, compile options). Provide CVE-ready writeups if appropriate.

---

# 4. Playbook &mdash; Concrete Steps & Sample Commands

1. **Inventory & target selection**

   * Identify server binaries, native libs, and firmware images. On Android, extract `.so` from APK:
     `unzip myapp.apk lib/arm64-v8a/*.so -d extracted_libs/`
2. **Prepare instrumented builds**

   * Rebuild server/native lib with ASan & UBSan:
     `clang -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer -shared -o libtarget.so target.c`
   * For libFuzzer harness, write `extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) { /* call parse()/process */ }` and compile with libFuzzer.
3. **Coverage-guided fuzzing**

   * libFuzzer: run the fuzzing binary directly (it is in-process).
   * AFL++: use `afl-fuzz -i seeds/ -o findings/ -- ./target @@` or compile with AFL instrumentation and run.
4. **Firmware fuzzing (emulation)**

   * Extract firmware (Binwalk), rehost via Firmadyne/QEMU, and attach AFL++ or honggfuzz to the emulated I/O entry points. Use snapshots to revert after crashes.
5. **Triage crashes**

   * Use ASan reports (files) or run crashed binary under Valgrind or GDB for further info:
     `gdb --args ./target <crash-input`> and inspect registers/stack. Use `gdbserver` for remote Android native debugging.
6. **Automated dedup & minimization**

   * Use `afl-cmin` / libFuzzer minimization to reduce size of crashing inputs.
7. **Exploit simulation (lab only)**

   * If desired and authorized, attempt controlled exploitation in sandbox to assess impact, then generate mitigations and detection rules. **Do not** deploy exploit code outside the lab.

---

## 5. Security Testing Approach & Tools


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
    <tr>
      <td>White-box</td>
      <td>SAST / Build-time</td>
      <td>Compile-time sanitizers (detect OOB / UAF)</td>
      <td>AddressSanitizer (ASan)</td>
      <td><a href="https://clang.llvm.org/docs/AddressSanitizer.html" target="_blank" rel="noopener">https://clang.llvm.org/docs/AddressSanitizer.html</a></td>
      <td>Both (server, mobile native libs)</td>
    </tr>
    <tr>
      <td>White-box / Gray-box</td>
      <td>DAST (coverage-guided)</td>
      <td>In-process coverage-guided fuzzing for libraries</td>
      <td>libFuzzer</td>
      <td><a href="https://llvm.org/docs/LibFuzzer.html" target="_blank" rel="noopener">https://llvm.org/docs/LibFuzzer.html</a></td>
      <td>Both (native libraries, mobile NDK)</td>
    </tr>
    <tr>
      <td>Gray-box / Black-box</td>
      <td>DAST (coverage-guided)</td>
      <td>Binary/executable fuzzing (corpus + forkserver)</td>
      <td>AFL / AFL++</td>
      <td><a href="https://aflplus.plus/" target="_blank" rel="noopener">https://aflplus.plus/</a></td>
      <td>Both (server, IoT firmware via emulation)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Security-oriented feedback fuzzing</td>
      <td>honggfuzz</td>
      <td><a href="https://honggfuzz.dev/" target="_blank" rel="noopener">https://honggfuzz.dev/</a></td>
      <td>Both (binaries, fuzzing harnesses)</td>
    </tr>
    <tr>
      <td>Black-box / Firmware</td>
      <td>Binary analysis / Emulation</td>
      <td>Firmware extraction & static inspection</td>
      <td>Binwalk</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk" target="_blank" rel="noopener">https://github.com/ReFirmLabs/binwalk</a></td>
      <td>IoT firmware images</td>
    </tr>
    <tr>
      <td>Black-box / Firmware</td>
      <td>DAST (emulation)</td>
      <td>Firmware emulation & dynamic testing</td>
      <td>Firmadyne (firmware emulation)</td>
      <td><a href="https://github.com/firmadyne/firmadyne" target="_blank" rel="noopener">https://github.com/firmadyne/firmadyne</a></td>
      <td>IoT firmware (Linux-based)</td>
    </tr>
    <tr>
      <td>Gray-box / Emulation</td>
      <td>DAST / Dynamic</td>
      <td>Generic machine emulator (rehost & fuzz)</td>
      <td>QEMU</td>
      <td><a href="https://www.qemu.org/" target="_blank" rel="noopener">https://www.qemu.org/</a></td>
      <td>IoT firmware, cross-arch binaries</td>
    </tr>
    <tr>
      <td>White-box / Dynamic</td>
      <td>DAST / Runtime</td>
      <td>Memory debugging, leak & invalid access detection</td>
      <td>Valgrind (Memcheck)</td>
      <td><a href="https://valgrind.org/" target="_blank" rel="noopener">https://valgrind.org/</a></td>
      <td>Both (host binaries; limited on some embedded targets)</td>
    </tr>
    <tr>
      <td>Gray-box / Triage</td>
      <td>Debugging / Exploit analysis</td>
      <td>Source & binary debugging</td>
      <td>GDB / gdbserver (with pwndbg/gef)</td>
      <td><a href="https://www.gnu.org/software/gdb/" target="_blank" rel="noopener">https://www.gnu.org/software/gdb/</a></td>
      <td>Both (server, Android NDK via gdbserver)</td>
    </tr>
    <tr>
      <td>Gray-box / Runtime</td>
      <td>Instrumentation / Hooking</td>
      <td>Runtime hooking & instrumentation (mobile)</td>
      <td>Frida</td>
      <td><a href="https://frida.re/" target="_blank" rel="noopener">https://frida.re/</a></td>
      <td>Android, iOS (for instrumentable targets)</td>
    </tr>
    <tr>
      <td>White-box / Static</td>
      <td>SAST</td>
      <td>Source static analysis (C/C++)</td>
      <td>Clang Static Analyzer / clang-tidy</td>
      <td><a href="https://clang.llvm.org/extra/clang-tidy/" target="_blank" rel="noopener">https://clang.llvm.org/extra/clang-tidy/</a></td>
      <td>Both (server, mobile native source)</td>
    </tr>
    <tr>
      <td>Gray-box / Binary RE</td>
      <td>SAST / DAST</td>
      <td>Reverse engineering & disassembly</td>
      <td>radare2 / Cutter</td>
      <td><a href="https://www.radare.org/n/" target="_blank" rel="noopener">https://www.radare.org/n/</a></td>
      <td>Both (binaries, firmware)</td>
    </tr>
    <tr>
      <td>Black-box / Network</td>
      <td>DAST / Passive</td>
      <td>Packet capture for crash reproduction & protocol fuzzing</td>
      <td>Wireshark</td>
      <td><a href="https://www.wireshark.org/" target="_blank" rel="noopener">https://www.wireshark.org/</a></td>
      <td>Network (all targets)</td>
    </tr>
    <tr>
      <td>Gray-box / Fuzz orchestration</td>
      <td>DAST</td>
      <td>Automated fuzzing harnesses & infrastructure</td>
      <td>OSS-Fuzz (integration / continuous fuzzing)</td>
      <td><a href="https://google.github.io/oss-fuzz/" target="_blank" rel="noopener">https://google.github.io/oss-fuzz/</a></td>
      <td>Server & library projects (open source)</td>
    </tr>
  </tbody>
</table>

---

## 6. References

1. Bierbaumer, B., Kirsch, J., Kittel, T., Francillon, A., Zarras, A. (2018). Smashing the Stack Protector for Fun and Profit. In: Janczewski, L., Kutyłowski, M. (eds) ICT Systems Security and Privacy Protection. SEC 2018. IFIP Advances in Information and Communication Technology, vol 529. Springer, Cham. [https://doi.org/10.1007/978-3-319-99828-2_21](https://doi.org/10.1007/978-3-319-99828-2_21).
2. Cowan, C., Pu, C., Maier, D., Walpole, J. et al. (1998). Stackguard: Automatic adaptive detection and prevention of buffer-overflow attacks. In *USENIX security symposium* (Vol. 98, pp. 63-78).
3. Manès, V. J., Han, H., Han, C., Cha, S. K., Egele, M., Schwartz, E. J., & Woo, M. (2019). The art, science, and engineering of fuzzing: A survey. *IEEE Transactions on Software Engineering*, 47(11), 2312-2331.
4. Shacham, H., Page, M., Pfaff, B., Goh, E. J., Modadugu, N., & Boneh, D. (2004, October). On the effectiveness of address-space randomization. In Proceedings of the 11th ACM conference on Computer and communications security (pp. 298-307).
5. Liang, Z., & Sekar, R. (2005, December). Automatic generation of buffer overflow attack signatures: An approach based on program behavior models. In 21st Annual Computer Security Applications Conference (ACSAC'05) (pp. 10-pp). IEEE. 
6. Chen, D. D., Woo, M., Brumley, D., & Egele, M. (2016, February). Towards automated dynamic analysis for linux-based embedded firmware. In NDSS (Vol. 1, pp. 1-1).
7. Kuperman, B. A., Brodley, C. E., Ozdoganoglu, H., Vijaykumar, T. N., & Jalote, A. (2005). Prevention and Detection of Stack Buffer Overflow Attacks. Prevention and Detection of Stack Buffer Overflow Attacks. 

