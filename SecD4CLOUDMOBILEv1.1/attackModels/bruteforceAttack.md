# Brute Force Attacks
This type of attack consists in trying to access a system using some mechanism or simply 
using trial-and-error, aiming to guess the password of a legitimate user of 
that system. The success of this attack depends largely on the cryptographic scheme used for authentication 
and access control to the system, as well as the nature of the password set by the legitimate user.
## Description
In this attack, some asset, namely, information, functionality, identity, etc., is protected 
by a finite secret value. The attacker attempts to gain access to this asset by using 
trial-and-error to exhaustively explore all the possible secret values in the hope of 
finding the secret (or a value that is functionally equivalent) that will unlock the asset. 
Examples of secrets can include, but are not limited to, passwords, encryption keys, database 
lookup keys, and initial values to one-way functions. The key factor in this attack is the attackers' 
ability to explore the possible secret space rapidly. This, in turn, is a function of the size of the 
secret space and the computational power the attacker is able to bring to bear on the problem. 
If the attacker has modest resources and the secret space is large, the challenge facing the 
attacker is intractable. Assuming a finite secret space, a brute force attack will eventually 
succeed. The defender must rely on making sure that the time and resources necessary to do so will 
exceed the value of the information.

This type of attack can be carried out in two different ways:
1. Encryption Brute Forcing;
2. Password Brute Forcing.

## Technical Impact
* Read Data:
* Gain Privileges.

## Likelihood Of Attack
* Medium

## Typical Severity
* High

## Risk Analysis
* Critical

## Likelihood of Exploit
* High 

## Recommendations
In order to mitigate the Brute Force type attacks it is convenient to follow the good practice guidelines, aiming at incorporating
the security mechanisms during the coding and implementation phase and carrying out the security tests suggested and present in 
the report during the verification phase, with the purpose of ensuring that the functional requirements linked to security and 
the non-functional requirements of the application to be developed or deployed are met.

## References
1. [https://capec.mitre.org/data/definitions/112.html];
2. [https://cwe.mitre.org/data/definitions/521.html]

## Brute Force Attack Tree Diagram
