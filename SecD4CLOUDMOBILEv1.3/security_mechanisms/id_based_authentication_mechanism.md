# ID-based Authentication Mechanisms 

ID-based authentication mechanisms are used to authenticate users in cloud-based mobile applications. This type of authentication typically involves the use of an identifier such as an email address or phone number, as well as a password or some other form of proof of identity. ID-based authentication may also involve the use of biometric markers like fingerprints or facial recognition to verify the user's identity. By using ID-based authentication, mobile applications can ensure that only authorized users are granted access, thereby protecting the data stored and exchanged on the application.

## ID-based Authentication Mechanisms Examples: 

| Security Requirement | Mobile Platform | Mechanism | Description | OSI Layer |
| --------------- | --------------- | ----------- | ----------- | --------- |
| Authentication | iOS | FaceID | User authenticates with their face | Layer 7 |
| Authentication | iOS | Touch ID | User authenticates with their thumbprint | Layer 7 | 
| Authorization | iOS | Apple App Tracking Transparency (ATT) | Authorizes a user’s usage data to be tracked by a third-party for targeted advertising | Layer 7 |
| Authentication | Android | Fingerprint Authenticator | User authenticates with their fingerpring | Layer 7 |
| Authentication | Android | Face Unlock | User authenticates with their face | Layer 7 |
| Authorization | Android | Google Play Billing Library | User authorizes payment for in-app billing | Layer 7 |