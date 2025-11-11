# Reverse Engineering Attack 

## Definition

**Reverse engineering attack**, the practice of analysing compiled binaries, firmware, hardware, protocols or app behaviour to discover internal logic, secrets (API keys, cryptographic material), undocumented protocols, licensing checks or vulnerabilities that enable cloning, tampering, bypassing protections or building targeted exploits. In cloud-backed mobile and IoT ecosystems reverse engineering is used to extract device/cloud credentials, reproduce provisioning flows, create rogue devices, or find vulnerabilities for large-scale compromise.

---

## Attack Categories

* **Binary/static analysis:** disassembling/decompiling mobile apps (APK/IPA), firmware images or native libraries to find keys, hardcoded endpoints or logic.
* **Dynamic/runtime analysis:** debugging, hooking, instrumentation (Frida, Xposed), or monitoring runtime behaviour to intercept secrets or bypass checks.
* **Firmware extraction & analysis:** dumping flash or extracting images via JTAG/SWD, bootloader unlocks, or SPI reads to study firmware internals.
* **Protocol reverse engineering:** sniffing traffic and inferring custom protocols or message formats to emulate devices or replay messages.
* **Hardware reverse engineering:** decapping chips, reading silicon, or analysing PCBs to uncover debug interfaces, crypto chips or secret storage.
* **Supply-chain cloning & counterfeit:** using reverse-engineered designs to build clones that impersonate legitimate devices and call cloud APIs.
* **Tooling-as-a-service / automated unpackers:** attackers use automated deobfuscation, symbol recovery and mass-analysis pipelines to scale attacks across many apps/devices.

---

## Mitigations & Defensive Controls

**Design & development**

* **Never hardcode secrets:** use hardware-backed keys (TPM/SE/eSE) or cloud-issued short-lived credentials.
* **Secure boot & signed firmware:** require cryptographic verification and anti-rollback for firmware/images.
* **Minimize sensitive logic client-side:** keep sensitive algorithms and secrets on server-side when possible, use server-side attestation for decisions.

**Obfuscation & tamper-resistance (defence-in-depth)**

* **Code obfuscation & packing** for mobile/native code (control-flow obfuscation, string encryption) — raises bar but not a substitute for real controls.
* **Runtime protections:** root/jailbreak detection, debugger/trace detection, integrity checks, white-box crypto when hardware keys unavailable.
* **Hardware protections:** lock or fuse debug interfaces, use secure elements to protect keys, and design PCBs to make probing harder.

**Protocol & provisioning**

* **Use strong mutual auth (mTLS, device certificates)** and bind tokens to device attestation so emulated devices can be detected/rejected.
* **Short-lived credentials & token binding:** ensure stolen secrets expire quickly and are tied to device identity or attestation evidence.
* **Encrypt telemetry and use message-level MACs with per-message nonces.**

**Operational & detection**

* **Monitor for abuse patterns:** atypical device fingerprints, mass-provisioning attempts, replayed messages, or many clients presenting identical firmware hashes.
* **Telemetry for tamper indicators:** unexpected API versions, abnormal API call sequences, or clients omitting attestation evidence.
* **Rotate keys & credentials frequently; use revocation lists for compromised device classes.**

**Policy & supply-chain**

* **Secure CI/CD and artifact signing:** M-of-N signing for releases; ensure build reproducibility and artifact provenance (SBOM).
* **Harden manufacturing:** disable debug on production units, vet contractors, and sample-check shipped firmware/hardware.

---

## DREAD Risk Assessment (0-10)

| DREAD Factor         | Score (0-10) | Rationale                                                                                                                                                |
| -------------------- | -----------: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Damage Potential** |        **8** | Extracted secrets or protocol details enable mass device impersonation, telemetry spoofing, firmware tampering, or cloud account compromise.             |
| **Reproducibility**  |        **8** | Reverse engineering techniques and tooling are well-known and automated pipelines scale analysis across many binaries/devices.                           |
| **Exploitability**   |        **7** | Requires physical access or delivery vector (app install / firmware sample) plus skills/tools — common among motivated attackers and commodity services. |
| **Affected Users**   |        **8** | A single successful reverse-engineering outcome (e.g., cloned device or stolen signing key) can affect large fleets and many cloud users.                |
| **Discoverability**  |        **6** | Presence of vulnerable artifacts is observable (public apps/firmware), but detecting active reverse engineering targeting your assets is non-trivial.    |

**Digit-by-digit arithmetic (explicit):**
Sum = 8 + 8 + 7 + 8 + 6 = **37**.
Average = 37 / 5 = **7.4**.

**DREAD average = 7.4**; Rating: **High priority**.

---

## References

1. US National Institute of Standards and Technology. (2021). *NISTIR 8276: Software Vulnerability Taxonomy for IoT Systems* (relevant sections on firmware/binary risk). NIST. [https://doi.org/10.6028/NIST.IR.8276](https://doi.org/10.6028/NIST.IR.8276)
2. OWASP Foundation. (2023). *OWASP Mobile Application Security Verification Standard (MASVS).* OWASP. [https://owasp.org/](https://owasp.org/)
3. Collberg, C., & Nagra, J. (2009). *Surreptitious Software: Obfuscation, Watermarking, and Tamperproofing for Software Protection.* Addison-Wesley.
4. National Institute of Standards and Technology. (2017). *NIST SP 800-147: BIOS Protection Guidelines* (for firmware integrity). NIST. [https://csrc.nist.gov/](https://csrc.nist.gov/)
5. ENISA. (2020). *Baseline Security Recommendations for IoT.* European Union Agency for Cybersecurity. [https://www.enisa.europa.eu/](https://www.enisa.europa.eu/)

---


## Reverse Engineering Attack Diagram