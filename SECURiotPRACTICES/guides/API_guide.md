## API Security Guide

Secure REST services must only provide HTTPS endpoints. This protects authentication credentials in transit, for example passwords, API keys or JSON Web Tokens. It also allows clients to authenticate the service and guarantees integrity of the transmitted data.


Non-public REST services must perform access control at each API endpoint. 	
Web services in monolithic applications implement this by means of user authentication, authorisation logic and session management.


* In order to minimise latency and reduce coupling between services, the access control decision should be taken locally by REST endpoints
* User authentication should be centralised in a Identity Provider (IdP), which issues access tokens


**JWT**		
There seems to be a convergence towards using JSON Web Tokens (JWT) as the format for security tokens. JWTs are JSON data structures containing a set of claims that can be used for access control decisions. A cryptographic signature or message authentication code (MAC) can be used to protect the integrity of the JWT.

* Ensure JWTs are integrity protected by either a signature or a MAC. Do not allow the unsecured JWTs: {"alg":"none"}. 
* In general, signatures should be preferred over MACs for integrity protection of JWTs.
* A relying party must verify the integrity of the JWT based on its own configuration or hard-coded logic. It must not rely on the information of the JWT header to select the verification algorithm.

Some claims have been standardised and should be present in JWT used for access controls. At least the following of the standard claims should be verified:

* iss or issuer - is this a trusted issuer? Is it the expected owner of the signing key?
* aud or audience - is the relying party in the target audience for this JWT?
* exp or expiration time - is the current time before the end of the validity period of this token?
* nbf or not before time - is the current time after the start of the validity period of this token?


**API Keys**
Public REST services without access control run the risk of being farmed leading to excessive bills for bandwidth or compute cycles. API keys can be used to mitigate this risk. API keys can reduce the impact of denial-of-service attacks. However, when they are issued to third-party clients, they are relatively easy to compromise.

* Require API keys for every request to the protected endpoint.
* Return 429 Too Many Requests HTTP response code if requests are coming in too quickly.
* Revoke the API key if the client violates the usage agreement.
* Do not rely exclusively on API keys to protect sensitive, critical or high-value resources.

**Restrict HTTP methods**

* Apply a whitelist of permitted HTTP Methods e.g. GET, POST, PUT.
* Reject all requests not matching the whitelist with HTTP response code 405 Method not allowed.
* Make sure the caller is authorised to use the incoming HTTP method on the resource collection, action, and record

**Input validation**


* Do not trust input parameters/objects.
* Validate input: length / range / format and type.
* Achieve an implicit input validation by using strong types like numbers, booleans, dates, times or fixed data ranges in API parameters.
* Constrain string inputs with regexps.
* Reject unexpected/illegal content.
* Make use of validation/sanitation libraries or frameworks in your specific language.
* Define an appropriate request size limit and reject requests exceeding the limit with HTTP response status 413 Request Entity Too Large.
* Consider logging input validation failures. Assume that someone who is performing hundreds of failed input validations per second is up to no good.
* Have a look at input validation cheat sheet for comprehensive explanation.
* Use a secure parser for parsing the incoming messages. If you are using XML, make sure to use a parser that is not vulnerable to XXE and similar attacks

**Validate Content Types**


 * Reject requests containing unexpected or missing content type headers with HTTP response status 406 Unacceptable or 415 Unsupported Media Type.
 * For XML content types ensure appropriate XML parser hardening.
 * Avoid accidentally exposing unintended content types by explicitly defining content types e.g. Jersey (Java) @consumes("application/json"); @produces("application/json"). 
 * Do NOT simply copy the Accept header to the Content-type header of the response.
 * Ensure sending intended content type headers in your response matching your body content e.g. application/json and not application/javascript

**Management endpoints**

* Avoid exposing management endpoints via Internet.
* If management endpoints must be accessible via the Internet, make sure that users must use a strong authentication mechanism, e.g. multi-factor.
* Expose management endpoints via different HTTP ports or hosts preferably on a different NIC and restricted subnet.
* Restrict access to these endpoints by firewall rules  or use of access control lists.

**Error handling**

* Respond with generic error messages - avoid revealing details of the failure unnecessarily.
* Do not pass technical details (e.g. call stacks or other internal hints) to the client.

**Audit logs**

* Write audit logs before and after security related events.
* Consider logging token validation errors in order to detect attacks.
* Take care of log injection attacks by sanitising log data beforehand.

**Sensitive information in HTTP requests**
RESTful web services should be careful to prevent leaking credentials. Passwords, security tokens, and API keys should not appear in the URL, as this can be captured in web server logs, which makes them intrinsically valuable.

* In POST/PUT requests sensitive data should be transferred in the request body or request headers.
* In GET requests sensitive data should be transferred in an HTTP Header.

OK:

> https://example.com/resourceCollection/[ID]/action ; https://twitter.com/vanderaj/lists

NOT OK:

> https://example.com/controller/123/action?apiKey=a53f435643de32 because API Key is into the URL.