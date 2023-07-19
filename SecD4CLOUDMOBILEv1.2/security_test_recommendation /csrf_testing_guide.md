# Testing the CSRF Attack 

Below are the steps to test for a CSRF attack:

1. Ensure that the application is properly allowing and validating CSRF tokens.
2. Identify all form entry points in the application.
3. Use a proxy tool such as Burp Suite to intercept the request.
4. Modify the request on the proxy tool with an incorrect CSRF token.
5. Submit the request and observe the response.
6. If an error is returned, the application is properly validating the token and the attack is not successful.
7. If the request is accepted, the application is not properly validating the CSRF token and the attack is successful.

## Testing Tools: 

| Target Testing    | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform |
|------------------ |------------------|--------------|------------|----------|----------------|
| CSRF Attack      | White-Box        | Dynamic      | Manual     | Burp Suite | iOS & Android  |
|                   | Grey-Box         | Static       | Automated  | Nikto      | IOS & Android  |
|                   | Black-Box        | Hybrid       | Automated  | Owasp Zap  | iOS & Android  |