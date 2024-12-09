# Security Best Practices Guidelines for HTML5 Security 

## HTML5 Security Best Practices Guidelines 

#### Minimizing Cross-Site Scripting Vulnerabilities 

- Use [HTML Escaping](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet#RULE_.231_-_HTML_Escape_Before_Inserting_Untrusted_Data_into_HTML_Element_Content) when rendering user-provided data in HTML by default 
- When creating dynamic web pages, use [Content Security Policy](https://content-security-policy.com/) to restrict potentially dangerous operations like inline script and styles 

#### Preventing Cross-Origin Resource Sharing (CORS) Attacks

- [Limit who can access](https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/) your resources with a whitelist policy. This should include all hosts who are legitimate users of your resource. 
- [Validate requests](https://www.nczonline.net/blog/2010/05/25/cross-domain-ajax-with-cross-origin-resource-sharing/) according to your CORS policy. This includes checking the origin and methods of each incoming request. 

#### Securing Session Storage

-Use [server-side sessions](https://www.sitepoint.com/php-sessions-vs-cookies/) where possible to store user data and use [HTTPOnly cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#Secure_and_HttpOnly_cookies) for authentication tokens and session identifiers. 
- Never store sensitive user data in cookies. 

#### Keeping Your HTML5 Applications Secure

- Validate user input on both the client and server-side. 
- Use [encryption](https://www.howtogeek.com/204407/htg-explains-what-is-encryption-and-how-does-it-work/) on sensitive data and don’t rely on client-side encryption. 
- Limit who can exploit your application from the outside. Use authentication and authorization techniques to limit access to certain parts of the application to certain users. 
- Regularly