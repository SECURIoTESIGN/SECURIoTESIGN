# Flooding Attack Model

## Definition
A **flooding attack** (DoS/DDoS) attempts to overwhelm a target’s resources—bandwidth, connection state, CPU, memory or application threads—by sending large volumes of traffic or resource-exhausting requests, rendering the service unavailable to legitimate users. Common forms include volumetric floods, protocol-level exhaustion (e.g., SYN floods), amplification/reflection attacks, and application-layer floods (e.g., HTTP GET/POST floods).

---

## Attack Categories

- **Volumetric / Bandwidth floods:** UDP, ICMP floods — saturate network links.
- **Amplification / Reflection:** DNS, NTP amplification — small query → large reply to victim.
- **Protocol-level exhaustion:** SYN floods, fragmented-packet attacks — exhaust connection tables or protocol state.
- **Application-layer (L7) floods:** HTTP GET/POST, slow-loris — consume server threads/CPU while appearing legitimate.
- **Network device floods:** MAC table flooding, broadcast storms — target network infrastructure.

---

## Mitigation (practical controls)
**Network/ISP:** ingress filtering (BCP38), upstream filtering/scrubbing, traffic sinkholing (as last resort).

**Transport/Protocol:** SYN cookies, TCP backlog tuning, connection rate limiting, fragment reassembly limits.

**Application:** WAF + rate limits, CAPTCHAs/challenges for suspicious flows, connection timeouts to mitigate slow attacks.

**Architecture & Ops:** CDN/Anycast, autoscaling with graceful degradation, monitoring/alerting baselines, runbooks and ISP/CERT contacts.

**Hygiene:** close open resolvers, disable unnecessary UDP services, patch and limit public-facing endpoints.

---

## DREAD Risk Assessment (0-10)

| Factor | Score | Rationale |
|---|---:|---|
| Damage Potential | 8 | Service outage, revenue/SLA impact. |
| Reproducibility | 9 | Techniques/tools/botnets widely available. |
| Exploitability | 7 | From trivial volumetric to moderately complex L7 attacks. |
| Affected Users | 9 | Public service → most or all users affected. |
| Discoverability | 8 | Public endpoints, open resolvers, measurable traffic spikes. |

**Average DREAD = (8+9+7+9+8)/5 = 8.2**; Rating: **High / Critical**

**Action Priority:** Immediate mitigation (edge rate-limits, WAF/CDN activation, ISP coordination); medium-term: scrubbing agreements, automated runbooks; long-term: resilient architecture (Anycast, geo-distribution).

---

## Key Metrics to Monitor

Bandwidth (bps), Packets-per-second (PPS), Concurrent connections, TCP SYN rates, HTTP request rates, 5xx error rates, latency percentiles, geographic anomalies.

---

## References

1. [Cloudflare — What is a DDoS attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/?utm_source=chatgpt.com). 
2. [Akamai — HTTP Flood DDoS Attack](https://www.akamai.com/glossary/what-is-an-http-flood-ddos-attack?utm_source=chatgpt.com)  
3. [AWS/Azure DDoS best practices](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/mitigation-techniques.html?utm_source=chatgpt.com)  
4. [OWASP — Denial of Service guidance](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html?utm_source=chatgpt.com)

---

## Flooding Attack Tree Diagram