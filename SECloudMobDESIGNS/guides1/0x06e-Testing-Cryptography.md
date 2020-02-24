## iOS Cryptography APIs

In the "Cryptography for Mobile Apps" chapter, we introduced general cryptography best practices and described typical problems that may occur when cryptography is used incorrectly. In this chapter, we'll detail the cryptography APIs available for iOS. We'll show how to identify usage of those APIs in the source code and how to interpret cryptographic configurations. When you're reviewing code, compare the cryptographic parameters with the current best practices linked in this guide.

### Verifying the Configuration of Cryptographic Standard Algorithms

#### Overview

Apple provides libraries that include implementations of most common cryptographic algorithms. [Apple's Cryptographic Services Guide](https://developer.apple.com/library/content/documentation/Security/Conceptual/cryptoservices/GeneralPurposeCrypto/GeneralPurposeCrypto.html "Apple Cryptographic Services Guide") is a great reference. It contains generalized documentation of how to use standard libraries to initialize and use cryptographic primitives, information that is useful for source code analysis.

##### CommonCrypto, SecKeyEncrypt and Wrapper libraries

The most commonly used Class for cryptographic operations is the CommonCrypto, which is packed with the iOS runtime. The functionality offered by the CommonCrypto object can best be dissected by having a look at the [source code of the header file](https://opensource.apple.com/source/CommonCrypto/CommonCrypto-36064/CommonCrypto/CommonCryptor.h.auto.html "CommonCrypto.h"):

- The `Commoncryptor.h` gives the parameters for the symmetric cryptographic operations,
- The `CommonDigest.h` gives the parameters for the hashing Algorithms
- The `CommonHMAC.h` gives the parameters for the supported HMAC operations.
- The `CommonKeyDerivation.h` gives the parameters for supported KDF functions
- The `CommonSymmetricKeywrap.h` gives the function used for wrapping a symmetric key with a Key Encryption Key.

Unfortunately, CommonCryptor lacks a few types of operations in its public APIs, such as: GCM mode is only available in its private APIs See [its sourcecode](https://opensource.apple.com/source/CommonCrypto/CommonCrypto-60074/include/CommonCryptorSPI.h "GCM in CC"). For this, an additional binding header is necessary or other wrapper libraries can be used.

Next, for asymmetric operations, Apple provides [SecKey](https://opensource.apple.com/source/Security/Security-57740.51.3/keychain/SecKey.h.auto.html "SecKey"). Apple provides a nice guide in its [Developer Documentation](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/using_keys_for_encryption "Using keys for encryption") on how to use this.

As noted before: some wrapper-libraries exist for both in order to provide convenience. Typical libraries that are used are, for instance:

- [IDZSwiftCommonCrypto](https://github.com/iosdevzone/IDZSwiftCommonCrypto "IDZSwiftCommonCrypto"),
- [Heimdall](https://github.com/henrinormak/Heimdall "Heimdall"),
- [SwiftyRSA](https://github.com/TakeScoop/SwiftyRSA "SwiftyRSA"),
- [SwiftSSL](https://github.com/SwiftP2P/SwiftSSL "SwiftSSL"),
- [RNCryptor](https://github.com/RNCryptor/RNCryptor "RNCryptor"),
- [Arcane](https://github.com/onmyway133/Arcane "Arcane")

##### Third party libraries

There are various third party libraries available, such as:

- CJOSE: With the rise of JWE, and the lack of public support for AES GCM, other libraries have found their way, such as [CJOSE](https://github.com/cisco/cjose "cjose"). CJOSE still requires a higher level wrapping as they only provide a C/C++ implementation.
- CryptoSwift: A library in Swift, which can be found at [GitHub](https://github.com/krzyzanowskim/CryptoSwift "CryptoSwift"). The library supports various hash-functions, MAC-functions, CRC-functions, symmetric ciphers, and password-based key derivation functions. It is not a wrapper, but a fully self-implemented version of each of the ciphers. It is important to verify the effective implementation of a function.
- OpenSSL: [OpenSSL](https://www.openssl.org/ "OpenSSL") is the toolkit library used for TLS, written in . Most of its cryptographic functions can be used to do the various cryptographic actions necessary, such as creating (H)MACs, signatures, symmetric- & asymmetric ciphers, hashing, etc.. There are various wrappers, such as [OpenSSL](https://github.com/ZewoGraveyard/OpenSSL "OpenSSL") and [MIHCrypto](https://github.com/hohl/MIHCrypto "MIHCrypto").
- LibSodium: Sodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more. It is a portable, cross-compilable, installable, packageable fork of NaCl, with a compatible API, and an extended API to improve usability even further. See [LibSodiums documentation](https://download.libsodium.org/doc/installation "LibSodium docs") for more details. There are some wrapper libraries, such as [Swift-sodium](https://github.com/jedisct1/swift-sodium "Swift-sodium"), [NAChloride](https://github.com/gabriel/NAChloride "NAChloride"), and [libsodium-ios](https://github.com/mochtu/libsodium-ios "libsodium ios").
- Tink: A new cryptography library by Google. Google explains its reasoning behind the library [in its security blog](https://security.googleblog.com/2018/08/introducing-tink-cryptographic-software.html "Introducing Tink"). The sources can be found at [Tinks GitHub repository](https://github.com/google/tink "Tink at GitHub").
- Themis: a Crypto library for storage and messaging for Swift, Obj-C, Android/Java, С++, JS, Python, Ruby, PHP, Go. [Themis](https://github.com/cossacklabs/themis "Themis") uses LibreSSL/OpenSSL engine libcrypto as a dependency. It supports Objective-C and Swift for key generation, secure messaging (e.g. payload encryption and signing), secure storage and setting up a secure session. See [their wiki](https://github.com/cossacklabs/themis/wiki/Objective-C-Howto "Themis wiki") for more details.
- Others: There are many other libraries, such as [CocoaSecurity](https://github.com/kelp404/CocoaSecurity "CocoaSecurity"), [Objective-C-RSA](https://github.com/ideawu/Objective-C-RSA "Objective-C-RSA"), and [aerogear-ios-crypto](https://github.com/aerogear/aerogear-ios-crypto "Aerogera-ios-crypto"). Some of these are no longer maintained and might never have been security reviewed. Like always, it is recommended to look for supported and maintained libraries.
- DIY: An increasing amount of developers have created their own implementation of a cipher or a cryptographic function. This practice is _highly_ discouraged and should be vetted very thoroughly by a cryptography expert if used.

#### Static Analysis

A lot has been said about deprecated algorithms and cryptographic configurations in section `Cryptography for Mobile Apps`. Obviously, these should be verified for each of the mentioned libraries in this chapter.
Pay attention to how-to-be-removed key-holding datastructures and plain-text data structures are defined. If the keyword `let` is used, then you create an immutable structure which is harder to wipe from memory. Make sure that it is part of a parent structure which can be easily removed from memory (e.g. a `struct` that lives temporally).

##### CommonCryptor

If the app uses standard cryptographic implementations provided by Apple, the easiest way to determine the status of the related algorithm is to check for calls to functions from `CommonCryptor`, such as `CCCrypt` and `CCCryptorCreate`. The [source code](https://opensource.apple.com/source/CommonCrypto/CommonCrypto-36064/CommonCrypto/CommonCryptor.h "CommonCryptor.h") contains the signatures of all functions of CommonCryptor.h. For instance, `CCCryptorCreate` has following signature:

```c
CCCryptorStatus CCCryptorCreate(
    CCOperation op,             /* kCCEncrypt, etc. */
    CCAlgorithm alg,            /* kCCAlgorithmDES, etc. */
    CCOptions options,          /* kCCOptionPKCS7Padding, etc. */
    const void *key,            /* raw key material */
    size_t keyLength,
    const void *iv,             /* optional initialization vector */
    CCCryptorRef *cryptorRef);  /* RETURNED */
```

You can then compare all the `enum` types to determine which algorithm, padding, and key material is used. Pay attention to the keying material: the key should be generated securely - either using a key derivation function or a random-number generation function.
Note that functions which are noted in chapter "Cryptography for Mobile Apps" as deprecated, are still programmatically supported. They should not be used.

##### Third party libraries

Given the continuous evolution of all third party libraries, this should not be the place to evaluate each library in terms of static analysis. Still there are some points of attention:

- **Find the library being used**: This can be done using the following methods:
- Check the [cartfile](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile "cartfile") if Carthage is used.
- Check the [podfile](https://guides.cocoapods.org/syntax/podfile.html "podfile") if Cocoapods is used.
- Check the linked libraries: Open the xcodeproj file and check the project properties. Go to the tab "Build Phases" and check the entries in "Link Binary With Libraries" for any of the libraries. See earlier sections on how to obtain similar information using [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF "MobSF").
- In the case of copy-pasted sources: search the headerfiles (in case of using Objective-C) and otherwise the Swift files for known methodnames for known libraries.
- **Determine the version being used**: Always check the version of the library being used and check whether there is a new version available in which possible vulnerabilities or shortcomings are patched. Even without a newer version of a library, it can be the case that cryptographic functions have not been reviewed yet. Therefore we always recommend using a library that has been validated or ensure that you have the ability, knowledge and experience to do validation yourself.
- **By hand?**: We recommend not to roll your own crypto, nor to implement known cryptographic functions yourself.

### Testing Random Number Generation

#### Overview

Apple provides a [Randomization Services](https://developer.apple.com/reference/security/randomization_services "Randomization Services") API, which generates cryptographically secure random numbers.

The Randomization Services API uses the `SecRandomCopyBytes` function to generate numbers. This is a wrapper function for the `/dev/random` device file, which provides cryptographically secure pseudorandom values from 0 to 255. Make sure that all random numbers are generated with this API. There is no reason for developers to use a different one.

#### Static Analysis

In Swift, the [`SecRandomCopyBytes` API](https://developer.apple.com/reference/security/1399291-secrandomcopybytes "SecRandomCopyBytes (Swift)") is defined as follows:

```swift
func SecRandomCopyBytes(_ rnd: SecRandomRef?,
                      _ count: Int,
                      _ bytes: UnsafeMutablePointer<UInt8>) -> Int32
```

The [Objective-C version](https://developer.apple.com/reference/security/1399291-secrandomcopybytes?language=objc "SecRandomCopyBytes (Objective-C)") is

```objc
int SecRandomCopyBytes(SecRandomRef rnd, size_t count, uint8_t *bytes);
```

The following is an example of the APIs usage:

```objc
int result = SecRandomCopyBytes(kSecRandomDefault, 16, randomBytes);
```

Note: if other mechanisms are used for random numbers in the code, verify that these are either wrappers around the APIs mentioned above or review them for their secure-randomness. Often this is too hard, which means you can best stick with the implementation above.

#### Dynamic Analysis

If you want to test for randomness, you can try to capture a large set of numbers and check with [Burp's sequencer plugin](https://portswigger.net/burp/documentation/desktop/tools/sequencer "Sequencer") to see how good the quality of the randomness is.

### Testing Key Management

#### Overview

There are various methods on how to store the key on the device. Not storing a key at all will ensure that no key material can be dumped. This can be achieved by using a Password Key Derivation function, such as PKBDF-2. See the example below:

```swift

        func pbkdf2SHA1(password: String, salt: Data, keyByteCount: Int, rounds: Int) -> Data? {
        return pbkdf2(hash:CCPBKDFAlgorithm(kCCPRFHmacAlgSHA1), password:password, salt:salt, keyByteCount:keyByteCount, rounds:rounds)
    }

    func pbkdf2SHA256(password: String, salt: Data, keyByteCount: Int, rounds: Int) -> Data? {
        return pbkdf2(hash:CCPBKDFAlgorithm(kCCPRFHmacAlgSHA256), password:password, salt:salt, keyByteCount:keyByteCount, rounds:rounds)
    }

    func pbkdf2SHA512(password: String, salt: Data, keyByteCount: Int, rounds: Int) -> Data? {
        return pbkdf2(hash:CCPBKDFAlgorithm(kCCPRFHmacAlgSHA512), password:password, salt:salt, keyByteCount:keyByteCount, rounds:rounds)
    }

    func pbkdf2(hash :CCPBKDFAlgorithm, password: String, salt: Data, keyByteCount: Int, rounds: Int) -> Data? {
        let passwordData = password.data(using:String.Encoding.utf8)!
        var derivedKeyData = Data(repeating:0, count:keyByteCount)
        let derivedKeyDataLength = derivedKeyData.count
        let derivationStatus = derivedKeyData.withUnsafeMutableBytes {derivedKeyBytes in
            salt.withUnsafeBytes { saltBytes in

                CCKeyDerivationPBKDF(
                    CCPBKDFAlgorithm(kCCPBKDF2),
                    password, passwordData.count,
                    saltBytes, salt.count,
                    hash,
                    UInt32(rounds),
                    derivedKeyBytes, derivedKeyDataLength)
            }
        }
        if (derivationStatus != 0) {
            print("Error: \(derivationStatus)")
            return nil;
        }

        return derivedKeyData
    }

    func testKeyDerivation(){
        //test run in the 'Arcane' librarie its testingsuite to show how you can use it
        let password     = "password"
        //let salt       = "saltData".data(using: String.Encoding.utf8)!
        let salt         = Data(bytes: [0x73, 0x61, 0x6c, 0x74, 0x44, 0x61, 0x74, 0x61])
        let keyByteCount = 16
        let rounds       = 100000

        let derivedKey = pbkdf2SHA1(password:password, salt:salt, keyByteCount:keyByteCount, rounds:rounds)
        print("derivedKey (SHA1): \(derivedKey! as NSData)")
    }
```

 *Source: [https://stackoverflow.com/questions/8569555/pbkdf2-using-commoncrypto-on-ios](https://stackoverflow.com/questions/8569555/pbkdf2-using-commoncrypto-on-ios), tested in the testsuite of the `Arcane` library*

When you need to store the key, it is recommended to use the Keychain as long as the protection class chosen is not `kSecAttrAccessibleAlways`. Storing keys in any other location, such as the `NSUserDefaults`, Propertylists or by any other sink from Coredata or Realm, is usually less secure than using the KeyChain.
Even when the sync of CoreData or Realm is protected by using `NSFileProtectionComplete` data protection class, we still recommend using the KeyChain. See the Testing Data Storage section for more details.

The KeyChain supports two type of storage mechanisms: a key is either secured by an encryption key stored in the secure-enclave or the key itself is within the secure enclave. The latter only holds when you use an ECDH singing key. See the [Apple Documentation](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_in_the_secure_enclave "Secure Enclave") for more details on its implementation.

The last three options are to use hardcoded encryption keys in the source code, having a predictable key derivation function based on stable attributes, and storing generated keys in places that are shared with other applications. Obviously, hardcoded encryption keys are not the way to go. This means every instance of the application uses the same encryption key. An attacker needs only to do the work once, to extract the key from the source code - whether stored natively or in objective-C/Swift. Consequently, he can decrypt any other data that he can obtain which was encrypted by the application.
Next, when you have a predictable key derivation function based on identifiers which are accessible to other applications, the attacker only needs to find the KDF and apply it to the device in order to find the key. Lastly, storing symmetric encryption keys publicly also is highly discouraged.

Two more notions you should never forget when it comes to cryptography:

1. Always encrypt/verify with the public key and always decrypt/sign with the private key.
2. Never reuse the key(pair) for another purpose: this might allow leaking information about the key: have a separate keypair for signing and a separate key(pair) for encryption.

#### Static Analysis

There are various keywords to look for: check the libraries mentioned in the overview and static analysis of the section "Verifying the Configuration of Cryptographic Standard Algorithms" for which keywords you can best check on how keys are stored.
Always make sure that:

- keys are not synchronized over devices if it is used to protect high-risk data.
- keys are not stored without additional protection.
- keys are not hardcoded.
- keys are not derived from stable features of the device.
- keys are not hidden by use of lower level languages (e.g. C/C++).
- keys are not imported from unsafe locations.

Most of the recommendations for static analysis can already be found in chapter "Testing Data Storage for iOS". Next, you can read up on it at the following pages:

- [Apple Developer Documentation: Certificates and keys]( https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys "Certificates and keys")
- [Apple Developer Documentation: Generating new keys](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/generating_new_cryptographic_keys "Generating new keys")
- [Apple Developer Documentation: Key generation attributes](
https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/key_generation_attributes "Key Generation attributes")

#### Dynamic Analysis

Hook cryptographic methods and analyze the keys that are being used. Monitor file system access while cryptographic operations are being performed to assess where key material is written to or read from.

### References

#### General Security Documentation

- Apple Developer Documentation on Security - <https://developer.apple.com/documentation/security>
- Apple Security Guide - <https://www.apple.com/business/site/docs/iOS_Security_Guide.pdf>

#### Configuration of Cryptographic algorithms

- Apple's Cryptographic Services Guide - <https://developer.apple.com/library/content/documentation/Security/Conceptual/cryptoservices/GeneralPurposeCrypto/GeneralPurposeCrypto.html>
- Apple Developer Documentation on randomization SecKey - <https://opensource.apple.com/source/Security/Security-57740.51.3/keychain/SecKey.h.auto.html>
- Apple Documentation on Secure Enclave - <https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_in_the_secure_enclave?language=objc>
- Source code of the header file - <https://opensource.apple.com/source/CommonCrypto/CommonCrypto-36064/CommonCrypto/CommonCryptor.h.auto.html>
- GCM in CommonCrypto - <https://opensource.apple.com/source/CommonCrypto/CommonCrypto-60074/include/CommonCryptorSPI.h>
- Apple Developer Documentation on SecKey - <https://opensource.apple.com/source/Security/Security-57740.51.3/keychain/SecKey.h.auto.html>
- IDZSwiftCommonCrypto - <https://github.com/iosdevzone/IDZSwiftCommonCrypto>
- Heimdall - <https://github.com/henrinormak/Heimdall>
- SwiftyRSA - <https://github.com/TakeScoop/SwiftyRSA>
- SwiftSSL - <https://github.com/SwiftP2P/SwiftSSL>
- RNCryptor - <https://github.com/RNCryptor/RNCryptor>
- Arcane - <https://github.com/onmyway133/Arcane>
- CJOSE - <https://github.com/cisco/cjose>
- CryptoSwift - <https://github.com/krzyzanowskim/CryptoSwift>
- OpenSSL - <https://www.openssl.org/>
- LibSodiums documentation - <https://download.libsodium.org/doc/installation>
- Google on Tink - <https://security.googleblog.com/2018/08/introducing-tink-cryptographic-software.html>
- Themis - <https://github.com/cossacklabs/themis>
- cartfile - <https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile>
- Podfile - <https://guides.cocoapods.org/syntax/podfile.html>

#### Random Number Documentation

- Apple Developer Documentation on randomization - <https://developer.apple.com/documentation/security/randomization_services>
- Apple Developer Documentation on secrandomcopybytes - <https://developer.apple.com/reference/security/1399291-secrandomcopybytes>
- Burp Suite Sequencer  - <https://portswigger.net/burp/documentation/desktop/tools/sequencer>

#### Key Management

- Apple Developer Documentation: Certificates and keys - <https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys>
- Apple Developer Documentation: Generating new keys - <https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/generating_new_cryptographic_keys>
- Apple Developer Documentation: Key generation attributes -
<https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/key_generation_attributes>

#### OWASP Mobile Top 10 2016

- M5 - Insufficient Cryptography - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>

#### OWASP MASVS

- V3.1: "The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption."
- V3.3: "The app uses cryptographic primitives that are appropriate for the particular use case, configured with parameters that adhere to industry best practices."
- V3.4: "The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes."
- V3.5: "The app doesn't re-use the same cryptographic key for multiple purposes."
- V3.6: "All random values are generated using a sufficiently secure random number generator."

#### CWE

- CWE-337 - Predictable Seed in PRNG
- CWE-338 - Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)
