## Web Service


**Transport Confidentiality**	
All communication with and between web services containing sensitive features, an authenticated session, or transfer of sensitive data must be encrypted using well configured TLS. This is recommended even if the messages themselves are encrypted because TLS provides numerous benefits beyond traffic confidentiality including integrity protection, replay defenses, and server authentication. 


**Server Authentication**	
TLS must be used to authenticate the service provider to the service consumer. The service consumer should verify the server certificate is issued by a trusted provider, is not expired, is not revoked, matches the domain name of the service, and that the server has proven that it has the private key associated with the public key certificate (by properly signing something or successfully decrypting something encrypted with the associated public key).


**User Authentication**	
User authentication verifies the identity of the user or the system trying to connect to the service. 

* If used, Basic Authentication must be conducted over TLS, but Basic Authentication is not recommended.
* Client Certificate Authentication using TLS is a strong form of authentication that is recommended.


**Transport Encoding**	
SOAP encoding styles are meant to move data between software objects into XML format and back again.

> Enforce the same encoding style between the client and the server.


**Message Integrity, Confidentiality and Size**	
Integrity of data in transit can easily be provided by TLS. When using public key cryptography, encryption does guarantee confidentiality but it does not guarantee integrity since the receiver's public key is public. For the same reason, encryption does not ensure the identity of the sender. 			
Data elements meant to be kept confidential must be encrypted using a strong encryption cipher with an adequate key length to deter brute forcing.	
Web services like web applications could be a target for DOS attacks by automatically sending the web services thousands of large size SOAP messages. This either cripples the application making it unable to respond to legitimate messages or it could take it down entirely.

* For XML data, use XML digital signatures to provide message integrity using the sender's private key. This signature can be validated by the recipient using the sender's digital certificate (public key).
* Messages containing sensitive data must be encrypted using a strong encryption cipher. This could be transport encryption or message encryption.
* SOAP Messages size should be limited to an appropriate size limit. Larger size limit (or no limit at all) increases the chances of a successful DoS attack.



**Authorization**	
Web services need to authorize web service clients the same way web applications authorize users. A web service needs to make sure a web service client is authorized to: perform a certain action on the requested data.

* A web service should authorize its clients whether they have access to the method in question. Following authentication, the web service should check the privileges of the requesting entity whether they have access to the requested resource. This should be done on every request.
* Ensure access to administration and management functions within the Web Service Application is limited to web service administrators. Ideally, any administrative capabilities would be in an application that is completely separate from the web services being managed by these capabilities, thus completely separating normal users from these sensitive functions.


**Content Validation**	
Like any web application, web services need to validate input before consuming it. Content validation for XML input should include:

* Validation against malformed XML entities.
* Validation against XML Bomb attacks.
* Validating inputs using a strong white list.
* Validating against external entity attacks.




**Availability**		
XML Denial of Service is probably the most serious attack against web services. So the web service must provide the following validation:

* Validation against recursive payloads.
* Validation against oversized payloads.
* Protection against XML entity expansion.
* Validating against overlong element names. If you are working with SOAP-based Web Services, the element names are those SOAP Actions.

This protection should be provided by your XML parser/schema validator. To verify, build test cases to make sure your parser to resistant to these types of attacks.