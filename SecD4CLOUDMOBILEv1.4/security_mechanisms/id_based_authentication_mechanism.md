# ID-based Authentication Mechanisms 

ID-based authentication mechanisms are used to authenticate users in cloud-based mobile applications. This type of authentication typically involves the use of an identifier such as an email address or phone number, as well as a password or some other form of proof of identity. ID-based authentication may also involve the use of biometric markers like fingerprints or facial recognition to verify the user's identity. By using ID-based authentication, mobile applications can ensure that only authorized users are granted access, thereby protecting the data stored and exchanged on the application.

## ID-based Authentication Mechanisms Examples: 

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
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">FaceID</td>
      <td style="border: 1px solid gray; padding: 8px;">User authenticates with their face</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Touch ID</td>
      <td style="border: 1px solid gray; padding: 8px;">User authenticates with their thumbprint</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authorization</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Apple App Tracking Transparency (ATT)</td>
      <td style="border: 1px solid gray; padding: 8px;">Authorizes a user’s usage data to be tracked by a third-party for targeted advertising</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Fingerprint Authenticator</td>
      <td style="border: 1px solid gray; padding: 8px;">User authenticates with their fingerprint</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Face Unlock</td>
      <td style="border: 1px solid gray; padding: 8px;">User authenticates with their face</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authorization</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Google Play Billing Library</td>
      <td style="border: 1px solid gray; padding: 8px;">User authorizes payment for in-app billing</td>
      <td style="border: 1px solid gray; padding: 8px;">Layer 7</td>
    </tr>
  </tbody>
</table>
