# Security Testing for On-Off Attacks

**Overview**

An On-Off attack is when a compromised node (sensor, actuator, gateway or mobile/IoT endpoint) behaves correctly for periods of time ("On") to build trust, then intermittently misbehaves ("Off") to avoid detection (for example dropping packets, injecting false data, or failing to report) and then goes back to normal ("On"). This makes detection harder because behaviour appears normal most of the time. This is especially relevant in IoT/WSN/mobile/cloud ecosystems where nodes are trusted once they appear healthy. For example, one paper titles "On-Off attack detection in trust model using intra-daily variability for the IoT".

---

## 1. High-level Testing Workflow / Setup

1. **Scope & threat modelling**

   * Identify nodes/devices: IoT sensors, actuators, gateways, mobile clients, cloud-ingestion endpoints.
   * Map data flows: node ↔ gateway ↔ cloud; mobile ↔ node/gateway ↔ cloud.
   * Identify trust/behavioural metrics: heartbeats, data upload volume, sensor readings, error rate, drop rate, registration events.
   * Define On-Off attack vectors: node behaves ‘good’ for a period to gain trust, then for a short window misbehaves (data drop/injection), then again behaves good to reset suspicion.

2. **Baseline capture / instrumentation**

   * Log normal node behaviour for periods: measurement frequency, drop rates, latency, data values, node uptime, registration events.
   * Record metrics such as trust score/time series per node, volatility of behaviour.

3. **Static review (SAST) & configuration check**

   * Review firmware/node software for missing anomaly detection, missing behaviour-logging, missing fallback or trust drop logic.
   * Review mobile/gateway/apps/cloud code: do they continuously monitor per-node behaviour over time (not just immediate failures)? Are there threshold checks for intermittent misbehaviour?
   * Verify backend has historical analytics and can track behavioural changes (On/Off pattern) rather than just binary up/down.

4. **Dynamic testing (DAST) &mdash; simulate On-Off behaviour**

   * In controlled testbed: take a node and simulate intermittent faults: for example, drop data every alternate hour, send bogus data for short period, then resume normal behaviour.
   * Measure system’s ability to detect the change, flag the node, degrade its trust or isolate it.
   * Use mobile/gateway to simulate node switch between "good" and "bad" behaviour.

5. **Monitoring, anomaly detection & telemetry validation**

   * Use time-series analytics: monitor each node’s metrics for volatility, intra-daily variability as described in the reference.
   * Configure alerts: e.g., high variance in performance/trust, repeated transitions good→bad→good within short window.
   * Validate that cloud/mobile dashboards display node trust drift, not just immediate failure.

6. **Mobile & IoT integration tests**

   * On mobile gateways: apply tests where the gateway intermittently fails to forward node data, then forwards, to see if mobile app/gateway/ cloud detect.
   * On IoT: periodically send correct readings, then send incorrect or stop sending, then resume, to test detection of On-Off sequence.

7. **Reporting & remediation**

   * Identify: nodes lacking behaviour-monitoring, systems only checking immediate state but ignoring historical patterns, thresholds too generous, alerts too coarse.
   * Recommend: implement trust models factoring volatility, per-node historical pattern analytics, shorter windows for detection of behaviour shifts, automatic quarantine of nodes with suspicious On-Off switching.
   * Retest simulation to confirm detection and logging work.

---

## 2. Security Test Approaches & Tools


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
      <td>Behaviour simulation – node alternates good/bad (On-Off)</td>
      <td>Custom test harness (Raspberry Pi/ESP32 sim node) + scripting</td>
      <td>&mdash; (custom)</td>
      <td>IoT nodes/gateway</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Firmware/software review for missing historical anomaly logic</td>
      <td>Ghidra / Binwalk</td>
      <td>https://ghidra-sre.org/ , https://github.com/ReFirmLabs/binwalk</td>
      <td>IoT nodes/gateway</td>
    </tr>
    <tr>
      <td>White-box</td>
      <td>SAST</td>
      <td>Backend code review – trust model & time-series analytics support</td>
      <td>Semgrep / CodeQL</td>
      <td>https://semgrep.dev/ , https://github.com/github/codeql</td>
      <td>Cloud backend</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Telemetry time-series anomaly monitoring</td>
      <td>Elastic Stack (Beats + Kibana) / Splunk</td>
      <td>https://www.elastic.co/elastic-stack/ , https://www.splunk.com/</td>
      <td>Both (mobile/gateway/cloud)</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>Network packet sniffing: detect alternating drop/injection pattern</td>
      <td>Wireshark / Zeek</td>
      <td>https://www.wireshark.org/ , https://www.zeek.org/</td>
      <td>Both</td>
    </tr>
    <tr>
      <td>Gray-box</td>
      <td>DAST</td>
      <td>Mobile/gateway instrumentation – simulate node bad behaviour then good</td>
      <td>Frida (mobile) + custom scripts (gateway)</td>
      <td>https://frida.re/</td>
      <td>Android, iOS, gateway</td>
    </tr>
    <tr>
      <td>Black-box</td>
      <td>DAST</td>
      <td>User behaviour analytics (nodes switching states) & alerting test</td>
      <td>UEBA tool (ex: Elastic UBA module) / Splunk UBA</td>
      <td>https://www.elastic.co/elastic-stack/ , https://www.splunk.com/</td>
      <td>Cloud/mobile/gateway</td>
    </tr>
  </tbody>
</table>

---

## Practical Testbed / Setup Checklist

* **Node fleet in lab**: Deploy a set of test IoT nodes (e.g., ESP32, nRF52) each reporting telemetry to gateway/cloud. Tag each node with ID and initial “healthy” behaviour.
* **Baseline period**: For a period (e.g., 24-48 h) run nodes with normal behaviour (steady telemetry, no failures), record metrics: data rates, error/drop rates, latency.
* **On-Off simulation**: For one or more nodes, script the following pattern: for “On” period → normal operation, then switch to “Off” behaviour → drop data or inject incorrect data for defined window, then switch back to “On”. E.g., 6 h good, 30 min bad, 6 h good, 30 min bad etc.
* **Mobile/gateway test**: Have gateway/mobile client relay node data to cloud; instrument gateway to simulate the node’s On/Off behaviour (# alternate drops/altered readings) and check whether gateway/mobile or cloud flags anomaly.
* **Telemetry logging**: Have cloud backend collect node-id, timestamp, behaviour status (healthy vs drop/fault), trust-score metrics; ensure dashboards display each node’s behaviour over time.
* **Detection validation**: Set alert threshold based on intra-daily variability (IV) or other metric (from reference) that captures frequent transitions between good and bad.
* **Network packet capture**: Use Wireshark/Zeek on gateway link to capture node traffic; analyze for patterns of alternating good/bad behaviour (e.g., sequence of normal upticks then drop/injection then normal).
* **Mobile instrumentation**: If mobile app controls or monitors nodes, use Frida to simulate node switching state and verify mobile UI/backend alerts.
* **Remediation validation**: After applying or enabling detection logic, re-run scripts and confirm that On-Off nodes are flagged/quarantined/isolated.

---

## 4. References

1. Labraoui, N., Gueroui, M., Sekhri, L. (2015). On-Off Attacks Mitigation against Trust Systems in Wireless Sensor Networks. In: Amine, A., Bellatreche, L., Elberrichi, Z., Neuhold, E., Wrembel, R. (eds) Computer Science and Its Applications. CIIA 2015. *IFIP Advances in Information and Communication Technology*, vol 456. Springer, Cham. [https://doi.org/10.1007/978-3-319-19578-0_33](https://doi.org/10.1007/978-3-319-19578-0_33).
2. Caminha, J., Perkusich, A., & Perkusich, M. (2018). A smart trust management method to detect on‐off attacks in the Internet of Things. Security and Communication Networks, 2018(1), 6063456.
3. Perrone, L. F., & Nelson, S. C. (2006, September). A study of on-off attack models for wireless ad hoc networks. In *2006 1st Workshop on Operator-Assisted (Wireless Mesh) Community Networks* (pp. 1-10). IEEE.
4. Savva, M., Ioannou, I., & Vassiliou, V. (2022, June). Fuzzy-logic based IDS for detecting jamming attacks in wireless mesh IoT networks. In *2022 20th Mediterranean Communication and Computer Networking Conference (MedComNet)* (pp. 54-63). IEEE.
5. Li, W., Meng, W., & Kwok, L. F. (2018). Investigating the influence of special on–off attacks on challenge-based collaborative intrusion detection network. *Future Internet*, 10(1), 6. [https://doi.org/10.3390/fi10010006](https://doi.org/10.3390/fi10010006).
