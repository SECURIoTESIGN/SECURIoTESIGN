# Testing the Session Fixation Attack 

## Testing for Session Fixation Attack

1. Start by testing for session fixation with known tokens. Generate a known token, log into the application and submit the known token in the login form. If the application successfully logs into the system, the application may be vulnerable to session fixation.

2. If the form does not accept known tokens and does not reissue the token, the application may be vulnerable to session fixation.

3. Insert a tracking or logging code into the application and try to use different known tokens and see if they are accepted by the application.

4. After logged in, renew the session and check if the session ID is changed. If it is same as before, it might be vulnerable to session fixation.

5. Log out of the application and try to use the session ID that was captured during login. If the application continues to use the same session ID, it might be vulnerable to session fixation.

6. Create a honeypot page that only registered users can access. Log in with a known token and try to access the page. If the application allows access to the page using the known token, the application might be vulnerable to session fixation.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool  | Mobile Platform 
--- | --- | --- | --- | --- | --- 
Session Fixation Attack | White-box | Dynamic | Automated | Web security scanner (e.g. Acunetix, Netsparker, Burp Suite) | N/A 
Session Fixation Attack | Grey-box | Dynamic | Automated | Web security scanner (e.g. Acunetix, Netsparker, Burp Suite) | N/A 
Session Fixation Attack | Black-box | Dynamic | Automated | Web security scanner (e.g. Acunetix, Netsparker, Burp Suite) | N/A 
Session Fixation Attack | White-box | Static | Automated | Code security scanner (e.g. Checkmarx, Veracode, SonarQube) | N/A
Session Fixation Attack | Grey-box | Static | Automated | Code security scanner (e.g. Checkmarx, Veracode, SonarQube) | N/A 
Session Fixation Attack | Black-box | Static | Automated | Code security scanner (e.g. Checkmarx, Veracode, SonarQube) | N/A  
Session Fixation Attack | White-box | Hybrid | Automated | Code and web vulnerability scanner (e.g. Appscan, Appspider, Arachni) | N/A 
Session Fixation Attack | Grey-box | Hybrid | Automated | Code and web vulnerability scanner (e.g. Appscan, Appspider, Arachni) | N/A 
Session Fixation Attack | Black-box | Hybrid | Automated | Code and web vulnerability scanner (e.g. Appscan, Appspider, Arachni) | N/A 
Session Fixation Attack | White-box | Dynamic | Manual | N/A | N/A 
Session Fixation Attack | Grey-box | Dynamic | Manual | N/A | N/A 
Session Fixation Attack | Black-box | Dynamic | Manual | N/A | N/A 
Session Fixation Attack | White-box | Static | Manual | N/A | N/A 
Session Fixation Attack | Grey-box | Static