## General Architecture Requirements 

Regardless of the metric device architecture chosen, the lower requirements are valid:

 * All app components are identified and known to be needed;

 * Security controls are never enforced only on the client side, but on the respective endpoints;

 + A high-level architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture;

 * Data considered sensitive context of the mobile app is clearly identified;

 * All app components are defined in terms of the business functions and/or security functions they provide;
 * A threat model for the mobile app and the associated remote services has been produced that identified threats and countermeasures;

 * All security controls have a centralized implementation;

 * There is an explicit policy for how cryptographic keys are managed, and the lifecycle of cryptography keys is enforced;

 * Security is addressed within all parts of the software development lifecycle.
