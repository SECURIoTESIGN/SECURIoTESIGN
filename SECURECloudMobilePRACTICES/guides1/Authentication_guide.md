## Authentication

**Authentication** is the process of verification that an individual, entity or website is who it claims to be. Authentication in the context of mobile applications is commonly performed by submitting a user name or ID and one or more items of private information that only a given user should know. 

**User ID's**		
Make sure your usernames/userids are case insensitive.	
User 'smith' and user 'Smith' should be the same user.	
User names should also be unique. For high security applications usernames could be assigned and secret instead of user-defined public data.	
Email address as a USER ID.	

**Password Length**		
Minimum password length (10 characters) should be enforced.
Maximum password length should not be too short because it will prevent users from creating passphrases. 
The typical maximum length is 128 characters.


**Password Complexity**		
Applications should enforce password complexity rules to discourage easy to guess passwords.	
Password mechanisms should allow virtually any character the user can type to be part of their password, including the space character. Passwords should, obviously, be case sensitive in order to increase their complexity.	

The password change mechanism should require a minimum level of complexity that makes sense for the application and its user population.	

 Password must meet at least 3 out of the following 4 complexity rules:	
  * At least 1 uppercase character (A-Z) 
  * At least 1 lowercase character (a-z) 
  * At least 1 digit (0-9) 
  * At least 1 special character (punctuation) space included 
  * At least 10 characters 
  * At most 128 characters 
  * Not more than 2 identical characters in a row (e.g. 111 not allowed) 

**Require Re-authentication for Sensitive Features**	
In order to mitigate CSRF and session hijacking, it's important to require the current credentials for an account before updating sensitive account information such as the user's password, user's email, or before sensitive transactions, such as shipping a purchase to a new address. 

**Authentication and Error Messages**	
 * Incorrectly implemented error messages in the case of authentication functionality can be used for the purposes of user ID and password enumeration. An application should respond (both HTTP and HTML) in a generic manner. 
 * An application should respond with a generic error message regardless of whether the user ID or password was incorrect. It should also give no indication to the status of an existing account.

**Session Management Best Practices**
 * Session IDs are randomly generated on the server side.
 * The IDs can't be guessed easily (use proper length and entropy).
 * Session IDs are always exchanged over secure connections (e.g. HTTPS).
 * The mobile app doesn't save session IDs in permanent storage.
 * The server verifies the session whenever a user tries to access privileged application elements, (a session ID must be valid and must correspond to the proper authorization level).
 * The session is terminated on the server side and deleted within the mobile app after it times out or the user logs out.

Incorrect Response Examples : 

 * Login for User foo: invalid password 
 * Login failed, invalid user ID 
 * Login failed; account disabled 
 * Login failed; this user is not active 

Correct Response Example : 

  * Login failed; Invalid userID or password


[https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authentication_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authentication_Cheat_Sheet.md)
