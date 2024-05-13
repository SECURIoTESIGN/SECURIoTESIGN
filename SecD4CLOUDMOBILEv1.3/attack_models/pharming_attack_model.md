# Pharming Attacks

A pharming attack is a form of cyberattack that redirects victims to fake websites, often without their knowledge. Let’s explore the details:

## Overview

* **Objective**: Trick users into visiting malicious websites that resemble legitimate ones.
* **Method**: Exploits the Domain Name System (DNS) to redirect users to spoofed sites.
* **Impact**: Can lead to data theft, credential harvesting, and financial fraud.

## How Pharming Works
1. **Malware-Based Pharming**:
* Users unknowingly acquire malware (e.g., Trojan horse or virus) via malicious emails or software downloads.
* The malware modifies locally hosted files and changes stored IP addresses.
* Victims are automatically redirected to the attacker’s fraudulent website when accessing the legitimate site.
2. DNS Server Poisoning:
* Corrupts DNS servers to direct website requests to alternate or fake IP addresses.
* Exploits vulnerabilities at the DNS server level.
* Users visit spoofed sites, believing they are legitimate.

## Consequences

1. Communication Disruption:
* Interrupts access to legitimate websites.
* Impacts online services, including banking and e-commerce.
1. Data Theft and Credential Harvesting:
* Attackers collect personal data, login credentials, and financial information.
* Victims unwittingly provide sensitive details on fake sites.

## Mitigation Strategies

1. **Secure DNS Practices**: Use DNSSEC (Domain Name System Security Extensions) to ensure that the DNS responses are not tampered with. This can prevent attackers from redirecting users to malicious sites.

2. **SSL Certificates**: Use SSL (Secure Sockets Layer) certificates for websites. This ensures that the connection between the user's browser and the server is encrypted and secure.

3. **Regular Software Updates**: Keep all software, including operating systems and applications, up to date. This helps to patch any known vulnerabilities that could be exploited by attackers.

4. **Firewalls and Intrusion Detection Systems (IDS)**: Use firewalls and IDS to monitor and control incoming and outgoing network traffic based on predetermined security rules.

5. **User Education**: Educate users about the risks of clicking on suspicious links and the importance of checking the URL in the address bar before entering any sensitive information.

6. **Two-Factor Authentication (2FA)**: Implement 2FA to add an extra layer of security. This requires users to provide two different authentication factors to verify themselves.

7. **Regular Audits and Penetration Testing**: Regularly conduct security audits and penetration testing to identify and fix any security vulnerabilities.

8. **Use of Secure Mobile Applications**: Encourage users to only download apps from trusted sources like official app stores, and to regularly update them.

Remember, security is a continuous process and it's important to stay updated with the latest threats and mitigation strategies.

## Architectural Risk Analysis of Pharming Vulnerability

The pharming attack targets users by redirecting them to fraudulent websites, often without their knowledge. Let’s assess the risk using the Common Vulnerability Scoring System (CVSS) v3.1:

### CVSS Metrics

| **Factor**                                                      | **Description**                                                                                                                  | **Value**                             |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Attack   Vector (AV):                                           | Social   (Exploits user trust and redirects to a phishing site)                                                                  | Social   (S)                          |
| Attack   Complexity (AC):                                       | Low   (Pharming websites can be relatively easy to set up)                                                                       | Low   (L)                             |
| Privileges   Required (PR):                                     | None   (User clicks the malicious link)                                                                                          | None   (N)                            |
| User   Interaction (UI):                                        | Required   (User clicks the malicious link)                                                                                      | Required   (R)                        |
| Scope   (S):                                                    | Account   Compromise (attacker gains access to user's account)                                                                   |         Unauthorized Access (U)       |
| Confidentiality   Impact (C):                                   | High   (attacker can steal confidential data)                                                                                    | High   (H)                            |
| Integrity   Impact (I):                                         | High   (attacker can tamper with data on the fake site)                                                                          | High   (H)                            |
| Availability   Impact (A):                                      | Low   (Doesn't affect application functionality)                                                                                 | Low   (L)                             |
| Base   Score (assuming High for Confidentiality and Integrity): | 0.85   * (AV:S/AC:L/PR:N/UI:R) * (S:U/C:H/I:H/A:L)                                                                               | 8.5   (High)                          |
| Temporal   Score (TS):                                          | Not   Applicable (N/A)                                                                                                           | N/A                                   |
| Environmental   Score (ES):                                     | Depends   on user awareness training, application security measures (e.g., SSL   certificate validation), anti-phishing features | Varies                                |
| Overall   CVSS Score                                            | Base   Score + TS + ES                                                                                                           |         Varies (Depends on ES)        |
| Risk   Rating                                                   | High   to Critical (Depends on ES)                                                                                               | High   to Critical                    |

Overall, Pharming poses a high to critical risk for mobile cloud-based applications that hold user's confidential data. Implementing a layered approach with user education, application security measures, and potential anti-phishing features can significantly reduce the risk.

*Remember, vigilance and proactive measures are essential to protect against pharming attacks.*
 
## Pharming Attack Tree Diagram