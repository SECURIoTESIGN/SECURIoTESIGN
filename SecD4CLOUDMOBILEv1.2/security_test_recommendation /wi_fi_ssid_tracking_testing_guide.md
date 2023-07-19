# Testing the Wi-Fi Jamming Attack 

1. Establish your test environment:
   - Create secure wireless network with a unique SSID.
   - Setup network tracking or logging capabilities to collect and analyze information.
   - Set different levels of access for different users and/or roles.

2. Deploy your wireless network and begin tracking traffic:
   - Provide access to all authorized users and install appropriate security protocols to protect the network from unauthorized access.
   - Monitor the network and log all wireless traffic, noting the SSIDs of all access points seen by the network.

3. Use an attacker tool to test your security and detect potential SSID Tracking attacks:
   - Utilize an attack tool like [Aircrack-ng](https://www.aircrack-ng.org/) to simulate an attacker attempting to connect to the wireless network. 
   - Use the attack tool to flood the network with SSID requests, and analyze the logs to see if any of them contain the unique SSID of the network.

4. Analyze results and adjust security accordingly:
   - If the SSID appears in the logs, the attack was successful and your security isn't sufficient to prevent tracking.
   - Adjust network security measures to ensure that unauthorized users cannot access the network and its resources.

## Testing Tools: 

| Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform |
| ------------- | ---------------- | ------------ | ---------- | -------- | --------------- |
| Wi-Fi SSID Tracking | White-box | Dynamic | Boundary Analysis | Qualys Network Inspector | iOS, Android, Windows | 
| Wi-Fi SSID Tracking | Grey-box | Static | Source Code Analysis | Veracode | Android, Windows |
| Wi-Fi SSID Tracking | Black-box | Hybrid | Penetration Testing | Burp Suite | iOS, Android, Windows |