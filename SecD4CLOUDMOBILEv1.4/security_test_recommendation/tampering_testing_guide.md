# Security Testing Setup for Tampering Attacks

## 1. Overview

Tampering involves unauthorized modification of code, firmware, configurations, or physical components. In cloud-mobile-IoT ecosystems, testing must span:

- **Mobile apps**: Detect code injection, runtime manipulation, and unauthorized access.
- **IoT devices**: Identify firmware tampering, debug port abuse, and physical bypass.
- **Cloud services**: Validate API integrity, configuration hardening, and deployment security.

### Recommended Testing Layers

1. **Static Analysis (SAST)**: Review source code and binaries for vulnerabilities.
2. **Dynamic Analysis (DAST)**: Monitor runtime behavior and responses to inputs.
3. **Physical Inspection**: Evaluate tamper-resistance of hardware and enclosures.
4. **Network Monitoring**: Detect unauthorized traffic and protocol manipulation.
5. **Penetration Testing**: Simulate real-world attacks across all layers.

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
    <td>Black-box</td>
    <td>DAST</td>
    <td>Pentesting</td>
    <td>Burp Suite</td>
    <td><a href="https://portswigger.net/burp">Burp Suite</a></td>
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
    <td>White-box</td>
    <td>SAST</td>
    <td>Code Review</td>
    <td>SonarQube</td>
    <td><a href="https://www.sonarsource.com/products/sonarqube/">SonarQube</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>Black-box</td>
    <td>DAST</td>
    <td>Web Security Scanner</td>
    <td>OWASP ZAP</td>
    <td><a href="https://owasp.org/www-project-zap/">OWASP ZAP</a></td>
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
    <td>Fuzzing</td>
    <td>Peach Fuzzer</td>
    <td><a href="https://www.peach.tech/">Peach Fuzzer</a></td>
    <td>Both</td>
  </tr>
  <tr>
    <td>White-box</td>
    <td>Physical Review</td>
    <td>Physical Security Measures Review</td>
    <td>IoT Inspector</td>
    <td><a href="https://www.iot-inspector.com/">IoT Inspector</a></td>
    <td>IoT</td>
  </tr>
</table>

---

## References

1. Sequeiros, J. B. F., Chimuco, F. T., Samaila, M. G., Freire, M. M., & Inácio, P. R. M. (2020). Attack and system modeling applied to IoT, cloud, and mobile ecosystems: Embedding security by design. *ACM Computing Surveys*, 53(2), Article 25. https://doi.org/10.1145/3376123
2. Chimuco, F. T., Sequeiros, J. B. F., Lopes, C. G., Simões, T. M. C., Freire, M. M., & Inácio, P. R. M. (2023). Secure cloud-based mobile apps: Attack taxonomy, requirements, mechanisms, tests and automation. *International Journal of Information Security*, 22, 833–867. https://doi.org/10.1007/s10207-023-00669-z
3. Bella, G., Biondi, P., Bognanni, S., & Esposito, S. (2023). Petiot: Penetration testing the internet of things. *Internet of Things*, 22, 100707.
4. Yadav, G., Allakany, A., Kumar, V., Paul, K., & Okamura, K. (2019, July). Penetration testing framework for iot. In *2019 8th International Congress on Advanced Applied Informatics (IIAI-AAI)* (pp. 477-482). IEEE.
