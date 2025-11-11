# Cache Poisoning Attack Model

## Definition

A **Cache Poisoning Attack** occurs when an attacker injects malicious or incorrect data into a cache (e.g., DNS, HTTP, CDN), causing users or systems to retrieve and act on falsified content. In cloud, mobile, and IoT ecosystems, poisoned caches can redirect traffic, serve malicious payloads, or disrupt service availability.

---

## Attack Categories

| **Category**               | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **DNS Cache Poisoning**    | Injects false DNS records to redirect users to malicious domains.               |
| **HTTP Cache Poisoning**   | Manipulates HTTP headers or requests to store malicious responses in shared caches. |
| **CDN Cache Manipulation** | Exploits edge caching rules to serve altered content across distributed networks. |
| **IoT Firmware Cache Abuse** | Delivers outdated or malicious firmware updates via poisoned cache endpoints.   |
| **Mobile App API Poisoning** | Alters cached API responses to mislead mobile apps or trigger faulty behavior.   |

---

## Mitigation Strategies

| **Layer**            | **Mitigation**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| **DNS Level**        | Use DNSSEC, validate responses, minimize TTLs for sensitive records.           |
| **HTTP/CDN Level**   | Sanitize headers, enforce cache key normalization, avoid caching user-specific content. |
| **App Level**        | Validate cached data before use, apply integrity checks, use secure update channels. |
| **IoT Firmware**     | Sign firmware updates, verify hash before installation, avoid caching sensitive binaries. |
| **Cloud Infrastructure** | Monitor cache behavior, isolate cache layers, apply WAF rules to block poisoning vectors. |

---

## Risk Assessment (DREAD Model)

| **Category**         | **Assessment**                                                                 | **Score (1-10)** |
|----------------------|---------------------------------------------------------------------------------|------------------|
| **Damage Potential** | Can redirect users to malicious sites, serve malware, or disrupt critical services. | **8**            |
| **Reproducibility**  | Easily repeatable if cache rules are misconfigured or validation is weak.       | **8**            |
| **Exploitability**   | Moderate skill required; many known techniques and tools exist.                 | **7**            |
| **Affected Users**   | All users relying on poisoned cache entries, potentially thousands or millions. | **8**            |
| **Discoverability**  | Often difficult to detect until users report anomalies or security audits are performed. | **7**            |

**Total DREAD Score: 38 / 5 = 7.6**; Rating: **High Risk**.

---

## References

1. [OWASP Caching Guide](https://owasp.org/www-project-secure-headers/#cache-control)
2. NIST SP 800-53: System and Communications Protection
3. ENISA Threat Landscape Report 2023 – [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
4. IEEE Security & Privacy: Cache Poisoning in Distributed Systems (2022)
5. [Mitre ATT&CK Framework - Network Service Manipulation](https://attack.mitre.org/techniques/T1557/)
6. SANS Institute: DNS and HTTP Cache Poisoning Attacks Whitepapers
7. Klein, A. (2011). Web Cache Poisoning Attacks. In: van Tilborg, H.C.A., Jajodia, S. (eds) Encyclopedia of Cryptography and Security. Springer, Boston, MA. https://doi.org/10.1007/978-1-4419-5906-5_666

---

## Cache Poisoning Attack Tree Diagram





