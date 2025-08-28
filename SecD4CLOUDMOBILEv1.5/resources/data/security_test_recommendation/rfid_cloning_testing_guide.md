# Testing the RFID Cloning Attack 

Testing RFID cloning involves using an RFID reader to scan different identification tags to determine if there are any discrepancies. 

To test RFID cloning: 

1. Place the two RFID tags or cards to be tested in front of the reader. 

2. Scan each tag individually using the RFID reader. 

3. Compare the response data from each scan to determine if the tags match or if there is any variation. If the tags match, then the RFID cloning is successful. 

4. If the scans produce different results, then the cloning attempt has failed and further investigation is needed to determine the cause. 

5. After the results have been examined, reset the reader and repeat the tests with the next RFID tag. 

By performing this process, it is possible to correctly identify any discrepancies in an RFID clone attempt.

## Testing Tools: 

| Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform |
|:-------------:|:----------------:|:------------:|:----------:|:---------:|:--------------:|
| Design        | White-box       | Static       | Manual     | N/A       | N/A            |
| Code          | White-box       | Static       | Manual     | N/A       | N/A            |
| Implementation| White-Box       | Dynamic      | Automated  | FuzzyByte  | Android        |
| Design        | Grey-box        | Static       | Manual     | N/A       | N/A            |
| Code          | Grey-box        | Static       | Manual     | N/A       | N/A            |
| Implementation| Grey-Box        | Dynamic      | Automated  | Peach      | iOS            |
| Design        | Black-box       | Static       | Manual     | N/A       | N/A            |
| Code          | Black-box       | Static       | Manual     | N/A       | N/A            |
| Implementation| Black-Box       | Hybrid       | Automated  | Metasploit | Android        |