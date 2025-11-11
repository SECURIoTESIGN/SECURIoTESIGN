# Security Testing for VM Migration Attacks

## 1. Overview

A VM Migration Attack targets the process of moving virtual machines (VMs) between physical hosts, exploiting vulnerabilities to compromise data, control, or system stability.

Addressing VM Migration Attack security testing is crucial for maintaining the integrity, confidentiality, and availability of cloud and virtualized environments.

## 2. Security Testing Approaches & Tools

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
      <td>Black-box / Gray-box</td>
      <td>DAST</td>
      <td>Live migration protocol fuzzing (network & RPC)</td>
      <td>FitM / custom middlebox fuzzer</td>
      <td><a href="https://github.com/topics/fuzzer">FitM / network fuzzers (examples)</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Migration stream tampering / MitM proxy</td>
      <td>mitmproxy, socat, tcpreplay</td>
      <td><a href="https://mitmproxy.org">mitmproxy</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Post-copy/resume stalling & resource exhaustion</td>
      <td>custom kernel/guest workloads, stress-ng</td>
      <td><a href="https://github.com/ColinIanKing/stress-ng">stress-ng</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Forensics</td>
      <td>Memory/state tampering & snapshot manipulation</td>
      <td>QEMU snapshot tools, libvirt, vmstate-tooling</td>
      <td><a href="https://www.qemu.org/docs/master/system/migration.html">QEMU migration docs</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Source review for migration code paths (libvirt/QEMU)</td>
      <td>CodeQL, SonarQube, Coverity</td>
      <td><a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Binary</td>
      <td>Fuzzing of migration RPCs / RPC handlers</td>
      <td>AFL/LibAFL harnesses targeting QEMU migration streams</td>
      <td><a href="https://lcamtuf.coredump.cx/afl/">AFL</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST / Network</td>
      <td>Network tracing / packet capture during migration</td>
      <td>Wireshark, tcpdump, Zeek</td>
      <td><a href="https://www.wireshark.org">Wireshark</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST / Runtime</td>
      <td>Runtime integrity & tamper-detection testing</td>
      <td>LibVMI, Volatility</td>
      <td><a href="https://github.com/libvmi/libvmi">LibVMI</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Cloud orchestration / API abuse during migration</td>
      <td>OpenStack client, AWS CLI, Terraform + Burp Suite</td>
      <td><a href="https://www.openstack.org">OpenStack</a></td>
      <td>Both</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Configuration & policy review (encryption/auth)</td>
      <td>Nessus / OpenVAS, CIS Benchmarks</td>
      <td><a href="https://www.openvas.org">OpenVAS</a></td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

## 3. Brief Testing Set-up 

1. **Isolated testbed** &mdash; dedicate physical hosts for source/target hypervisors (KVM/QEMU, Xen, VMware) and an isolated network to avoid impacting production. Use libvirt to orchestrate migration flows. (QEMU/KVM docs are a practical reference). 

2. **Build baseline VM images** &mdash; minimal Linux/Windows guests and representative Android emulator images (QEMU-based). For IoT: use lightweight guests or container-based device images (CRIU for container migration experiments). 

3. **Enable migration modes** &mdash; test pre-copy, post-copy, and block/live migration modes supported by your stack (QEMU has explicit migration states and troubleshooting tips). Record migration control channels (TCP ports / unix sockets). 

4. **Network & MitM testing** &mdash; place a MitM between source and target migration endpoints and attempt: packet corruption, selective drop, replay, injection, or protocol field fuzzing. Use mitmproxy/socat/tcpreplay to manipulate streams and observe failure modes. (Empirical attacks historically exploited unsecured migration channels). 

5. **Stream / state fuzzing** &mdash; fuzz the migration RPC/state machine (e.g., QEMU migration stream) with AFL/LibAFL harnesses or fuzzer-in-the-middle setups that mutate live migration messages; capture crashes and incomplete restores. 

6. **Resource exhaustion & stalling** &mdash; run attacker workloads in guest (e.g., memory churn, hugedirty pages) to attempt migration stalling or amplification attacks (stalled post-copy or forced repeated rounds). Monitor migration progress and host resource consumption; reproduce KVM stalling attacks for research validation. 

7. **Snapshot & snapshot-manipulation attacks** &mdash; create and modify VM snapshots / disk/image state to simulate tampering during offline/online migration; attempt rollback/resume tampering to observe integrity failures. Use QEMU snapshot tooling and libvirt APIs. 

8. **Forensic & detection instrumentation** &mdash; attach LibVMI/Volatility on the target host to inspect guest memory/CPU state after migration; use logs and packet captures to triage whether tampering produced code execution or data corruption. 

9. **SAST & config review** &mdash; review migration code paths (libvirt, QEMU, VMware agents) for insecure defaults, missing encryption/auth, improper length checks, and deserialization issues. Run CodeQL/SonarQube and check cloud orchestration APIs for misconfigurations. 

10. **Reproduce & PoC** &mdash; for every crash/state inconsistency, collect migration logs, full VM snapshots, pcap, guest traces, and step-by-step reproduction on a clean environment. Prepare responsible disclosure or mitigation recommendations.

## 4. References

1. Oberheide, J., Cooke, E., & Jahanian, F. (2008, February). Empirical exploitation of live virtual machine migration. In *Proceeding of Black Hat DC convention* (pp. 1-6). Citeseer: The Pennsylvania State University.
2. Atya, A., Aqil, A., Khalil, K., Qian, Z., Krishnamurthy, S. V., & La Porta, T. F. (2017). Stalling live migrations on the cloud. In *11th USENIX Workshop on Offensive Technologies (WOOT 17)*.
3. Clark, C. et al. (2005). Live migration of virtual machines. In *Proceedings of the 2nd conference on Symposium on Networked Systems Design & Implementation-Volume 2* (pp. 273-286).
4. Casola, V., De Benedictis, A., Rak, M., & Villano, U. (2018, June). Towards automated penetration testing for cloud applications. In 2018 IEEE 27th International Conference on Enabling Technologies: Infrastructure for Collaborative Enterprises (WETICE) (pp. 24-29). IEEE.
5. Rakotondravony, N., Taubmann, B., Mandarawi, W. et al. Classifying malware attacks in IaaS cloud environments. J Cloud Comp 6, 26 (2017). https://doi.org/10.1186/s13677-017-0098-8