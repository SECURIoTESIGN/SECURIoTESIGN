# Testing the SSRF Attack 

**Testing SSRF Attack**

1. Set up an attacker controlled server: This server needs to be able to accept connections from the target server and should log the requests from the target server like the source IP address, used port, timestamp, and any data sent over with the request.

2. Prepare a crafted URL: This URL should lead to the attacker controlled server and is used for the SSRF attack.

3. Send the crafted URL to the target server: This can be done manually by providing the URL as an input for a user or programmatically by sending the URL with a POST request to the target server.

4. Check the logs of the attacker controlled server: After the URL is sent to the target server, the attacker controlled server should log the requests sent by the target server. This is used to analyze the type of requests being sent, the data being sent, and the source IP address.

5. Monitor the environment of the target server: When the target server makes requests to the attacker controlled server, the attacker can set up environment variables, files, resources, etc. in order to exploit the target server.

6. Try to gain access to the target server: If the SSRF attack was successful, the attacker can try to access the target server from the attacker controlled server by using the access gained from the exploited environment of the target server.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform
--- | --- | --- | --- | --- | --- 
Server|White-Box|Dynamic|Input Validation|DSSS - Detection of SSRF|No
Server|Gray-Box|Dynamic|Fuzzing|Burpsuite|No
Server|Black-Box|Dynamic|Vulnerability Scanner|NTOSpider|No
Server|White-Box|Static|Source Code Analysis|Code Editors|No
Server|Gray-Box|Static|Source Code Auditing|Vega|No
Server|Black-Box|Static|Manual Review|Manual Review|No
Server|White-Box|Hybrid|Interactive Testing|Manual Review|No
Server|Gray-Box|Hybrid|Penetration Testing|Metasploit|No
Server|Black-Box|Hybrid|Penetration Testing|Zed Attack Proxy|No
Mobile|White-Box|Dynamic|Input Validation|DSSS - Detection of SSRF|Yes
Mobile|Gray-Box|Dynamic|Fuzzing|Burpsuite|Yes
Mobile|Black-Box|Dynamic|Vulnerability Scanner|NTOSpider|Yes
Mobile|White-Box|Static|Source Code Analysis|Code Editors|Yes
Mobile|Gray-Box|Static|Source Code Auditing|Vega|Yes
Mobile|Black-Box|Static|Manual Review|Manual Review|Yes
Mobile|White-Box|Hybrid|Interactive Testing|Manual Review|Yes
Mobile|Gray-Box|Hybrid|Penetration Testing|Metasploit|Yes
Mobile|Black-Box|Hybrid|Penetration Testing|Burp Suite|Yes