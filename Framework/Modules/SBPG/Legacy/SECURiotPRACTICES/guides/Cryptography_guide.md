## Cryptography	

An architectural decision must be made to determine the appropriate method to protect data at rest. There are such wide varieties of products, methods and mechanisms for cryptographic storage.The general practices and required minimum key length depending on the scenario listed below: 

 * Key exchange: Diffie-Hellman key exchange with minimum 2048 bits 
 * Message Integrity: HMAC-SHA2 
 * Message Hash: SHA2 256 bits 
 * Asymmetric encryption: RSA 2048 bits 
 * Symmetric encryption: AES 128 bits 
 * Password Hashing: Argon2, PBKDF2, Scrypt, Bcrypt 

**Secure Cryptographic Storage Design:** 

 * All protocols and algorithms for authentication and secure communication should be well vetted by the cryptographic community. 
 * Ensure certificates are properly validated against the hostnames users  whom they are meant for. 
 * Avoid using wildcard certificates unless there is a business need for it 
 * Maintain a cryptographic standard to ensure that the developer community knows about the approved ciphersuits for network security protocols, algorithms, permitted use, cryptoperiods and Key Management. 
 * Only store sensitive data that you need 

**Use strong approved Authenticated Encryption**		
CCM or GCM are approved Authenticated Encryption modes based on AES algorithm. 

**Use strong approved cryptographic algorithms** 

* Do not implement an existing cryptographic algorithm on your own, no matter how easy it appears. * Instead, use widely accepted algorithms and widely accepted implementations.  
* Only use approved public algorithms such as AES, RSA public key cryptography, and SHA-256 or better for hashing. 
* Do not use weak algorithms, such as MD5 or SHA1. 
* Avoid hashing for password storage,instead use Argon2, PBKDF2, bcrypt or scrypt.  
* See NIST approved algorithms or ISO TR 14742 "Recommendations on Cryptographic Algorithms or Algorithms", key size and parameters by  European Union Agency for Network and Information Security.  
* If a password is being used to protect keys then the password strength should be sufficient for the strength of the keys it is protecting.  * When 3DES is used, ensure K1 != K2 != K3, and the minimum key length must be 192 bits .  
* Do not use ECB mode for encrypting lots of data (the other modes are better because they chain the blocks of data together to improve the data security).

**Use strong random numbers**	

 * Ensure that all random numbers, especially those used for cryptographic parameters (keys, IV's, MAC tags), random file names, random GUIDs, and random strings are generated in a cryptographically strong fashion. 
 * Ensure that random algorithms are seeded with sufficient entropy. 
 * Tools like NIST RNG Test tool can be used to comprehensively assess the quality of a Random Number Generator by 
reading e.g. 128MB of data from the RNG source and then assessing its randomness properties with the tool. 

The following libraries are considered weak random numbers generators and should not be used: 

C library: random(), rand(), use getrandom(2) instead		
Java library: java.util.Random() instead use java.security.SecureRandom instead		
For secure random number generation, refer to NIST SP 800-90A. CTR-DRBG, HASH-DRBG, HMAC-DRBG are recommended


[https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)