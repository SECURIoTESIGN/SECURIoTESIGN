# Testing the XSS Attack 

**Testing XSS Attack**

1. Identify the potential injection points: 
   - Take a look at webpages for available input fields, parameters in a URL, cookies, and source code.
2. Input test payloads:
   - One of the most common XSS payloads is the `<script>alert(1)</script>` tag.
3. Monitor the response:
   - If your payload is successfully executed, you'll likely get an alert box or some other type of notification.
4. Assess for vulnerabilities:
   - Once you've confirmed where the vulnerabilities are, you can start to control and mitigate the attack.

**Prevention of XSS Attack**

1. Employees: 
   - Train employees to be aware of XSS attacks so they can spot and report suspicious activities.
2. Validate input: 
   - Validate and filter any user input to ensure that only properly formatted input is accepted.
3. Sanitize input: 
   - Sanitizing data is the process of removing Javascript, HTML, and other malicious code from user input.
4. Use Trusted data: 
   - Be sure to use trusted input whenever possible to minimize the chances of XSS attacks.
5. Use Security Headers: 
   - Use security headers, such as HTTP Strict Transport Security (HSTS), to help prevent XSS attacks.

## Testing Tools: 

Target Testing  | Testing Technique | Test Analysis | Test Method  | Test Tool | Mobile Platform
----------------|------------------|--------------|-------------|----------|----------------
XSS Attack     | White-box        | Dynamic      | Manual      | Burp Suite| iOS, Android 
                | Grey-box         | Static       | Automated   | HP WebInspect | 
                | Black-box        | Hybrid       |             | Acunetix    |