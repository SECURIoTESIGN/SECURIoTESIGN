# Security Best Practices Guidelines for Input Validation 

## Input Validation Security Best Practices

1. **Whitelisting:** Use whitelisting to ensure only known reliable data enters the system.
2. **Data Minimization:** When possible, minimize the amount of user supplied input data.
3. **Data Size Limitation:** Restrict input data to a reasonable length.
4. **Data Type Limitation:** Restrict input data to expected types and formats.
5. **Input Data Sanitization:**Sanitize input data to strip out malicious content (e.g. tags, scripts).
6. **Input Data Encoding:**Encode input data (e.g. HTML encoding) to prevent attackers from exploiting a known vulnerability.
7. **Verify Server Side:** Perform checks and validation on the server side for all user supplied data.
8. **Data Format Validation:** Validate any input data is in the required format.
9. **Reduce False Positives:** Try to reduce any false positives that impede users from submitting their input data (e.g. CAPTCHAs).
10. **Logging and Monitoring:** Monitor suspicious or malicious activity (e.g. failed logins attempts) around user input.