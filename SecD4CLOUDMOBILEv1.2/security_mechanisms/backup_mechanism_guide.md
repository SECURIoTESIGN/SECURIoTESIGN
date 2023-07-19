# Security Backup Mechanisms 

Security Backup Mechanisms for cloud-based mobile apps are procedures to keep data safe and secure in the event of an emergency, such as a computer crash, a user error, or a malicious attack. These mechanisms can include:

• Access Control: Access control restricts the access of certain parts of the application, such as confidential data or the application’s backend, in order to limit the potential damage caused by malicious activities.

• Data Encryption: Data Encryption scrambles application data into an unreadable format, making it impossible to access without the decryption key.

• Password Hashes: Password Hashes are securely stored versions of the users’ passwords to prevent malicious activities such as credentials theft.

• Tokenization: Tokenization is a mechanism that replaces sensitive data with a token to reduce the risk of data theft. 

• Backup System: A backup system can be used to store application data in separate, secure locations. This data can be used to restore the application to its former state in the event of a disruption.

## Backup Mechanisms Examples: 

Security Requirement | Mobile Platform | Mechanism | Description | OSI Layer |
-------------------- | -------------- | --------- | ----------- | --------- |
Backup  | iOS |  iTunes Backup |  Syncs with iTunes for off-site backup | 7 - Application |
Backup  | Android | Google Drive |  Google's cloud solution for data storage and backup | 7 - Application |
Backup  | Android | Third-party cloud solutions | Solutions such as Dropbox, OneDrive and iCloud Drive | 7 - Application |
Backup | All | Local Backup | On-site backups saved on the device's internal storage | 1 - Physical |
Backup | All | External Storage Backup | Off-site backups saved to external devices such as external hard drives and USB drives | 1 - Physical |