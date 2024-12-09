# Testing the Code Injection Attack 

Testing code injection attacks involve attempting to inject malicious code into a web application. Testing code injection is typically done using a few different methods.

1. Manual Tests: Manual tests involve manual input of potentially malicious code into user inputs and forms within the application. If the application does not appropriately filter or reject suspicious input, this can lead to the vulnerability.

2. Automation Tools: Automation tools, such as Security Scanners, can be used to test for code injection attacks. Tools such as these can detect code injection vulnerabilities with very high accuracy, allowing security teams to quickly identify and mitigate such risks.

3. Penetration Testing: Penetration testing is a manual assessment of security. During this process testers attempt to gain access to restricted areas within an application, by entering or manipulating code in user input fields. This will allow testers to identify potential security weaknesses in an application, and recommend remediation strategies.

## Testing Tools: 

| Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform |
| --------------- | ---------------- | ------------ | ----------- | --------- | -------------- |
| Code Injection | White-box | Dynamic | Unit Testing | HP QTP | Android |
| Code Injection | Grey-box | Dynamic | Penetration Testing | HP Fortify | Android |
| Code Injection | Black-box | Static | Security Scanning | Burp Suite | iOS |
| Code Injection | White-box | Hybrid | Code Review | Splint | iOS |