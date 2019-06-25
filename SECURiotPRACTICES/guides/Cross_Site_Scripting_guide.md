##  Cross Site Scripting (XSS)

Given the way browsers parse HTML, each of the different types of slots has slightly different security rules. 
When you put untrusted data into these slots, you need to take certain steps to make sure that the data does not break out of that slot into a context that allows code execution. 

HTML entity encoding is okay for untrusted data that you put in the body of the HTML document, such as inside a "div" tag. It even sort of works for untrusted data that goes into attributes, particularly if you're religious about using quotes around your attributes. But HTML entity encoding  doesn't work if you're putting untrusted data inside a "script" tag anywhere, or an event handler attribute  like onmouseover, or inside CSS, or in a URL. 

**XSS Prevention Rules**	

 * Never Insert Untrusted Data Except in Allowed Locations - The first rule is to deny all 
 * HTML Escape Before Inserting Untrusted Data into HTML Element Content 
 * Attribute Escape Before Inserting Untrusted Data into HTML Common Attributes 
 * JavaScript Escape Before Inserting Untrusted Data into JavaScript Data Values 
 * HTML escape JSON values in an HTML context and read the data with JSON.parse 
 * Ensure returned Content-Type header is application/json and not text/html.  
 * CSS Escape And Strictly Validate Before Inserting Untrusted Data into HTML Style Property Values
 * URL Escape Before Inserting Untrusted Data into HTML URL Parameter Values 
 * Sanitize HTML Markup with a Library Designed for the Job 
 * Prevent DOM-based XSS 
 * Use HTTPOnly cookie flag 
 * Implement Content Security Policy 
 * Use an Auto-Escaping Template System 
 * Use the X-XSS-Protection Response Header 
 * Properly use modern JS frameworks like Angular (2+) or ReactJS

[https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md)