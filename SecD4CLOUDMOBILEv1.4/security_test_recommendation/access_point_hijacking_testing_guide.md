# Testing the Access Point Hijacking Attack 

1. **Reconnaissance:** Utilize network reconnaissance techniques to identify wireless access points within range. These can include passive approaches such as wireless network scanning with a tool like [Kismet](https://www.kismetwireless.net/), or active approaches such as using a tool like [Aircrack-ng](https://www.aircrack-ng.org/).

2. **Enumeration:** Connect to a legitimate access point on the network and run a tool like [NetStumbler](http://www.netstumbler.com/) to enumerate the target.

3. **Exploitation:** Attempt to perform an access point hijacking attack by using a tool like [AirJack](https://github.com/airjack-ng/airjack). AirJack will capture valid authentication packets and can be used to take control of the target access point.

4. **Verification:** Verify the success of the attack by ensuring that the access point is controlled by the attacking machine. This can be done by pinging the IP address of the access point or using a tool like [MDK3](https://github.com/WiFi-Pumpkin/MDK3-master) to verify that the access point is now under the control of the attacker.

5. **Mitigation:** Implement security measures to prevent and detect access point hijacking attacks. These can include monitoring network traffic for suspicious activity, disabling SSID broadcast, enabling WPA2 encryption, implementing MAC address filtering and implementing a whitelisting protocol.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform 
--- | --- | --- | --- | --- | --- 
Access Point Hijacking Attack | White-box | Dynamic | Packet Sniffing | Wireshark | Android / iOS
Access Point Hijacking Attack | Gray-box | Static | Code Review | static code analysis tool | Android / iOS
Access Point Hijacking Attack | Black-box | Hybrid | Penetration Testing | Burp Suite | Android / iOS