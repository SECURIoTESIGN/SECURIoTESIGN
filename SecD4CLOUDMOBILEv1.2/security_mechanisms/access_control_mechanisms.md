# Access Control Mechanisms 

Security Access Control Mechanisms (SACMs) are the technical and administrative strategies and tools used to protect cloud-based mobile apps from unauthorized access to confidential data and systems. These mechanisms are designed to restrict access to certain users, manage user privileges, authenticate user accounts, and authorize access requests. Examples of SACMs include multi-factor authentication (MFA), biometric authentication, single-sign-on (SSO), role-based access control (RBAC), application-level encryption, and least privilege access. SACMs allow organizations to properly control who has access to what resources and strictly enforce principles of confidentiality, privacy, and data security.

## Access Control Mechanisms Examples: 

Security Requirement | Mobile Platform | Mechanism | Description | OSI Layer
--------------------|----------------|----------|------------|-----------
Data confidentiality | Android | RSA Encryption | Encryption of data with public and private keys | Application
Data integrity | Android | Hashing | Use of a hash algorithm such as SHA-2 to ensure that data is not tampered with | Transport
Account Management | iOS | Two-Factor Authentication | Use of two-factor authentication to verify user access | Presentation
Data access control | iOS | Role-Based Access Control (RBAC) | Defines levels of access based on user roles | Application
Resource authorization | iOS | Authorization Token | Generates a token at the end of a successful authorization process which is used to grant permission | Application