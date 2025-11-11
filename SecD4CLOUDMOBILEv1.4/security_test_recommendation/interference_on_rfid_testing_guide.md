# Security Testing for RF Interference on RFID Attacks

## 1. Overview

RF interference (intentional jamming, unintentional co-channel noise, selective jamming, and collision attacks) can prevent RFID readers from communicating with tags, create denial-of-service, or selectively block/alter reads (e.g., to evade inventory or access control). Testing should cover physical PHY-layer interference, protocol-level resilience and interplay with mobile/cloud telemetry so you validate detection, mitigation and incident response across the ecosystem.

---

## 2. High-level Workflow / Testing Setup

1. **Threat model & scope** &mdash; identify tag types (LF/HF/UHF), reader models, antennas, reader dwell/anti-collision settings, mobile apps that act as readers (NFC on Android/iOS), and cloud ingestion/telemetry rules.
2. **Baseline measurement (golden)** &mdash; capture normal RSSI/BER/reader logs/throughput and tag read rates under controlled, interference-free conditions.
3. **Passive monitoring** &mdash; record RF activity (spectrum waterfall, ADS-B type) using SDR/logic (RTL-SDR, HackRF, USRP, Saleae) while the system is idle and during normal operation.
4. **Active interference tests (DAST)** &mdash; use SDR or dedicated jammers to perform broad-band narrowband jamming, targeted (selective) jamming of specific reader/tag frequencies or timing collisions, and analyze effect on read reliability, latency and cloud alerts.
5. **Protocol-level tests** &mdash; attempt repeated collisions during anti-collision windows, evaluate reader timeouts and re-tries, test selective blocking of certain EPCs or tag families.
6. **Mobile + cloud integration tests** &mdash; verify how mobile clients (Android / iOS) and cloud pipelines detect, log and react to degraded/failing reads; ensure telemetry includes signal/reader status and that alerts are actionable.
7. **Reporting & remediation** &mdash; classify findings (availability, integrity, detection gaps) and recommend controls (physical shielding, channel hopping, anti-jamming algorithms, monitoring, enforced telemetry).

---

## 3. Security Test Tools


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
    <!-- Reader/Tag reverse engineering and tag emulation -->
    <tr>
      <td>Gray-box</td>
      <td>SAST / DAST</td>
      <td>Tag/reader protocol analysis & emulation</td>
      <td>Proxmark3</td>
      <td><a href="https://github.com/Proxmark/proxmark3">Proxmark3</a></td>
      <td>Both</td>
    </tr>
    <!-- Passive spectrum monitoring -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Spectrum monitoring / logging</td>
      <td>RTL-SDR (RTL2832U), SDR# / gqrx / CubicSDR</td>
      <td><a href="https://www.rtl-sdr.com/">RTL-SDR</a></td>
      <td>Both</td>
    </tr>
    <!-- Active RF transmit / jamming -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Active RF interference / jamming (broadband / narrowband)</td>
      <td>HackRF One (SDR) / GNU Radio</td>
      <td><a href="https://github.com/mossmann/hackrf">HackRF One</a></td>
      <td>Both</td>
    </tr>
    <!-- Higher-power / professional -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>High-power, controlled jamming / continuous wave</td>
      <td>USRP (Ettus) + GNU Radio</td>
      <td><a href="https://www.ettus.com/">USRP (Ettus) + GNU Radio</a></td>
      <td>Both</td>
    </tr>
    <!-- Targeted selective jamming / collision -->
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Selective/targeted jamming & collision timing attacks</td>
      <td>Custom GNU Radio flowgraphs / HackRF scripts</td>
      <td><a href="https://www.gnuradio.org/">Custom GNU Radio flowgraphs</a></td>
      <td>Both</td>
    </tr>
    <!-- RFID-specific tools & automation -->
    <tr>
      <td>Gray-box</td>
      <td>DAST / SAST</td>
      <td>RFID tools & automation (scanning, logging, fuzzing)</td>
      <td>RFIDIot, proxmark3 client</td>
      <td><a href="https://github.com/AdamLaurie/RFIDiot">RFIDIot</a></td>
      <td>Both</td>
    </tr>
    <!-- Antenna-level sensing -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Logic / RF capture for antenna signals & timing</td>
      <td>Saleae Logic / oscilloscope (for reader control lines)</td>
      <td><a href="https://www.saleae.com/">Saleae Logic</a></td>
      <td>Both</td>
    </tr>
    <!-- Mobile platform tests -->
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile NFC app testing / instrumentation</td>
      <td>MIFARE Classic Tool (Android), NFC Tools</td>
      <td><a href="https://play.google.com/store/apps/details?">MIFARE Classic Tool</a></td>
      <td>Android</td>
    </tr>
    <!-- Cloud telemetry / analytics -->
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Cloud / telemetry integrity checks</td>
      <td>Custom telemetry analyzers, ELK stack, Splunk</td>
      <td><a href="https://www.elastic.co/elastic-stack/">Custom telemetry analyzers</a></a></td>
      <td>Both</td>
    </tr>
    <!-- Antenna & RF characterization -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>RF tuning, antenna pattern & power testing</td>
      <td>Spectrum analyzer (Keysight, Rigol)</td>
      <td><a href="https://www.keysight.com/">Keysight</a></td>
      <td>Both</td>
    </tr>
    <!-- Controlled lab test / regulatory -->
    <tr>
      <td>White-box</td>
      <td>DAST</td>
      <td>Controlled chamber testing / EMI</td>
      <td>RF shielding chamber / Anechoic chamber</td>
      <td>Lab vendors (e.g., ETS-Lindgren)</td>
      <td>Both</td>
    </tr>
  </tbody>
</table>

---

## 4. Practical Testbed 

* **Proxmark3** (LF/HF tag read/write/emulate) &mdash; for protocol-level tests, tag emulation, and verifying selective blocking effects. 
* **HackRF One** (transmit & receive SDR) + **GNU Radio** &mdash; create narrowband or broadband jamming signals, generate timed collisions, and script attacks. 
* **USRP (Ettus)** &mdash; for higher-power precision jamming / multi-channel simultaneous jamming and research-grade experiments. 
* **RTL-SDR** &mdash; inexpensive passive spectrum monitoring and waterfall captures to detect interference and identify jammer signatures. 
* **RF spectrum analyzer** (bench or portable) &mdash; measure power spectral density, identify interfering sources, verify compliance.
* **Anechoic / shielded test area or attenuators** &mdash; avoid radiating unlawful transmissions and to keep tests contained.
* **Oscilloscope / logic analyzer** &mdash; observe reader control lines, antenna feed, and timing for collision tests.
* **Mobile test phones** &mdash; Android phones with NFC developer tools (Android supports NFC tag emulation with HCE in many cases; iOS supports a subset of NFC). Test mobile app behaviours under interference.
* **Cloud telemetry collector** (ELK, Splunk) &mdash; ingest reader logs and sensor telemetry to validate detection & alerting.

Safety/regulatory: perform transmit tests in shielded/attenuated environments and ensure legal compliance (RF transmissions are regulated). Use attenuators and lab chambers or the local authority experimental license. 

---

## 5. Example Tests & Commands 

1. **Passive detection** &mdash; run RTL-SDR waterfall while reading tags; note spikes near 13.56 MHz (HF/NFC) or 902–928 MHz (UHF).
2. **Broadband nuisance jamming** &mdash; with HackRF and GNU Radio, transmit white noise over the tag-reader band (low power inside chamber) and measure read success rate vs baseline.
3. **Selective jamming (target EPC)** &mdash; observe tag read timing, then transmit short bursts to collide specifically during tag reply windows (requires synchronized timing and precise SDR scripting). Monitor whether reader chooses re-try or times out.
4. **Reader behavior fuzzing** &mdash; use Proxmark3 to inject malformed tag replies or replay legitimate tag frames with timing jitter to measure recovery. 
5. **Cloud alert validation** &mdash; while causing read rate drop artificially, confirm cloud telemetry flags devices/locations and triggers incident workflows.

---

## 6. References

1. Souryal, M. R., Novotny, D. R., Kuester, D. G., Guerrieri, J. R., & Remley, K. A. (2012). Impact of RF interference between a passive RFID system and a frequency hopping communications system in the 900 MHz ISM band. *IEEE Electromagnetic Compatibility Magazine*, 1(3), 97-102.
2. Juels, A. (2006). RFID security and privacy: A research survey. *IEEE journal on selected areas in communications*, 24(2), 381-394.
3. Jacovic, M., Rey, X. R., Mainland, G., & Dandekar, K. R. (2023). Mitigating RF jamming attacks at the physical layer with machine learning. IET communications, 17(1), 12-28.
4. Garcia, F. D., de Koning Gans, G., & Verdult, R. (2012). Tutorial: Proxmark, the swiss army knife for RFID security research.
5. Stancu, E., Berceanu, M., Halunga, S., & Fratu, O. (2023, March). RFID sensitivity in narrowband jamming environment. In *Advanced Topics in Optoelectronics, Microelectronics, and Nanotechnologies XI* (Vol. 12493, pp. 699-703). SPIE.
