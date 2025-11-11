# Security Backup Mechanisms 

Security Backup Mechanisms for cloud-based mobile apps are procedures to keep data safe and secure in the event of an emergency, such as a computer crash, a user error, or a malicious attack. These mechanisms can include:

• Access Control: Access control restricts the access of certain parts of the application, such as confidential data or the application’s backend, in order to limit the potential damage caused by malicious activities.

• Data Encryption: Data Encryption scrambles application data into an unreadable format, making it impossible to access without the decryption key.

• Password Hashes: Password Hashes are securely stored versions of the users’ passwords to prevent malicious activities such as credentials theft.

• Tokenization: Tokenization is a mechanism that replaces sensitive data with a token to reduce the risk of data theft. 

• Backup System: A backup system can be used to store application data in separate, secure locations. This data can be used to restore the application to its former state in the event of a disruption.

## Backup Mechanisms Examples: 


<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="border: 1px solid gray; padding: 8px;">Security Requirement</th>
      <th style="border: 1px solid gray; padding: 8px;">Mobile Platform</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism</th>
      <th style="border: 1px solid gray; padding: 8px;">Description</th>
      <th style="border: 1px solid gray; padding: 8px;">OSI Layer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">iTunes Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">Syncs with iTunes for off-site backup</td>
      <td style="border: 1px solid gray; padding: 8px;">7 - Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Google Drive</td>
      <td style="border: 1px solid gray; padding: 8px;">Google's cloud solution for data storage and backup</td>
      <td style="border: 1px solid gray; padding: 8px;">7 - Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Third-party cloud solutions</td>
      <td style="border: 1px solid gray; padding: 8px;">Solutions such as Dropbox, OneDrive and iCloud Drive</td>
      <td style="border: 1px solid gray; padding: 8px;">7 - Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">All</td>
      <td style="border: 1px solid gray; padding: 8px;">Local Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">On-site backups saved on the device's internal storage</td>
      <td style="border: 1px solid gray; padding: 8px;">1 - Physical</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">All</td>
      <td style="border: 1px solid gray; padding: 8px;">External Storage Backup</td>
      <td style="border: 1px solid gray; padding: 8px;">Off-site backups saved to external devices such as external hard drives and USB drives</td>
      <td style="border: 1px solid gray; padding: 8px;">1 - Physical</td>
    </tr>
  </tbody>
</table>
