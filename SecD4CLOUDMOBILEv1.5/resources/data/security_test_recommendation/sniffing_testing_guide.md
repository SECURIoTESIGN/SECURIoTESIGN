# Testing the Sniffing Attack 

To detect sniffing attacks, the following steps should be followed:

1. Monitor Network Activity:  Monitor your network for unusually high levels of traffic, and compare it to what is normal. High amounts of traffic can indicate malicious activity.

2. Perform Packet Capture: Use packet capture techniques such as port mirroring or port spanning to monitor all the packets that travel between two locations or over a network. This will allow you to analyze the data in detail and detect any malicious activity.

3. Track Source IP Addresses: Track the source IP addresses of incoming packets to determine any suspicious activity. Malicious IPs can be blocked and monitored later.

4. Compare Protocols: Compare the protocols used in the captured network traffic. If any unusual or unfamiliar protocols are used, the traffic should be investigated further.

5. Utilize Intrusion Detection Systems (IDS): Utilize Intrusion Detection Systems (IDS) to detect any anomalies in the network traffic. IDS systems analyze packets in real-time and look for any suspicious activity.

6. Use Network Scanning Tools: Utilize tools such as Nmap to identify open ports, services and vulnerabilities that need to be patched.

7. Use Antivirus Software: Use antivirus software to detect and prevent malicious activity. Antivirus software should be updated regularly for maximum protection.

8. Implement Encryption: Encrypt data before sending it over a network. This will prevent malicious actors from decrypting and accessing confidential data.

## Testing Tools: 

| Target Testing | Testing Technique | Test Analysis   | Test Method    | Test Tool          | Mobile Platform |
| ------------- | ---------------- | -------------- | -------------- |------------------ | ----------------|
| Network       | White-box        | Dynamic        | Network Sniffer| Wireshark/Ethereal | None            |
| Network       | Grey-box         | Dynamic        | Network & Host | Nmap              | None            |
| Network       | Grey-box         | Dynamic        | Protocol Tests | Ncat              | None            |
| Host          | White-box        | Static         | File Scanning  | NESSUS            | None            |
| Host          | Grey-box         | Hybrid         | Application    | Burp Suite        | iOS/Android     |	  
| Application   | Black-box        | Dynamic        | Code Analysis  | FindBugs          | iOS/Android     |