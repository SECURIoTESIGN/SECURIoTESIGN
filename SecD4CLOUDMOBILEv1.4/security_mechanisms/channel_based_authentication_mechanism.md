# Channel-based Authentication Mechanisms 

Channel-based authentication mechanisms in cloud-based mobile apps refer to a set of security protocols that validate users and authorize access to specific resources in a cloud mobile application. This authentication is done through a set of channels, such as biometrics, passwords, OTPs, or mobile phone numbers, each with its own level of security and authentication request. This type of authentication is used to ensure access to sensitive data and improve the overall security of the application.

## Channel-based Authentication Mechanisms Examples: 

| Security Requirement | Mobile Plataform | Mechanism   | Description                                                                                                                   | OSI Layer     |
|---------------------|-----------------|-------------|-----------------------------------------------------------------------------------------------------------------------------|---------------|
| Authentication      | Android         | HMAC-SHA256  | Mobile application uses a pre-shared HMAC-SHA256 token to authenticate with the cloud server and establish a secure channel. | Application   |
| Authorization       | iOS             | OAuth-2      | Mobile application uses an OAuth-2 access token to authorize requests made to the cloud server and establish a secure channel. | Application   |
| Identity Management | Cross-platform  | OpenID Connect| Mobile application uses OpenID Connect to authenticate with the cloud server and establish a secure channel.                    | Application   |
| Data Encryption     | Cross-platform  | TLS/SSL      | Mobile application uses TLS/SSL to encrypt data transmitted between the mobile device and the cloud server.                    | Transport     |