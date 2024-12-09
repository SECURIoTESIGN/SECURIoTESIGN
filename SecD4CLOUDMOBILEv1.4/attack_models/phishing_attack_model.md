# Phishing Attack 

Phishing is a type of cyber attack that uses social engineering tactics to steal data and information from unsuspecting victims. It is an attempt to unlawfully obtain sensitive information such as usernames, passwords, and credit card details by impersonating a trusted entity. Phishing attacks can be launched through email, instant message, text messages, or malicious websites.

## Mitigation

1. **Education and Awareness**: Conduct regular training and awareness programs to educate users about phishing attacks and how to identify them;

2. **Email Filters**: Use email filters to scan for phishing emails and block them;

3. **Firewalls**: Deploy firewalls to block malicious IP addresses and protect the network from phishing attacks;

4. **Anti-Phishing Toolbars**: Use anti-phishing toolbars that can run quick checks on the sites that you are visiting and compare them to lists of known phishing sites;

5. **Regular Updates**: Keep all systems and software updated with the latest security patches;

6. **Two-Factor Authentication (2FA)**: Implement two-factor authentication to add an extra layer of security;

7. **Regular Backups**: Regularly backup data to reduce the impact in case a phishing attack leads to data loss.

Please note that the effectiveness of these strategies may vary depending on the specific circumstances and the capabilities of the attacker. It's always a good idea to consult with a cybersecurity expert when dealing with these types of threats.

## Phishing Architectural Risk Analysis: 

The Common Vulnerability Scoring System (CVSS) is a framework for communicating the severity of software vulnerabilities. CVSS v3.1 is the latest version of CVSS, released in June 2019.
| **Factor**                                                      | **Description**                                                                                                                   | **Value**                             |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Attack   Vector (AV):                                           | Social   (Exploits user trust to reveal credentials)                                                                              | Social   (S)                          |
| Attack   Complexity (AC):                                       | Low   (Crafting phishing messages can be relatively easy)                                                                         | Low   (L)                             |
| Privileges   Required (PR):                                     | None   (User reveals credentials)                                                                                                 | None   (N)                            |
| User   Interaction (UI):                                        | Required   (User clicks the link or enters credentials)                                                                           | Required   (R)                        |
| Scope   (S):                                                    | Account   Compromise (attacker gains access to user's account)                                                                    |         Unauthorized Access (U)       |
| Confidentiality   Impact (C):                                   | High   (attacker can steal confidential data)                                                                                     | High   (H)                            |
| Integrity   Impact (I):                                         | High   (attacker can tamper with data within the account)                                                                         | High   (H)                            |
| Availability   Impact (A):                                      | Low   (Doesn't affect application functionality)                                                                                  | Low   (L)                             |
| Base   Score (assuming High for Confidentiality and Integrity): | 0.85   * (AV:S/AC:L/PR:N/UI:R) * (S:U/C:H/I:H/A:L)                                                                                | 8.5   (High)                          |
| Temporal   Score (TS):                                          | Not   Applicable (N/A)                                                                                                            | N/A                                   |
| Environmental   Score (ES):                                     | Depends   on user awareness training, application security measures (e.g., multi-factor   authentication), anti-phishing features | Varies                                |
| Overall   CVSS Score                                            | Base   Score + TS + ES                                                                                                            |         Varies (Depends on ES)        |
| Risk   Rating                                                   | High   to Critical (Depends on ES)                                                                                                | High   to Critical                    |

**Overall, Phishing poses a high to critical risk for mobile cloud-based applications that hold user's confidential data. Implementing a layered approach with user education, application security measures (like MFA), and potential anti-phishing features can significantly reduce the risk.**

## Phishing Attack Tree Diagram