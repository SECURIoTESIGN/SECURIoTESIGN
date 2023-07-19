# SSRF Attacks

In this type of attack, which aims to force the server to make a request to itself, to services running on the server's internal network, or to external third parties, an attacker exploits the validation of improper entries by submitting malicious entries created to a server-side target application.


## Definition

We are in the presence of a Server Side Request Forgery Attack (SSRF) as long as the web application is vulnerable and redirects the attacker's requests to the internal network and exposes local services to the remote attacker, which introduces different forms of risks. According~\cite{10.1145/3412841.3442036}, this type of attack can exploit internal services in different ways, from sending spam emails to remotely executing operating system commands on servers that are running web applications. In case the vulnerable server (i.e. the server running the vulnerable web application) is hosted on a remote server in the Cloud, SSRF attacks require less effort from attackers, causing a higher impact in terms of dangerousness in terms of data leakage or theft. 

 * In-band SSRF attack;
 * Out-of-band SSRF attack.
 
## Technical Impact
* Modify and Read Data; 
* Resource Consumption.

## Risk Analysis
  * High Risk.

## Likelihood of Exploit
  * High.

## Attacker Powers

 * Access sensitive data;
 * Execute commands on the server’s network;
 * Make external requests with the stolen identity of the server.

## Recommendations

In order to ensure that the mobile application is resilient or immune to the SSRF attacks, it is recommended that the measures described in the good practice report and the security testing present in the full report are followed.

## References
1. Jabiyev, B., et al., 2021. Preventing Server-Side Request Forgery Attacks. Association for Computing Machinery, New York, NY, USA. p. 1626–1635. URL: https://doi.org/10.1145/3412841.3442036.800-63-3.pdf, doi:https://doi.org/10.6028/NIST.SP.800-63-3.
2. [CAPEC-664: Server Side Request Forgery](https://capec.mitre.org/data/definitions/664.html).

## SSRF Attacks Diagram


