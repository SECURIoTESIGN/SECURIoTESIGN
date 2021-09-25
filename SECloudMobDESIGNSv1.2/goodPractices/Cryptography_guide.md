# Cryptography	

An architectural decision must be made to determine the appropriate method to protect data at rest. There are such wide varieties of products, methods and mechanisms for cryptographic storage.The general practices and required minimum key length depending on the scenario listed below: 

 
## Good practices

 * Cryptographic algorithms are up to date and in-line with industry standards. This includes, but is not limited to outdated block ciphers (e.g. DES), stream ciphers (e.g. RC4), as well as hash functions (e.g. MD5) and broken random number generators like Dual_EC_DRBG (even if they are NIST certified). All of these should be marked as insecure and should not be used and removed from the application and server.
 * Key lengths are in-line with industry standards and provide protection for sufficient amount of time. A comparison of different key lengths and protection they provide taking into account Moore's law is available online.
 * Cryptographic means are not mixed with each other: e.g. you do not sign with a public key, or try to reuse a keypair used for a signature to do encryption.
 * Cryptographic parameters are well defined within reasonable range. This includes, but is not limited to: cryptographic salt, which should be at least the same length as hash function output, reasonable choice of password derivation function and iteration count (e.g. PBKDF2, scrypt or bcrypt), IVs being random and unique, fit-for-purpose block encryption modes (e.g. ECB should not be used, except specific cases), key management being done properly (e.g. 3DES should have three independent keys) and so on.
 
## Recommended Algorithms 
 * Confidentiality algorithms: AES-GCM-256 or ChaCha20-Poly1305;
 * Integrity algorithms: SHA-256, SHA-384, SHA-512, Blake2;
 * Digital signature algorithms: RSA (3072 bits and higher), ECDSA with NIST P-384;
 * Key establishment algorithms: RSA (3072 bits and higher), DH (3072 bits or higher), ECDH with NIST P-384;
 * Application must be capable of using end-to-end encryption via SSL / TLS in relation to sensitive data in transit and at rest.

Additionally, you should always rely on secure hardware (if available) for storing encryption keys, performing cryptographic operations, etc.


## Secure Cryptographic Storage Design

 * All protocols and algorithms for authentication and secure communication should be well vetted by the cryptographic community. 
 * Ensure certificates are properly validated against the hostnames users  whom they are meant for. 
 * Avoid using wildcard certificates unless there is a business need for it 
 * Maintain a cryptographic standard to ensure that the developer community knows about the approved ciphersuits for network security protocols, algorithms, permitted use, cryptoperiods and Key Management. 
 * Only store sensitive data that you need 

## Use strong approved Authenticated Encryption		
CCM or GCM are approved Authenticated Encryption modes based on AES algorithm. 

## Use strong approved cryptographic algorithms 

 * Do not implement an existing cryptographic algorithm on your own, no matter how easy it appears. * Instead, use widely accepted algorithms and widely accepted implementations.  
 * Only use approved public algorithms such as AES, RSA public key cryptography, and SHA-256 or better for hashing. 
 * Do not use weak algorithms, such as MD5 or SHA1. 
 * Avoid hashing for password storage,instead use Argon2, PBKDF2, bcrypt or scrypt.  
 * See NIST approved algorithms or ISO TR 14742 "Recommendations on Cryptographic Algorithms or Algorithms", key size and parameters by  European Union Agency for Network and Information Security.  
 * If a password is being used to protect keys then the password strength should be sufficient for the strength of the keys it is protecting.  * When 3DES is used, ensure K1 != K2 != K3, and the minimum key length must be 192 bits .  
 * Do not use ECB mode for encrypting lots of data (the other modes are better because they chain the blocks of data together to improve the data security).

## Use strong random numbers	

 * Ensure that all random numbers, especially those used for cryptographic parameters (keys, IV's, MAC tags), random file names, random GUIDs, and random strings are generated in a cryptographically strong fashion. 
 * Ensure that random algorithms are seeded with sufficient entropy. 
 * Tools like NIST RNG Test tool can be used to comprehensively assess the quality of a Random Number Generator by reading e.g. 128MB of data from the RNG source and then assessing its randomness properties with the tool. 

The following libraries are considered weak random numbers generators and should not be used: 

* C library: random(), rand(), use getrandom(2) instead;		
* Java library: java.util.Random() instead use java.security.SecureRandom instead.		

For secure random number generation, refer to NIST SP 800-90A. CTR-DRBG, HASH-DRBG, HMAC-DRBG are recommended.


[https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)