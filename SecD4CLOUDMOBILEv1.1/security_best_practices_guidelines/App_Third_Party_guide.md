# Third-Party Applications 

Many social networks also offer the possibility to create additional applications that extend the functionality of the network. The two major platforms for such applications are the Facebook Platform and Open Social. While applications designed for the Facebook Platform can only be executed in Facebook, Open Social is a combined effort to allow developers to run their applications on any social network that supports the Open Social platform (e.g., MySpace and Orkut).


## Requirements for a secure third-party applications

 * Secure Computation: No external entity should be able to observe or interfere with the computation performed by trustworthy remote entity (TRE). Since the adversary has physical access to the platform, the confidentiality and integrity must be protected from untrusted sofware on the same platform;
 * Secure Communication: Communication between the TRE and other parties must be confidential and integrity-prtected;
 * Strong Attestation: The root of trust used for attestation must be trusted by all parties. The attestation mus be unambiguously linked to the communicating entity (authenticity) to avoid masquerading attacks, and must concey the current state of the system (freshness) to prevent replay attacks.


Apps that process or query sensitive information should run in a trusted and secure environment. To create this environment, the app can check the device for the following:

 * PIN - or password-protected device locking;
 * Recent Mobile Plataform or OS version;
 * USB Debugging activation;
 * Device encryption;
 * Device rooting (see also "Testing Root Detection").


