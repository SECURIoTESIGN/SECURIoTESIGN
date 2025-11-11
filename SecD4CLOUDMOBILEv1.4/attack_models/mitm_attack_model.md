# Man-in-the-Middle Attack Model

## Definition

A *Man-in-the-Middle (MITM) attack* is a cyberattack in which a malicious actor secretly intercepts, relays, or alters communications between two parties who believe they are directly communicating with each other. In cloud, mobile, and IoT ecosystems, this attack exploits the distributed and often wireless nature of these environments to compromise data confidentiality, integrity, or authentication.

---

## Relevant Attack Categories

* **Network-level MITM (LAN/Wi-Fi):** ARP spoofing, DHCP spoofing, rogue Wi-Fi APs, or evil-twin hotspots intercepting mobile app and IoT traffic.
* **Protocol downgrade / TLS stripping:** A protocol downgrade attack (also called version rollback or bidding-down attack) occurs when an attacker forces a system to abandon a secure protocol (like TLS 1.3) in favor of an older, less secure version (like TLS 1.0 or even SSL).
* **Certificate & PKI attacks:** Use of fraudulent certificates, compromised CAs, or client acceptance of invalid/self-signed certs (mobile apps lacking pinning).
* **Proxy / transparent gateway compromise:** Rogue or misconfigured proxies, compromised gateway firmware or cloud edge services that alter or exfiltrate data.
* **DNS/DNS-spoofing / DNS-cache poisoning:** Redirecting legitimate hostnames to attacker controlled IPs (affecting APIs, update servers or telemetry endpoints).
* **Compromised supply-chain or OEM image:** Devices or apps shipped with backdoored trust anchors, proxying all comms to attacker C2.
* **Application-layer MITM (API abuse):** Intercepting/rewriting REST/WebSocket calls, injecting commands to IoT actuators or stealing tokens via mobile app webviews or insecure deep links.

---

## Mitigations & Defensive Controls

### Cryptographic & protocol controls

* **Always use strong end-to-end TLS (latest TLS 1.3) with secure cipher suites**; disable older/proprietary ciphers and renegotiation.
* **Certificate validation & pinning:** enforce strict validation on clients (mobile apps) and use certificate pinning or public-key pinning where feasible (with safe update mechanisms).
* **Mutual TLS (mTLS):** use client certificates for device↔cloud authentication in IoT/gateway scenarios.
* **HSTS, secure cookie flags, and SameSite policies** for web components.

### Network & Infrastructure

* **DNS security:** DNSSEC on authoritative zones, validate responses where possible; use DNS over TLS/HTTPS for clients.
* **Network segmentation & least-privilege:** isolate IoT networks from user/customer networks and internet-facing admin planes; limit lateral movement.
* **Use secure, managed Wi-Fi (enterprise WPA2/WPA3-Enterprise) and avoid open hotspots** for provisioning or sensitive flows.

### Application & Device Hardening

* **Avoid embedding trust anchors that are immutable without update channel.** Implement secure, authenticated update channels and revocation.
* **Short-lived tokens, mTLS, and OAuth best practices:** do not rely solely on long-lived static API keys stored unprotected.
* **Disable insecure fallback:** app should never silently accept downgraded connections or invalid certs; fail closed.
* **Harden webviews & deep links:** disable JavaScript handling of arbitrary URIs when not required; verify origin of URIs.

### Operational & Detection

* **Network IDS/SSL/TLS inspection awareness:** detect ARP/DHCP anomalies, unusual TLS certificate chains, or mismatched SNI vs. certificate.
* **Telemetry & analytics:** monitor for sudden changes in API endpoints, unusual client IPs, token reuse, or unexpected command acknowledgements from devices.
* **Secure provisioning:** out-of-band verification (QR + per-device one-time codes), ephemeral bootstrap tokens, and enrollment with attestation.
* **User education & tooling:** warn users against unknown Wi-Fi networks, and provide in-app indicators when endpoints or certs change.

---

## 4) DREAD Risk Assessment

<style>
table, th, td {
  border: 1px dotted gray;
  border-collapse: collapse;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
}
</style>

<table>
  <thead>
    <tr>
      <th>DREAD Factor</th>
      <th style="text-align:right;">Score (0-10)</th>
      <th>Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Damage Potential</td>
      <td style="text-align:right;"><strong>8</strong></td>
      <td>MITM can expose credentials, session tokens, PII, control commands for IoT actuators, or manipulate transactions—leading to data breach, fraud or physical harm.</td>
    </tr>
    <tr>
      <td>Reproducibility</td>
      <td style="text-align:right;"><strong>8</strong></td>
      <td>Techniques like rogue APs, ARP spoofing, DNS spoofing and proxying are well-known and easily reproduced with inexpensive tools.</td>
    </tr>
    <tr>
      <td>Exploitability</td>
      <td style="text-align:right;"><strong>7</strong></td>
      <td>Requires network access (Wi-Fi/LAN) or ability to poison DNS/PKI; some vectors (compromised CA, supply chain) are harder but possible.</td>
    </tr>
    <tr>
      <td>Affected Users</td>
      <td style="text-align:right;"><strong>8</strong></td>
      <td>Mobile users in public networks, entire IoT zones (warehouse, factory), or cloud customers relying on compromised gateways can be impacted.</td>
    </tr>
    <tr>
      <td>Discoverability</td>
      <td style="text-align:right;"><strong>7</strong></td>
      <td>Many MITM attacks are detectable (cert warnings, unusual network patterns), but sophisticated setups (transparent proxies, valid certs) can be stealthy.</td>
    </tr>
  </tbody>
</table>


**Digit-by-digit arithmetic:**
**Sum = 8 + 8 + 7 + 8 + 7 = 38.**
**Average = 38 / 5 = 7.6**;  Rating: **High / Critical**

---

## References

1. OWASP Foundation. (2023). *OWASP Cheat Sheet: Transport Layer Protection*. OWASP. [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
2. National Institute of Standards and Technology. (2020). *NIST Special Publication 800-52 Revision 2: Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations.* NIST. [https://doi.org/10.6028/NIST.SP.800-52r2](https://doi.org/10.6028/NIST.SP.800-52r2)
3. Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3* (RFC 8446). Internet Engineering Task Force. [https://tools.ietf.org/html/rfc8446](https://tools.ietf.org/html/rfc8446)
4. European Union Agency for Cybersecurity. (2020). *ENISA Threat Landscape — 2020: Trends and developments in the cyber threat landscape*. ENISA. [https://www.enisa.europa.eu/publications/enisa-threat-landscape-2020](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2020)
5. OWASP Foundation. (2023). *OWASP Mobile Top 10* and *OWASP IoT Top Ten* (guidance on mobile & IoT app security). [https://owasp.org](https://owasp.org)

---


## MiTM Attack Tree Diagram