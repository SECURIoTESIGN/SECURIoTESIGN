# Testing the Side-Channel Attack 

1. First, you should define the types of side-channels you would like to test. Examples of side-channels might include power, electromagnetic, timing, acoustic, and leakage. 

2. Then, you should decide which data gathering tools you will use to record the information associated with each side-channel. Depending on your environment, these tools can vary from devices such as oscilloscopes to software programs such as spectral analyzers or logic analyzers.

3. Once you have determined the tools needed, you should set up the environment in which your tests will occur. Make sure to carefully plan the physical location of each component, such as the device being tested and the monitoring equipment, to ensure accurate measurements. 

4. Once the environment is set, you should begin recording data. Output from the side-channel should be captured in an organized manner, such as separating the data into multiple files or creating a log.

5. Lastly, the data should be analyzed to identify any potential issues. This can be done by using various analysis techniques, such as manually examining the data or using statistical algorithms. This analysis should then be reported in a format that is easy to interpret, such as tables or graphs.

## Testing Tools: 

| Target Testing         | Testing Technique | Test Analysis | Test Method  | Test Tool | Mobile Plataform | 
  | --------------------- | ---------------- | ------------ | ----------- | ----------| --------------- |
  | White-Box            | Dynamic          | System Call  | Penetration | Kali      | Android          |
  |                      |                  |              | Testing     | Nmap      | iOS              |
  | Grey-Box             | Static           | Dynamic Trace| Regression  | HPFortify |                 |
  |                      |                  |              | Testing     | Metasploit|                 |
  | Black-Box            | Hybrid           | Security Scan|Fuzz-testing | Coreaudit |                 |