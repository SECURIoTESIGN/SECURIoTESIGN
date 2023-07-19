# Testing the Command Injection Attack 

1. **Testing for Command Injection**

Command Injection is an attack in which malicious commands are injected into a vulnerable application in order to gain access or obtain privileged information. This type of attack involves taking user input and executing it as code on the system, making it highly dangerous and difficult to detect.

In order to test for command injection, it is important to first identify any areas of the application that may be vulnerable to attack. Applications which take user input and execute it as code are particularly at risk.

Once potential vulnerable areas have been identified, test cases can be created to simulate attempts at injecting malicious code. This can be done by attempting to insert special characters or meta-characters into input fields, such as semi-colons, backticks, or quotation marks. If the application responds in an unexpected manner or creates an externally visible result, such as creating an extra file in the directory, it is likely that command injection is possible.

It is important to note that command injection may not always be easy to spot, as the application may attempt to sanitize user input or where malicious code can be 'hidden' within benign input. As such, testing using all potential input combinations is recommended in order to ensure that vulnerabilities have been adequately identified and addressed.

Once all potential vulnerabilities have been assessed and remediated, it is recommended to repeat the testing process in order to validate the changes.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform 
--- | --- | --- | --- | --- | ---
Command Injection Attack | White-box | Dynamic | Input Fuzzing | Metasploit | iOS/Android
Command Injection Attack | Grey-box | Static | Variant Analysis | CodeSonar | iOS/Android 
Command Injection Attack | Black-box | Hybrid | Interactive Fuzzing | Burp | iOS/Android