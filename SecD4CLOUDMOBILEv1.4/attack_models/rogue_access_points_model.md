# Rogue Access Point (AP) Attack Model

## Definition

A **rogue access point (AP) attack** occurs when an attacker deploys an unauthorized wireless access point that imitates legitimate Wi-Fi (SSID, BSSID, signal characteristics) to entice devices (mobile apps, IoT devices, users) to associate. Once devices connect, the attacker can intercept traffic (MITM), present phishing portals, push malicious updates, capture credentials/tokens, or pipe forged telemetry into cloud backends. Rogue APs include “evil-twin” hotspots, open hotspots that entice auto-join, and compromised enterprise APs misconfigured or backdoored.

---

## Attack categories 

* **Evil-Twin / Fake SSID:** attacker creates AP with same SSID as corporate/known network to trick mobile devices and IoT to auto-join.
* **Rogue open hotspot / captive portal phishing:** AP forces captive portal that harvests credentials or prompts unsafe actions (install app, accept certificate).
* **Rogue AP as MITM / traffic proxy:** AP intercepts TLS-stripped or misvalidated traffic, injects payloads, or relays credentials to attacker.
* **Client-side auto-join abuse / KARMA:** AP advertises many SSIDs (probe-response trickery) to capture devices that auto-connect to previously seen SSIDs.
* **Compromised/insider AP:** legitimate APs or enterprise controllers hijacked (misconfiguration, default creds) act as rogue proxies.
* **Rogue AP for device provisioning abuse:** attacker intercepts onboarding flows (QR, captive, OTA) to enroll devices into attacker services or steal provisioning tokens.
* **Rogue AP for IoT lateral movement:** once an IoT device connects, attacker probes local network, abuses weak protocols, or uses device credentials to reach cloud management endpoints.

---

## Mitigations & Defensive Controls

**Authentication & transport**

* Use **802.1X (EAP-TLS)** or other certificate-based enterprise authentication; avoid PSK for critical devices.
* Enforce **TLS 1.3 / mTLS** for all API calls so intercepted traffic cannot easily be decrypted or injected.
* **Pin certificates / public keys** in mobile apps (with safe update path) and require device attestation for IoT onboarding.

**Network & access controls**

* **Wired-and-wireless NAC** (network access control) that verifies device posture and blocks unknown AP associations; use VLANs and least privilege for wireless segments.
* **Disable auto-join** policies on managed mobile devices; use MDM to push authorized SSID lists and disallow user changes.
* **Guest/IoT segmentation:** isolate guest and IoT networks and block direct access to management/cloud planes except via authenticated gateways.

**Visibility & detection**

* Deploy **WIDS/WIPS (wireless intrusion detection/prevention)** sensors to detect new APs, duplicate BSSIDs, suspicious signal patterns, or probe-response attacks.
* Use **802.11 management frame protection (PMF)** where supported to prevent spoofed management frames.
* Correlate edge logs and cloud telemetry for anomalies (new client MACs seen via odd APs, sudden token use from new IPs).

**Provisioning & device hardening**

* Require **out-of-band verification** for provisioning (one-time codes, signed manifests), and bind onboarding tokens to device identity.
* Harden IoT devices: disable promiscuous Wi-Fi scan/auto-connect modes, rotate credentials, and store secrets in hardware (TPM/SE).
* Implement **short-lived tokens** and step-up authentication for sensitive operations (payments, firmware updates).

**Operational & user controls**

* Train staff to avoid public/untrusted Wi-Fi for admin tasks; provide secure company VPN and enforce its use.
* Maintain an inventory of authorized APs and an emergency contact/process for reported rogue APs.
* Use DNS over TLS/HTTPS (DoT/DoH) and HTTPS Everywhere principles to reduce credential leakage.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor     | Score (0-10) | Rationale                                                                                                                                |
| ---------------- | -----------: | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Damage Potential |        **8** | Credential theft, session hijack, malicious provisioning, or cloud account takeover with business/financial/safety impact.               |
| Reproducibility  |        **8** | Evil-twin and rogue AP setups are trivial with commodity hardware/SDR or portable devices.                                               |
| Exploitability   |        **7** | Requires proximity for Wi-Fi attacks (local), but social engineering (captive portals) and device auto-join make exploitation practical. |
| Affected Users   |        **8** | Any mobile user or IoT device that auto-joins or uses weak onboarding; can affect many devices in a location.                            |
| Discoverability  |        **8** | New APs and duplicate SSIDs are detectable with WIDS/WIPS and client telemetry, but skilled attackers can be stealthy.                   |

**Digit-by-digit arithmetic (explicit):**

**Sum = 8 + 8 + 7 + 8 + 8 = 39**.
**Average = 39 / 5 = 7.8**; Rating: **High / Critical**.

---

## References

1. National Institute of Standards and Technology. (2013). *Guide to Securing Wireless Local Area Networks (NIST Special Publication 800-153).* NIST. [https://doi.org/10.6028/NIST.SP.800-153](https://doi.org/10.6028/NIST.SP.800-153)
2. IEEE Standards Association. (2016). *IEEE Std 802.11™-2016 — IEEE Standard for Information technology—Telecommunications and information exchange between systems Local and metropolitan area networks—Specific requirements — Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications.* IEEE. [https://standards.ieee.org/standard/802_11-2016.html](https://standards.ieee.org/standard/802_11-2016.html)
3. European Union Agency for Cybersecurity. (2020). *Baseline Security Recommendations for IoT.* ENISA. [https://www.enisa.europa.eu/publications](https://www.enisa.europa.eu/publications)
4. OWASP Foundation. (2023). *OWASP Mobile Top 10 & Mobile Security Verification Standard (MASVS).* OWASP. [https://owasp.org/](https://owasp.org/)
5. Cisco Systems. (2019). *Best Practices for Securing Enterprise Wireless LANs.* Cisco White Paper. (Vendor guidance on enterprise WLAN security and rogue AP detection.)

---


## Rogue Access Point Attack Tree Diagram


