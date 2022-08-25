# Authentication

**Authentication** is the process of verifying that an individual, entity or website is whom it claims to be. Authentication in the context of web applications is commonly performed by submitting a username or ID and one or more items of private information that only a given user should know.

## Authentication General Guidelines

### User IDs

  * Make sure your usernames/user IDs are case-insensitive (e.g. User 'smith' and user 'Smith' should be the same user); 
  * Usernames should also be unique; 
  * For high-security applications, usernames could be assigned and secret instead of user-defined public data.

### Authentication Solution and Sensitive Accounts

- Do **NOT** allow login with sensitive accounts (i.e. accounts that can be used internally within the solution such as to a back-end / middle-ware / DB) to any front-end user-interface
- Do **NOT** use the same authentication solution (e.g. IDP / AD) used internally for unsecured access (e.g. public access / DMZ)

### Implement Proper Password Strength Controls

- Password Length
    * Minimum password length (10 characters) should be enforced;
    * Maximum password length should not be too short because it will prevent users from creating passphrases; 
    * The typical maximum length is 128 characters.
- Do not silently truncate passwords.
- Allow usage of **all** characters including unicode and whitespace.
- Ensure credential rotation when a password leak occurs, or at the time of compromise identification.
- Include password strength meter to help users create a more complex password and block common and previously breached passwords
    - [zxcvbn-ts library](https://github.com/zxcvbn-ts/zxcvbn) can be used for this purpose;
    - [Pwned Passwords](https://haveibeenpwned.com/Passwords) is a service where passwords can be checked against previously breached passwords. You can host it yourself or use the [API](https://haveibeenpwned.com/API/v3#PwnedPasswords).


### Implement Secure Password Recovery Mechanism

 * Please check [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) for details on this feature.

### Store Passwords in a Secure Fashion

 * Please see [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) for details on this feature.

### Compare Password Hashes Using Safe Functions

- Using a secure password comparison function provided by the language or framework, such as the [password_verify()](https://www.php.net/manual/en/function.password-verify.php) function in PHP. 

- Where this is not possible, ensure that the comparison function:

 - Has a maximum input length, to protect against denial of service attacks with very long inputs.
 - Explicitly sets the type of both variable, to protect against type confusion attacks such as [Magic Hashes](https://www.whitehatsec.com/blog/magic-hashes/) in PHP.
 - Returns in constant time, to protect against timing attacks.

### Change Password Feature

When developing change password feature, ensure to have:

- User is authenticated with active session.
- Current password verification.

### Transmit Passwords Only Over TLSv1.3 or Other Strong Transport

Check: [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)

### Require Re-authentication for Sensitive Features

Require the current credentials for an account before updating sensitive account information such as the user's password, user's email, or before sensitive transactions, such as shipping a purchase to a new address to avoid CSRF or XSS;

### Consider Strong Transaction Authentication

The application must use a second authentication factor in financial transactions.

#### TLS Client Authentication

It is a good idea to do this when:

- It is acceptable (or even preferred) that the user only has access to the website from only a single computer/browser;
- The user is not easily scared by the process of installing TLS certificates on his browser, or there will be someone, probably from IT support, that will do this for the user;
- The website requires an extra step of security;
- It is also a good thing to use when the website is for an intranet of a company or organization.

It is generally not a good idea to use this method for widely and publicly available websites that will have an average user (e.g. Facebook)

### Authentication and Error Messages

 * Incorrectly implemented error messages in the case of authentication functionality can be used for the purposes of user ID and password enumeration. 
 * An application should respond (both HTTP and HTML) in a generic manner.

#### Authentication Responses

Using any of the authentication mechanisms (login, password reset or password recovery), an application must respond with a generic error message regardless of whether:

- The user ID or password was incorrect.
- The account does not exist.
- The account is locked or disabled.

##### Incorrect and correct response examples

###### Login

Incorrect response examples:

- "Login for User foo: invalid password."
- "Login failed, invalid user ID."
- "Login failed; account disabled."
- "Login failed; this user is not active."

Correct response example:

- "Login failed; Invalid user ID or password."

###### Password recovery

Incorrect response examples:

- "We just sent you a password reset link."
- "This email address doesn't exist in our database."

Correct response example:

- "If that email address is in our database, we will send you an email to reset your password."

###### Account creation

Incorrect response examples:

- "This user ID is already in use."
- "Welcome! You have signed up successfully."

Correct response example:

- "A link to activate your account has been emailed to the address provided."

### Protect Against Automated Attacks

Countermeasures against automated attacks on authentication stand out: 

 * Multi-Factor Authentication (MFA);
 * Account Lockout;
 * CAPTCHA;
 * Security Questions and Memorable Words.

## Logging and Monitoring

Enable logging and monitoring of authentication functions to detect attacks/failures on a real-time basis

- Ensure that all failures are logged and reviewed;
- Ensure that all password failures are logged and reviewed;
- Ensure that all account lockouts are logged and reviewed.

## Use of authentication protocols that require no password

 1. OAuth
  * Implement OAuth 1.0a or OAuth 2.0 since the very first version (OAuth1.0) has been found to be vulnerable to session. fixation.

 2. OpenId;
 3. SAML
  * Implement version 2.0 since it is very feature-complete and provides strong security. 
 4. FIDO.

## Password Managers

Web applications should not make password managers' job more difficult than necessary by observing the following recommendations:

- Use standard HTML forms for username and password input with appropriate `type` attributes.
    - Avoid plugin-based login pages (such as Flash or Silverlight).
- Implement a reasonable maximum password length, such as 64 characters, as discussed in the [Password Storage Cheat Sheet](Password_Storage_Cheat_Sheet.md#maximum-password-lengths).
- Allow any printable characters to be used in passwords.
- Allow users to paste into the username and password fields.
- Allow users to navigate between the username and password field with a single press of the `Tab` key.


## References
1. [Authentication Cheat Sheet] (https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
