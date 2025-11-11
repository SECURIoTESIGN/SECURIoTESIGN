# Pharming Attack Model

## Definition

**Pharming** is an attack that redirects users or devices from legitimate network resources to attacker-controlled endpoints — typically by corrupting name-resolution or provisioning mechanisms (DNS cache poisoning, rogue DHCP, hosts-file modification, or compromised resolvers). Unlike phishing (which lures users with malicious links), pharming **breaks or subverts the name-to-address mapping** so victims transparently connect to fraudulent cloud APIs, update servers, or IoT backends and disclose credentials, tokens or telemetry.

---

## Attack Categories

* **DNS cache poisoning / spoofing:** corrupting recursive resolver caches so domain names resolve to attacker IPs.
* **Compromised authoritative DNS / zone takeover:** attacker obtains control of DNS zone (compromised registrar, DNS provider) and points services to malicious hosts.
* **Rogue/compromised recursive resolver (ISP or enterprise):** attacker controls or poisons resolver used by many clients.
* **Rogue DHCP / network gateway (MITM + DHCP):** on local networks an attacker supplies malicious DNS settings via DHCP to force clients to a malicious resolver.
* **Hosts-file / firmware modification on device:** local modification on mobile or IoT device (malware or tampering) causing name overrides.
* **Compromised provisioning / bootstrap servers:** attacker subverts device provisioning (e.g., supply-chain or CI/CD) to ship devices with malicious DNS endpoints or certificate trust anchors.
* **TLS/PKI misuse combined with pharming:** attacker uses fraudulent certs (compromised CA, misplaced trust anchors) so redirected traffic appears secure.

---

## Mitigations & Defensive Controls

**DNS & network layer**

* **DNSSEC** for authoritative zones and resolvers to validate DNS data integrity end-to-end.
* **Use trusted recursive resolvers / DoH/DoT:** employ DNS-over-TLS or DNS-over-HTTPS with authenticated resolvers and pin resolver endpoints where possible.
* **Harden registrar/DNS-provider accounts:** MFA, registrar lock, monitoring for unauthorized zone changes and two-person approval for zone changes.
* **Egress/NGFW rules:** whitelist DNS servers and block arbitrary DNS port egress; detect unusual DNS server configs via DHCP.
* **Network segmentation & secure DHCP:** restrict DHCP providers, use 802.1X for network access to prevent rogue DHCP, and monitor DHCP leases for unexpected options.

**Endpoint & application**

* **Strict TLS & certificate validation:** enforce certificate validation, certificate transparency monitoring, HSTS and reject connections with invalid certs.
* **Pinning & mTLS:** use certificate pinning or mTLS (mutual TLS) for device↔cloud authentication so simple redirect cannot impersonate services.
* **Avoid hardcoded insecure DNS / fallback logic:** devices should not silently accept arbitrary DNS changes; require authenticated reconfiguration.
* **Secure provisioning & attestation:** bind onboarding to out-of-band secrets, signed manifests and hardware-backed device identity to prevent boot-time redirects.

**Cloud & backend**

* **Endpoint allowlisting & token binding:** require device identity attestation and bind short-lived tokens to device credentials or mTLS sessions.
* **Monitor for anomalous client IPs / resolver patterns:** correlate incoming requests with expected resolver pools and geolocation.
* **Zone-change monitoring & rollback:** log and alert on DNS zone edits and enable rapid rollback and emergency delegation control.

**Operational & detection**

* **Logging & alerting:** monitor DNS query patterns, sudden spikes in NXDOMAIN or unusual TTLs, and certificate validation failures; integrate resolver telemetry with SIEM.
* **Incident playbooks & registrar contacts:** maintain registrar/hosting provider contacts and pre-authorised emergency steps (domain lock, registrar recovery).
* **User/device education & hardening:** instruct users to avoid unknown Wi-Fi for sensitive flows; for managed devices use MDM policies to lock network settings.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor         | Score (0-10) | Rationale                                                                                                                                                                |
| -------------------- | -----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Damage Potential** |        **8** | Redirected traffic can expose credentials, tokens, firmware images, and telemetry — enabling large-scale account takeover, device compromise or fraudulent provisioning. |
| **Reproducibility**  |        **8** | DNS/DHCP-based redirection techniques are well-known and can be automated (rogue resolvers, poisoned caches, rogue DHCP).                                                |
| **Exploitability**   |        **7** | Requires access to DNS chain (resolver, registrar) or local network; many environments historically had weak controls.                                                   |
| **Affected Users**   |        **8** | Resolver/zone compromises can affect many users/devices (ISP customers, enterprise endpoints, device fleets).                                                            |
| **Discoverability**  |        **7** | Name-resolution anomalies and unexpected certs are detectable, but silent exploitation (valid-looking certs, transient DHCP) can delay detection.                        |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 8 + 7 = **38**.
Average = 38 / 5 = **7.6**; Rating: **High / Critical**

---

## References

1. Ristic, I. (2016). *DNS Security: Defending the Domain Name System.* O’Reilly Media.
2. OWASP Foundation. (2023). *OWASP Cheat Sheet: DNS Security and Best Practices.* OWASP. [https://owasp.org/](https://owasp.org/)
3. National Institute of Standards and Technology. (2020). *NIST SP 800-81: Secure Domain Name System (DNS) Deployment Guide.* NIST. [https://csrc.nist.gov/](https://csrc.nist.gov/) (see DNS guidance)
4. European Union Agency for Cybersecurity. (2020). *ENISA Threat Landscape and DNS Security Recommendations.* ENISA. [https://www.enisa.europa.eu/](https://www.enisa.europa.eu/)
5. Internet Engineering Task Force. (2011). *RFC 5914: DNS Security Threats and Practices* (and related RFCs on DNSSEC/DoT). IETF. [https://www.ietf.org/](https://www.ietf.org/)

---

 
## Pharming Attack Tree Diagram