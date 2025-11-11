# Security Testing for NFC Payment Replay Attacks

## 1. Overview

NFC-based payments (mobile wallets, contactless cards) rely on the assumption of proximity and freshness of the transaction. Replay (or relay) attacks allow attackers to capture valid NFC exchange data and reuse or retransmit it later (or at a remote terminal), thereby defrauding payment systems. In a cloud-mobile-IoT ecosystem, mobile devices act as both clients and NFC targets, IoT devices/gateways may act as readers or payment endpoints, and cloud services process these payments &mdash; so any weakness in the chain (mobile, reader, firmware, cloud backend) enables replay attacks. Research shows that NFC payments can be attacked via relay/replay even with mobile wallets.
Additionally, recent industry reports highlight malware and MaaS platforms exploiting NFC relay or replay for fraudulent cash-outs. 

---

## 2. High-level Testing Workflow / Setup

1. **Scope & threat modelling**

   * Identify payment endpoints: mobile wallets (Android HCE, iOS), contactless cards, IoT payment readers/gateways, cloud payment processors.
   * Map NFC transaction flows: device &harr; reader (mobile/IoT) &harr; gateway &harr; cloud.
   * Identify replay/relay vectors: i) capturing NFC frames and later replaying at terminal; ii) tunnelling NFC frames remotely (relay); iii) mobile/IoT reader pretending to be legitimate and replaying previously valid data; iv) cloud backend trusting repeated tokens or missing freshness checks.

2. **Baseline capture & metrics**

   * Capture normal NFC transaction flows: logs, NFC trace data (APDUs, timing, terminal reader responses), mobile wallet logs, reader logs, cloud back-end logs.
   * Capture metadata: terminal location/time, device identity, transaction counters/sequence numbers, session tokens, cryptographic nonces.

3. **Static analysis (SAST) & configuration review**

   * Review mobile wallet application code (if accessible) or reverse-engineer to check for nonce usage, counter-based tokens, anti-replay logic, HCE implementation.
   * Review IoT/reader firmware and gateway code: verify that replay detection is implemented, that each transaction token is fresh and cannot be reused, that reader logs duplicate attempts.
   * Review cloud backend logic: check that incoming payment transactions include freshness, sequence number, card/reader ID, transaction counters, and that repeated tokens are rejected.

4. **Dynamic testing (DAST) / replay attack simulation**

   * Set up NFC testbed: use mobile device, payment terminal (or mock reader), capture NFC exchanges. Use tools to dump APDUs or transaction data.
   * Replay captured transactions at same or different terminal to test if system allows reuse.
   * Relay scenario: use two devices (one near card/mobile wallet, one near terminal) to tunnel NFC frames in real time (or near real-time) and verify if the system detects that the card/wallet is not in proximity. (See relay vs replay distinction.)
   * Mobile wallet scenario: test if mobile wallet uses HCE and how it handles duplicate tokens or previous transaction tokens.
   * IoT reader/gateway scenario: test if IoT payment reader accepts duplicate NFC tokens or fails to notice reuse of previously captured tokens.

5. **Network, telemetry & logging detection tests**

   * Monitor logs for duplicate transaction IDs, sequence numbers reused, unexpected location/terminal ID mismatch, multiple terminals seeing same token.
   * Use network sniffing (near reader/gateway) to capture NFC traffic, APDU sequences, or communication between reader and backend.
   * Use side-channel or trace tools if needed (timing anomalies, unexpected delays suggest relay). Research indicates ambient sensor/side-channel detection may help.

6. **Mobile & IoT integration tests**

   * On Android/iOS: test mobile wallet robustness against replay attacks; e.g., attempt replay of a previously executed transaction; simulate near-field attacker capturing wallet tap and replaying at another terminal.
   * For IoT payment readers/gateways: test insertion of malicious node that performs replay of prior transactions, verify cloud backend logs and detection.
   * Test backend logic: repeated token usage, reversed timing, unusual terminal location/time stamps.

7. **Reporting & remediation**

   * Identify gaps: missing nonce/sequence checks, lack of proximity verification, no transaction counter or reuse detection, mobile wallet HCE weaknesses, reader firmware missing anti-replay logic.
   * Recommend mitigations: unique transaction counters, nonces, tokenizations with expiry, proximity proofs (distance bounding, ambient sensors), mutual authentication, backend duplicate-token detection, device time/location checks, mobile wallet user confirmation.
   * Validate by retesting after mitigation to ensure replay attempts are blocked or logged.

---

## 3. Security Test Approaches & Tools


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
      <td>Gray-box</td>
      <td>DAST</td>
      <td>NFC transaction capture & replay</td>
      <td>Proxmark3 / NFCReader + custom scripts</td>
      <td><a href="https://github.com/Proxmark/proxmark3">Proxmark3</a></td>
      <td>Android (HCE), IoT reader</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>NFC relay test (tunnel frames to remote terminal)</td>
      <td>NFCGate (relay tool) / Two-phone relay setup</td>
      <td><a href="https://github.com/SMKLab/NFCGate">NFCGate</a></td>
      <td>Android (wallet + attacker devices)</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Mobile wallet code review for anti-replay logic</td>
      <td>MobSF / Static code analysis</td>
      <td><a href="https://mobsf.github.io/">MobSF</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Reader/gateway firmware review for replay detection</td>
      <td>Binwalk + Ghidra</td>
      <td><a href="https://github.com/ReFirmLabs/binwalk">Binwalk</a> / <a href="https://ghidra-sre.org/">Ghidra</a></td>
      <td>IoT payment reader</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Backend API review for duplicate-token handling & freshness</td>
      <td>Postman / Burp Suite (API testing)</td>
      <td><a href="https://www.postman.com/">Postman</a> / <a href="https://portswigger.net/burp">Burp Suite</a></td>
      <td>Cloud backend</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Network sniffing & anomaly detection on payment flows</td>
      <td>Wireshark / Zeek</td>
      <td><a href="https://www.wireshark.org/">Wireshark</a> / <a href="https://www.zeek.org/">Zeek</a></td>
      <td>Both (mobile/IoT/gateway)</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile instrumentation for HCE‐wallet behavior under replay</td>
      <td>Frida</td>
      <td><a href="https://frida.re/">Frida</a></td>
      <td>Android, iOS</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>SAST</td>
      <td>Replay detection logic review & code security scanning</td>
      <td>Semgrep / CodeQL</td>
      <td><a href="https://semgrep.dev/">Semgrep</a> / <a href="https://github.com/github/codeql">CodeQL</a></td>
      <td>Cloud/mobile wallet/reader firmware</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Physical proximity / ambient sensor testing for relay detection</td>
      <td>Custom test harness (accelerometer/gyro), ambient sensors</td>
      <td>&mdash; (custom) </td>
      <td>Mobile device</td>
    </tr>
  </tbody>
</table>


---

## 4. Practical Testbed / Setup Checklist

* **Device set-up:**

  * Mobile wallet device (Android with HCE; optionally iOS if wallet supports contactless).
  * Payment reader terminal or mock POS / IoT reader device configured for NFC payment.
  * Attacker device: NFC reader/emulator (Proxmark3) to capture frames; optionally relay phone or NFC gateway.
  * IoT gateway/payment reader device if applicable (for IoT payment endpoint).
  * Cloud backend / payment-processor environment instrumented with logging and API endpoints.

* **Baseline capture:**

  * Execute a legitimate NFC payment transaction: capture APDU sequence, mobile wallet logs, reader logs, backend logs.
  * Record transaction ID, timestamp, nonce, reader ID, mobile device ID, token details, sequence/counter.
  * Ensure logs have sufficient detail: receipt of payment token, clearance by backend, token consumption.

* **Replay test:**

  * Using Proxmark3 or NFC reader device, capture the transaction frames from the mobile wallet reader.
  * Immediately (or after a delay) attempt to replay the captured frames at the same or different reader terminal. Observe whether transaction is accepted or rejected.
  * Monitor logs: does backend detect duplicate token? Does reader reject? Are sequence numbers reused?
  * Variation: Use a delay or altered reader (geographically distant) to test whether proximity/freshness checks exist.

* **Relay test:**

  * Set up two devices: one near mobile wallet, one near reader terminal. Use software (NFCGate) to tunnel NFC frames between them (effectively remote token usage).
  * Verify whether system handles remote/replayed token and detects/blocks it or not.

* **Mobile instrumentation test:**

  * Using Frida, instrument the mobile wallet app to skip certain checks (e.g., disable nonce/sequence validation) and then attempt to replay token or duplicate transaction.
  * Check whether wallet transaction flows detect duplicate or stale tokens.

* **Reader/gateway firmware test:**

  * Extract firmware via Binwalk/Ghidra; review for anti-replay logic: presence of counters, nonces, token timestamp checks, token-id consumption.
  * If missing, inject older token frames and attempt repeated transactions.

* **Cloud backend test:**

  * Use Postman/Burp to attempt to reuse the same transaction token via API endpoint (simulate wallet/reader submitting a replayed transaction) or modify token timestamp fields, token IDs, sequence numbers. Observe backend handling.
  * Check whether backend logs duplicates, rejects second use of token, or flags abnormal pattern (e.g., same token twice, same wallet ID, same reader ID but far apart).

* **Detection monitoring:**

  * Use Wireshark/Zeek to capture NFC reader &harr; mobile &harr; backend communications; analyze for repeated token IDs, unusual timing, multiple reader IDs for same token.
  * Set up SIEM/UEBA to alert on: same token ID used from different terminal IDs within short time; identical APDU sequence multiple times; token reuse; mismatched location/time for reader device; etc.

* **Ambient/proximity sensor tests:**

  * On mobile wallet side: test whether ambient sensor data (accelerometer, gyroscope, magnetometer) is used to verify proximity; attempt to bypass by spoofing sensor data or using stationary remote relay; observe how system responds. Research shows ambient sensing alone may be insufficient but is relevant.
  * For IoT reader/terminal: test whether reader uses physical proximity constraints (limiting NFC field strength, verifying location/time of tap) and attempt replay bypass.

* **Reporting and remediation:**

  * Summarize findings: which components were vulnerable (wallet, reader, backend). Note missing anti-replay mechanisms: e.g., lack of token counter, lack of timestamp/nonce, no duplicate detection, no proximity proof.
  * Provide mitigation recommendations: implement unique transaction nonce + single-use token, enforce strict token lifetime, reader side verification of token counters, backend duplicate usage detection + blacklisting, proximity bounding (e.g., ultrasonics, ambient sensor correlation), HCE implementation hardened for logs/counters, mobile wallet requiring user confirmation for unusual terminals, IoT reader firmware update.
  * Retest after applying fixes to verify replay attempts are blocked or logged appropriately.

---

## 5. References

1. Francis, L., Hancke, G., Mayes, K., & Markantonakis, K. (2011). Practical relay attack on contactless transactions by using NFC mobile phones. *Cryptology ePrint Archive, Paper 2011/618*.
2. Giese, D., Liu, K., Sun, M., Syed, T., & Zhang, L. (2019). Security analysis of Near-Field Communication (NFC) payments. *arXiv preprint arXiv:1904.10623*. 
3. Akram, R. N., Gurulian, I., Shepherd, C., Markantonakis, K., & Akram, R. N. (2016). Empirical evaluation of ambient sensors as proximity detection mechanism for mobile payments. *arXiv preprint arXiv:1601.07101*. 
4. Harnaningrum, L. N., Ashari, A., & Putra, A. E. (2022). Mobile payment transaction model with robust security in the NFC-HCE ecosystem with secure elements on smartphones. *International Journal of Advanced Computer Science and Applications*, 13(8), 160-168.


