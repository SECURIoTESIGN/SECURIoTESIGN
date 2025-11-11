# Server-Side Request Forgery (SSRF) Attacks Model

A **Server-Side Request Forgery (SSRF) Attack** is a critical web security vulnerability that targets the application server ability to make requests to other resources. In the Cloud-Mobile-IoT ecosystem, SSRF is particularly dangerous because it allows an external attacker to force a trusted, cloud-based application or API to interact with internal, protected network resources or other cloud services on their behalf.

-----

## Definition

A **Server-Side Request Forgery (SSRF) Attack** occurs when an attacker can control or partially control the target of a request made by a server-side application. The application is typically designed to fetch resources from a user-supplied URL (e.g., retrieving an image from an external website for processing). By manipulating the input URL parameter, the attacker forces the server to make a connection to an unintended internal resource.

In the cloud-mobile-IoT context, the compromised server (often a middleware or API gateway) acts as a **proxy for the attacker**, enabling it to:

  * Scan and attack the private network hosting other cloud services, databases, or IoT management dashboards.
  * Access **metadata services** unique to cloud providers (e.g., AWS EC2 metadata), which often contain highly sensitive credentials and access tokens.

-----

## Attack Categories

### 1\. Internal Network Exploration and Attack (Cloud/IoT Layer)

  * **Port Scanning:** The attacker uses the vulnerable cloud server to scan the internal network (e.g., `10.x.x.x` or `192.168.x.x`). By observing the server response time or error messages, the attacker can map the private topology, identify open ports, and discover internal services (e.g., an unauthenticated database).
  * **Internal Service Access:** The attacker targets administrative interfaces or other internal APIs (e.g., a service managing the fleet of **IoT devices**) that are typically unprotected because they assume network-level security. The trusted cloud server bypasses this perimeter defense.

### 2\. Cloud Metadata Service Exploitation (Cloud Layer)

  * **Metadata Access:** Cloud providers (like AWS, Azure, GCP) use local metadata services (e.g., accessible via `http://169.254.169.254` in AWS) to allow instances to retrieve configuration and credentials.
  * **Key Leakage:** The attacker forces the vulnerable server to request the metadata endpoint, which leaks the server **IAM role credentials**, security keys, and access tokens. These credentials can then be used to gain control over other resources in the cloud provider account.

### 3\. Blind SSRF (Data Leakage)

  * **Mechanism:** In some cases, the vulnerable application executes the request but does not return the response body to the attacker.
  * **Exploitation:** The attacker uses out-of-band communication (e.g., forcing the server to issue a DNS query to an attacker-controlled domain) to confirm the success of the attack and leak small amounts of data, even when the server response is "blind."

-----

## Mitigation Strategies

Mitigation must focus on strictly validating and sanitizing user input and adopting a defense-in-depth approach for internal resources.

### 1\. Input Validation and URL Filtering (Application/API Layer)

  * **Whitelisting:** The most robust defense. Restrict the target URLs to an **explicitly allowed list** (a whitelist) of domains and IP addresses. **Never** use a blacklist, as attackers can always find ways to bypass it (e.g., using IP shortcuts like `0.0.0.0` or different encoding schemes).
  * **URL Parsing and Sanitization:** Use a robust, standard URL parser to validate that the hostname is a public, resolvable address and is not using non-HTTP/HTTPS schemes (like `file://`, `ftp://`, or `gopher://`) which can be exploited.
  * **Disable Unused Protocols:** Disable or strictly limit the ability of the server to execute requests using non-HTTP protocols, especially those that can target local files (e.g., `file://`).

### 2\. Network and Cloud Hardening (Cloud/Network Layer)

  * **Network Segmentation:** Place internal services, databases, and IoT management consoles on private network segments (VPCs/subnets) that **cannot** be reached from the public internet or from the cloud server public interface.
  * **Metadata Access Control:** If using cloud metadata services, configure the instance roles with the absolute **Principle of Least Privilege**, ensuring the stolen credentials (if leaked) have minimal impact. Modern cloud services offer enhanced protections to limit the reach of the metadata endpoint.
  * **Internal Firewalls:** Use host-based firewalls or security groups to prevent the vulnerable application server from establishing connections to common internal IP ranges (e.g., `169.254.169.254`, `127.0.0.1`, `10.0.0.0/8`) and internal service ports.

-----

## DREAD Risk Assessment

The DREAD framework is used to quantify the risk of an SSRF attack, particularly in a cloud environment targeting internal resources or metadata.

| DREAD Factor | Assessment | Score (0-10) | Rationale for SSRF Attack |
| :--- | :--- | :--- | :--- |
| **D**amage Potential | **Catastrophic** | 10 | Allows access to internal networks, databases, and cloud metadata/IAM credentials, leading to total compromise of the entire cloud account and all tenant data. |
| **R**eproducibility | **Medium-High** | 7 | Highly reproducible once a vulnerable endpoint is found, as the attack relies on standard HTTP libraries in the server. Attackers can automate scanning for the internal resource (metadata IP). |
| **E**xploitability | **Medium** | 6 | Requires moderate skill to identify the vulnerable parameter and understand URL parsing/encoding bypasses. Tools exist to automate internal network scanning via SSRF. |
| **A**ffected Users | **Systemic** | 9 | Compromise of the cloud backend or metadata can affect all users and all linked IoT devices/services in the cloud account. |
| **D**iscoverability | **High** | 7 | Vulnerable API endpoints are easy to find through standard black-box testing (fuzzing URL parameters and observing behavior). Simple to check if a provided URL parameter is processed by the server. |
| **Total Risk Score** | **High** | 39/5 (**Average: 7.8**) | A critical, high-impact threat that turns a single server flaw into an internal network gateway for the attacker. |

-----

## References

  1. LeBlanc, D., & Howard, M. (2002). *Writing Secure Code* (2nd ed.). Microsoft Press. (For the foundational DREAD model)
  2. OWASP Foundation. (n.d.). **OWASP Top 10**. Retrieved from [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) (Relevant to A10:2021-Server-Side Request Forgery).
  3. Shostack, A. (2014). *Threat Modeling: Designing for Security*. Wiley.
  4. Sinha, K., & Bera, M. (2020). **A Study of Server-Side Request Forgery (SSRF) Attacks in Cloud Environment**. *International Journal of Advanced Computer Science and Applications (IJACSA)*, *11*(6), 46-53.
  5. Soni, S., & Singh, J. (2022). **Mitigation of Server-Side Request Forgery (SSRF) Attacks in Internet of Things (IoT) Environment**. *Journal of Physics: Conference Series*, *2161*(1), 012015.
  6. Jabiyev, B., et al., 2021. Preventing Server-Side Request Forgery Attacks. Association for Computing Machinery, New York, NY, USA. p. 1626–1635. URL: https://doi.org/10.1145/3412841.3442036.800-63-3.pdf, doi:https://doi.org/10.6028/NIST.SP.800-63-3.

 -----

## SSRF Attack Tree Diagram


