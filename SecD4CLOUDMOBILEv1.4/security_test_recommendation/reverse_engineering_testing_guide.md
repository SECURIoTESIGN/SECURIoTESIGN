# Security Testing Setup for Reverse Engineering Attacks

## 1. Overview

Reverse engineering involves disassembling or analyzing applications, binaries, or firmware to understand internal logic, extract sensitive data, or modify behavior. In cloud-mobile-IoT environments, attackers may:

- **Decompile mobile apps** to extract API keys or bypass logic.
- **Analyze firmware** to find hardcoded credentials or debug interfaces.
- **Intercept cloud communication** to reverse protocols or authentication flows.

### Recommended Testing Layers

1. **Static Analysis (SAST)**: Disassemble and inspect code or firmware for secrets, logic flaws, or insecure configurations.
2. **Dynamic Analysis (DAST)**: Monitor runtime behavior, memory, and network traffic for tampering or reverse engineering attempts.
3. **Physical Inspection**: Evaluate hardware for debug ports, unprotected storage, or firmware extraction vectors.
4. **Penetration Testing**: Simulate reverse engineering scenarios using emulators, patching, and instrumentation.

---

## 2. Security Testing Approach & Tools

<table border="1" cellpadding="6" cellspacing="0">
  <tr>
    <th>Test Approach</th>
    <th>Analysis Type</th>
    <th>Approach Name</th>
    <th>Testing Tool</th>
    <th>Tool Hyperlink</th>
    <th>Platform</th>
  </tr>
  <tr>
    <td>White-box</td>
    <td>SAST</td>
    <td>Code Review</td>
    <td>Ghidra</td>
    <td><a href="https://ghidra-sre.org/">Ghidra</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>Gray-box</td>
    <td>SAST</td>
    <td>Code Security Scanner</td>
    <td>MobSF</td>
    <td><a href="https://github.com/MobSF/Mobile-Security-Framework-MobSF">MobSF</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>Black-box</td>
    <td>DAST</td>
    <td>Fuzzing</td>
    <td>Peach Fuzzer</td>
    <td><a href="https://www.peach.tech/">Peach Fuzzer</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>Gray-box</td>
    <td>DAST</td>
    <td>Network Packet Sniffing</td>
    <td>Wireshark</td>
    <td><a href="https://www.wireshark.org/">Wireshark</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>Black-box</td>
    <td>DAST</td>
    <td>Pentesting</td>
    <td>Frida</td>
    <td><a href="https://frida.re/">Frida</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>White-box</td>
    <td>SAST</td>
    <td>Firmware Analysis</td>
    <td>Binwalk</td>
    <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a></td>
    <td>IoT</td>
  </tr>
  <tr>
    <td>White-box</td>
    <td>Physical Review</td>
    <td>Physical Security Measures Review</td>
    <td>ChipWhisperer</td>
    <td><a href="https://chipwhisperer.io/">ChipWhisperer</a></td>
    <td>IoT</td>
  </tr>
</table>


---

## 3. References

1. Sequeiros, J. B., Chimuco, F. T., Samaila, M. G., Freire, M. M., & Inácio, P. R. (2020). Attack and system modeling applied to IoT, cloud, and mobile ecosystems: Embedding security by design. *ACM Computing Surveys (CSUR)*, 53(2), 1-32.
2. Elsayed, E. K., ElDahshan, K. A., El-Sharawy, E. E., & Ghannam, N. E. (2019). Reverse engineering approach for improving the quality of mobile applications. *PeerJ Computer Science*, 5, e212.
3. Shwartz, O., Mathov, Y., Bohadana, M., Elovici, Y., & Oren, Y. (2018). Reverse engineering IoT devices: Effective techniques and methods. *IEEE Internet of Things Journal*, 5(6), 4965-4976.
4. Franke, D., Elsemann, C., Kowalewski, S., & Weise, C. (2011, October). Reverse engineering of mobile application lifecycles. In *2011 18th Working Conference on Reverse Engineering* (pp. 283-292). IEEE.
5. Albakri, A., Fatima, H., Mohammed, M., Ahmed, A., Ali, A., Ali, A., & Elzein, N. M. (2022). Survey on Reverse‐Engineering Tools for Android Mobile Devices. *Mathematical Problems in Engineering*, 2022(1), 4908134.
6. Chavan, N., Patel, H., & Shah, K. (2025). Comprehensive Approach to Android Penetration Testing: Techniques, Tools and Best Practices for Securing Mobile Applications. In *2025 12th International Conference on Computing for Sustainable Global Development (INDIACom)* (pp. 01-07). IEEE.
