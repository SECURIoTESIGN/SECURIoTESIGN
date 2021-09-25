# Logging and Error Handling 

## Purpose of logging

Application logging should be always be included for security events. Application logs are invaluable data for:

* Identifying security incidents;	
* Monitoring policy violations;	
* Establishing baselines;	
* Assisting non-repudiation controls;	
* Providing information about problems and unusual conditions;	
* Contributing additional application-specific data for incident investigation which is lacking in other log sources;	
* Helping defend against vulnerability identification and exploitation through attack detection.	

Each log entry needs to include sufficient information for the intended subsequent monitoring and analysis. It could be full content data, but is more likely to be an extract or just summary properties.

The application logs must record "when, where, who and what" for each event.



## Where to record event data

* When using the file system, it is preferable to use a separate partition than those used by the operating system, other application files and user generated content:
 * For file-based logs, apply strict permissions concerning which users can access the directories, and the permissions of files within the directories;
 * In web applications, the logs should not be exposed in web-accessible locations, and if done so, should have restricted access and be configured with a plain text MIME type (not HTML).
* When using a database, it is preferable to utilize a separate database account that is only used for writing log data and which has very restrictive database , table, function and command permissions;
* Use standard formats over secure protocols to record and send event data, or log files, to other systems e.g. Common Log File System (CLFS) or Common Event Format (CEF) over syslog; standard formats facilitate integration with centralised logging services.


## Which events to log

* Input validation failures e.g. protocol violations, unacceptable encodings, invalid parameter names and values;
* Output validation failures e.g. database record set mismatch, invalid data encoding
* Authentication successes and failures;
* Authorization (access control) failures;
* Session management failures e.g. cookie session identification value modification
* Application errors and system events e.g. syntax and runtime errors, connectivity problems, performance issues, third party service error messages, file system errors, file upload virus detection, configuration changes;
* Application and related systems start-ups and shut-downs, and logging initialization (starting, stopping or pausing);
* Use of higher-risk functionality e.g. network connections, addition or deletion of users, changes to privileges, assigning users to tokens, adding or deleting tokens, use of systems administrative privileges, access by application administrators, all actions by users with administrative privileges, access to payment cardholder data, use of data encrypting keys, key changes, creation and deletion of system-level objects, data import and export including screen-based reports, submission of user-generated content - especially file uploads.


## Data to exclude

* Application source code;
* Session identification values (consider replacing with a hashed value if needed to track session specific events);
* Access tokens;
* Sensitive personal data and some forms of personally identifiable information (PII) e.g. health, government identifiers, vulnerable people;
* Authentication passwords;
* Database connection strings;
* Encryption keys and other master secrets;
* Bank account or payment card holder data;
* Data of a higher security classification than the logging system is allowed to store;
* Commercially-sensitive information;
* Information it is illegal to collect in the relevant jurisdictions;
* Information a user has opted out of collection, or not consented to e.g. use of do not track, or where consent to collect has expired.


## Error Handling

### User Facing Error Messages
	
Error messages displayed to the user should not contain system, diagnostic or debug information.


### Formatting Error Messages

Error messages are often logged to text files or files viewed within a web browser.

* Text based log files: Ensure any newline characters (%0A%0C) are appropriately handled to prevent log forging;
* Web based log files: Ensure any logged html characters are appropriately encoded to prevent XSS when viewing logs.

## Recommended Error Handling Design

* Log necessary error data to a system log file;
* Display a generic error message to the user;
* If necessary provide an error code to the user which maps to the error data in the log file. A user reporting an error can provide this code to help diagnose issue.



[https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Logging_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Logging_Cheat_Sheet.md)