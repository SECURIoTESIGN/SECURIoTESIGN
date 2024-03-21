# Session Hijacking Attack 

Session Hijacking is a type of cyber attack in which an attacker takes control of a user's active session by taking control of the session ID. It is also known as session riding or SideJacking. 

An attacker can hijack a session by stealing the session ID and using it to create a new session. 

This attack can be used to access the user's account and data. It can be used to impersonate the user, perform malicious activities under their name, and gain access to other resources.

To protect against session hijacking, it is important to use strong authentication methods, establish secure network connections, and use session timeouts. Additionally, web applications can use encryption, secure cookies, and server-side session management.

## Session Hijacking Architectural Risk Analysis: 

| Component | Attack Vector | Attack Complexity | Privileges Required | User Interaction   | Scope | Confidentiality (C) | Integrity (I) | Availability (A) |
|-----------|---------------|------------------|--------------------|--------------------|-------|------------------|--------------|-----------------|
| Session Hijacking | Network (N) | Low (L) | None (N) | None (N) | Changed (C) | High (H) | Low (L) | Low (L) |

**CVSS Score:** 8.2 (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:L)

**Impact:** High

## Session Hijacking Attack 