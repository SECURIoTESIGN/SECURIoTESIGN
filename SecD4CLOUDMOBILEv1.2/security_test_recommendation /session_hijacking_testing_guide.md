# Testing the Session Hijacking Attack 

Testing Session Hijacking attack requires two machines connected to the same network. The attacker would need to intercept the network traffic from the victim's machine where the session data is being exchanged. It is also important to note that it is possible to hijack cookies from other machines on the same network.

Here are the steps to test a Session Hijacking attack:

1. Install a network sniffing tool (such as Wireshark) on both machines to monitor network traffic.

2. Use the sniffing tool to identify any cookies used in the session interaction between the two machines. Note that certain browsers may encrypt the cookie data so the cookie might appear to be encrypted.

3. Intercept the cookie data on the attacker’s machine - the attacker should now have temporary access to the session data.

4. Use the sniffing tool to analyze the data transferred between the two machines and confirm if the session data has been compromised.

5. Try to login to the victim’s session with the stolen credentials or cookies.

6. If successful, the attacker has hijacked the session and should be able to access the victim’s session data. 

7. Log out of the session on the attacker's machine and remove all evidence of the session hijacking attack.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform
--- | --- | --- | --- | --- | ---
Session Hijacking Attack | White-box | Dynamic | Code review | Burp Suite | N/A
Session Hijacking Attack | Grey-box | Static | Vulnerability assessment | Nessus | N/A
Session Hijacking Attack | Black-box | Hybrid | Penetration testing | Nmap | N/A