# SQL Injection Attacks

In this type of attack, an attacker could provide malicious input with a clever mix of characters and meta characters from a form (e.g., login form) to alter the logic of the SQL command.


## Definition

Structured Query Language (SQL) Injection Attack is a code injection technique commonly used to attack web applications where an attacker enters SQL characters or keywords into an SQL statement through superuser input parameters for the purpose to change the logic of the desired query.

## Technical Impact
 * Read Application Data;
 * Bypass Protection Mechanism;
 * Modify Application Data.

## Likelihood of Exploit

High.

## Risk

Critical Risk.

## Attacker's Powers
 * Identify parameters vulnerable to injection;
 * Discover DBMS and version;
 * Discover relational scheme;
 * Extract data;
 * Add/modify data;
 * Cause denial of service;
 * Evade detection;
 * Bypass authentication;
 * Execute commands;
 * Elevate privileges.

## Recommendations

To ensure that the mobile application is resilient or immune to SQLi attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed to ensure authenticity, confidentiality, access control, integrity, privacy and authenticity of the data.

## Reference
 1. [https://cwe.mitre.org/data/definitions/89.html]
 
## SQL Injection Attacks Diagram


