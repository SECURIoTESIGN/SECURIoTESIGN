

## CSRF Arquitectural Risk Analysis: 

## Architectural Risk Analysis of CSRF Vulnerability

####Description 

Cross-Site Request Forgery (CSRF) is a type of attack which occurs when a malicious website, email, or message causes the victim’s web browser to perform an unwanted action on a trusted site. It means that the malicious website can trick the user's browser into sending a malicious request to the vulnerable site without the user's knowledge.

####Scoring

| Category | Metric | Value |
| --- | --- | --- |
| Exploitability | Attack Vector | Network |
| Exploitability | Attack Complexity | Low | 
| Exploitability | Privileges Required | None | 
| Exploitability | User Interaction | Required | 
| Impact | Scope | Changed | 
| Impact | Confidentiality | Low |
| Impact | Integrity | Low | 
| Impact | Availability | None |

####Risk Score 

A risk score of 2.6 (from 0.0 to 10.0) is calculated according to the Common Vulnerability Scoring System v3.1.

####Mitigation Strategies

Strict measures should be taken to ensure that the web application is not vulnerable to the CSRF attack. The following approaches can be taken for protecting against CSRF attack:

1. Implement Cross-Site Request Forgery tokens.
2. Use Same-Site Cookies.
3. Use Captcha. 
4. Set HTTP headers like X-Frame-Options, X-XSS-Protection and Content-Security-Policy.
5. Implement Post/Redirect/Get design to all requests.
6. Use one-time tokens while sending forms.
7. Use JavaScript token validation.
8. Validate each request on server side.

## CSRF Arquitectural Risk Analysis: 

### Arquitectural Risk Analysis for CSRF Vulnerability

In accordance with Common Vulnerability Scoring System (CVSS) v3.1, the arquitectural risk analysis of cross site request forgery (CSRF) vulnerability will focus on the following metrics:

| Metric | Score |
|-------|------|
| Attack Vector | Network (AV:N) |
| Attack Complexity | Low (AC:L) |
| Privileges Required | None (PR:N) |
| User Interaction | None (UI:N) |
| Scope | Changed (S:C) |
| Confidentiality | None (C:N) |
| Integrity | None (I:N) |
| Availability | None (A:N) |
 
This risk is classified as a **CVSS v3.1 Base Score of 6.4**, with a **High Vector Severity (VSR) of 6.4**. The high vector severity indicates that the vulnerability has a high potential for exploitation and should be addressed with an urgency. 

This risk should be remediated immediately, as exploiting the vulnerability may result in malicious code execution, data manipulation/corruption, and other undesired system behaviors. It is recommended to implement mitigating technologies, such as input and output validation, content security policies, and request tokens to reduce the risk associated with this vulnerability.