# Cryptographic Algorithms Mechanisms 

Cryptographic algorithms are used to ensure data confidentiality, authenticity, integrity and non-repudiation in cloud-based mobile apps. To achieve these goals, cryptographic algorithms are often used in combination with mechanisms, such as Digital Signatures, Secret Key Cryptography and Public Key Cryptography. 

Digital Signatures validate the identity and authenticity of communications, while Secret Key Cryptography algorithms like AES, DES and 3DES protect transmitted data through the use of encryption. Public Key Cryptography algorithms like RSA, ECDSA and Diffie-Hellman can also be used to authenticate, encrypt and exchange secret keys between the mobile device and the cloud provider. In addition, protocols such as SSL / TLS can add an extra layer of security while protecting and verifying the communication and providing message integrity.

## Cryptographic Algorithms Mechanisms Examples: 

| Security Requirement |Mobile Platform  |Mechanism       |Description                                                                                |OSI Layer  | Use for coding | Use for runtime |
|:-------------------:|:---------------|:---------------|:------------------------------------------------------------------------------------------|:---------:|:--------------:|:---------------:|
| Integrity           | Android        | HMAC-SHA256    | A cryptographic hash function based on SHA256 that combines a shared secret and the message | 7         | Yes            | Yes             |
| Confidentiality     | iOS            | AES-128        | AES with 128 bit key size that supports authenticated encryption                           | 6         | Yes            | Yes             |
| Authentication      | iOS            | ECDSA          | Elliptic Curve Digital Signature Algorithm that provides digital signatures                | 7         | Yes            | Yes             |