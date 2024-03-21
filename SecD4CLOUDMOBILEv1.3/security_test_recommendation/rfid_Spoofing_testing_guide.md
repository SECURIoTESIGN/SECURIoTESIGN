# Testing the RFID Spoofing Attack 

**Testing RFID Spoofing Attacks:**

1. In order to test potential RFID spoofing attacks, a special device called an RFID emulator or cloner is needed. 
2. An RFID emulator is a device that behaves and responds to an authentic RFID card or tag in the same way that a genuine RFID tag would.
3. It is used to simulate and inject messages into a system to see how it responds. 
4. The RFID emulator is designed to intercept and analyze the communication between an RFID reader and a tag or card. 
5. The emulator then transmits a fake tag response, which is then seen by the reader as a legitimate tag. 
6. By running this test, you can detect and prevent any spoofing attacks. 
7. If the RFID reader responds as expected, then you have successfully identified any potential RFID spoofing attack.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Plataform
--- | --- | --- | --- | --- | --- 
RFID | White-box | Dynamic | Penetration Testing | Nessus | iOS
RFID | Grey-box | Static | Fuzz Testing | OWASP Zap | Android
RFID | Black-box | Hybrid | Security Analysis | Metasploit | iOS/Android