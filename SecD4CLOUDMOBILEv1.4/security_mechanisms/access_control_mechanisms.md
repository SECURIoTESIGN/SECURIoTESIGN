# Access Control Mechanisms 

Security Access Control Mechanisms (SACMs) are the technical and administrative strategies and tools used to protect cloud-based mobile apps from unauthorized access to confidential data and systems. These mechanisms are designed to restrict access to certain users, manage user privileges, authenticate user accounts, and authorize access requests. Examples of SACMs include multi-factor authentication (MFA), biometric authentication, single-sign-on (SSO), role-based access control (RBAC), application-level encryption, and least privilege access. SACMs allow organizations to properly control who has access to what resources and strictly enforce principles of confidentiality, privacy, and data security.

## Access Control Mechanisms Examples: 

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
      <td style="border: 1px solid gray; padding: 8px;">Data confidentiality</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">RSA Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Encryption of data with public and private keys</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data integrity</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Hashing</td>
      <td style="border: 1px solid gray; padding: 8px;">Use of a hash algorithm such as SHA-2 to ensure that data is not tampered with</td>
      <td style="border: 1px solid gray; padding: 8px;">Transport</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Account Management</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Two-Factor Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">Use of two-factor authentication to verify user access</td>
      <td style="border: 1px solid gray; padding: 8px;">Presentation</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data access control</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Role-Based Access Control (RBAC)</td>
      <td style="border: 1px solid gray; padding: 8px;">Defines levels of access based on user roles</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Resource authorization</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Authorization Token</td>
      <td style="border: 1px solid gray; padding: 8px;">Generates a token at the end of a successful authorization process which is used to grant permission</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
  </tbody>
</table>
