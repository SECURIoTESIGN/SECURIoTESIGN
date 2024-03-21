# Testing the SQLi Attack 

## Testing SQLi Attack

### 1. Cross-Site Scripting (XSS)

Cross-site scripting (XSS) is a type of attack that involves a malicious script being injected into a website. When a user visits the website, the script is executed in their browser. To test for XSS, we can insert a malicious script into the website and see if the script is executed.

### 2. SQL Injection

SQL injection is a type of attack where malicious code is inserted into the SQL query in order to gain access to data stored in a database. To test for SQLi attacks, we can insert a malicious query into the website and check if it is executed on the database.

### 3. Parameter Tampering

Parameter tampering is a type of attack where parameters of a URL are modified to gain access to restricted information or data. To test for parameter tampering, we can change the values of URL parameters and see if the website is responding with different outputs.

### 4. Brute-Force Attack

Brute-force attacks are attempts to guess the username and password of a system using automated tools. To test for brute-force attacks, we can use tools that try different combinations of usernames and passwords and check if the system is able to detect the attempts.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform
----------- | --------------- | ------------ | ----------- | ---------- | -------------
SQLi Attack | White-box | Dynamic |  Manual | SQLMap | iOS / Android 
SQLi Attack | Grey-box | Static | Automated | OWASP ZAP | iOS / Android 
SQLi Attack | Black-box | Hybrid | Exploration | Burp Suite | iOS / Android