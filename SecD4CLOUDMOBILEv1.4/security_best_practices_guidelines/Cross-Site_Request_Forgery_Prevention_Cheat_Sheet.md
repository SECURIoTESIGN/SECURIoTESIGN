# Security Best Practices Guidelines for CSRF 

## CSRF Prevention Best Practices

Cross-site request forgery (CSRF) is a type of attack that allows an attacker to force an authorized user to initiate an action on a web application without their consent. These attacks are sneaky because they are hard to detect until it is too late. To prevent these attacks, it is important to implement proper CSRF protection best practices.

1. **Generate Unique and Unpredictable Tokens** 
    - Generate unique CSRF tokens when the user is authenticated. These tokens should be unpredictable generated and associated with the user session.

2. **Validate Tokens on All Requests**
    - Make sure to check if the CSRF token is present in requests and validate it against the token stored in the session.

3. **Use Same-Domain Cookies**
    - Make sure to keep the cookie domain and the website domain the same so that the cookies are not accessible cross-domain.

4. **Use POST Requests Instead of GET Requests**
    - GET requests can be easily manipulated by attackers, so use POST requests instead. This way even if the request is compromised the data is not sent to the client.

5. **Whitelist HTTP Referers**
    - Your website should only accept requests from whitelisted referrers. This way malicious requests can be easily identified.

6. **Log Suspicious Activity**
    - Keep track of all suspicious requests sent to your website and log them. This can help you identify and investigate possible attacks.

7. **Validate User Inputs**
    - Make sure to validate user inputs against known and acceptable values. This helps in filtering out malicious requests.

8. **Implement Open Redirect Protection**
    - Open redirects can be used in CSRF attacks, so it is important to implement open redirect protection to avoid such attacks.

Following these CSRF prevention best practices can help keep your website and users safe from malicious attackers.