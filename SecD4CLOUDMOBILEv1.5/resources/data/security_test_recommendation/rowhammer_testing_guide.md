# Testing Rowhammer Attack 

1. Choose a system with vulnerable DRAM modules: 
    - It is important to have a system with vulnerable DRAM modules to test for Rowhammer. 
2. Set up stressor application (e.g. memtest86+):
    - To test for Rowhammer, a stressor application is needed. A popular one, often used for this type of testing, is memtest86+.  
3. Run the stressor application repeatedly for a longer period of time:
    - The stressor application should be run repeatedly for a longer period of time, usually several hours. 
4. Monitor system response:
    - During the test, the system should be monitored to check for any errors or abnormalities. 
5. Analyze results: 
    - Once the testing period is over, the results should be analyzed for any evidence of Rowhammer attacks.

## Testing Tools: 

Target Testing  | Testing Technique | Test Analysis  | Test Method  | Test Tool  | Mobile Platform
----------------|------------------|---------------|-------------|-----------|----------------
Hardware       | White-box        | Dynamic       | Hardware-in-the-Loop   |Babblar   | Android
Software       | Grey-box         | Static        | Fuzz Testing           |Windmill  | iOS
Firmware       | Black-box        | Hybrid        | Dynamic Web Testing    |Syhunt    |
Application    |                  |               | Penetration Testing    | Metasploit |