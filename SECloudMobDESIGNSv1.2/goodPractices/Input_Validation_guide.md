#  Input Validation 

**Input validation** is performed to ensure only properly formed data is entering the workflow in an information system, preventing malformed data from persisting in the database and triggering malfunction of various downstream components. 

## Implementing input validation	

 * Data type validators available natively in web application frameworks; 
 * Validation against JSON Schema and XML Schema (XSD) for input in these formats; 
 * Type conversion (e.g. Integer.parseInt() in Java, int() in Python) with strict exception handling; 
 * Minimum and maximum value range check for numerical parameters and dates; 
 * Minimum and maximum length check for strings; 
 * Array of allowed values for small sets of string parameters (e.g. days of week); 
 * Regular expressions for any other structured data covering the whole input string (^...$) and not using "any character" wildcard (such as . or \S) 

If it's well structured data, like dates, social security numbers, zip codes, e-mail addresses, etc. then the developer should be able to define a very strong validation pattern, usually based on regular expressions, for validating such input. 
If the input field comes from a fixed set of options, like a drop down list or radio buttons, then the input needs to match exactly one of the values offered to the user in the first place. 
Free-form text, especially with Unicode characters, is perceived as difficult to validate due to a relatively large space of characters that need to be whitelisted. 
The primary means of input validation for free-form text input should be: 

 * Normalization: Ensure canonical encoding is used across all the text and no invalid characters are present; 
 * Character category whitelisting: Unicode allows whitelisting categories such as "decimal digits" or "letters" which  not only covers the Latin alphabet but also various other scripts used globally (e.g. Arabic, Cyryllic, CJK ideographs etc); 
 * Individual character whitelisting: If you allow letters and ideographs in names and also want to allow apostrophe ' for Irish names, but don't want to allow the whole punctuation category. 

## Client Side vs Server Side Validation
		
Be aware that any JavaScript input validation performed on the client can be bypassed by an attacker that disables 
JavaScript or uses a Web Proxy. Ensure that any input validation performed on the client is also performed on the server. 

## Email Validation Basics		

Many web applications do not treat email addresses correctly due to common misconceptions about what constitutes a valid address. Specifically, it is completely valid to have an mailbox address which: 

 * Is case sensitive in the local portion of the address (left of the rightmost @ character); 
 * Has non-alphanumeric characters in the local-part (including + and @); 
 * Has zero or more labels. 

 Following RFC 5321, best practice for validating an email address would be to: 

 * Check for presence of at least one @ symbol in the address;
 * Ensure the local-part is no longer than 64 octets; 
 * Ensure the domain is no longer than 255 octets; 
 * Ensure the address is deliverable.

 [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Input_Validation_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Input_Validation_Cheat_Sheet.md)