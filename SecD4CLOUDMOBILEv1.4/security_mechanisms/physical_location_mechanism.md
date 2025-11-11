# Physical Location Mechanisms 

Security physical location mechanisms are applied to cloud-based mobile apps to ensure that user data is not accessed or stored from locations outside of an approved geographic region. These mechanisms include technologies such as geofencing and IP address tracking. Geofencing verifies that user data is being accessed and stored within a predetermined geographic area by creating a virtual fence around the area. IP address tracking allows mobile apps to identify the geographical location associated with a particular IP address in order to verify that a user is located in the approved geographic area. These security location mechanisms are essential for cloud-based mobile apps, as they help prevent unauthorized access to user data from malicious actors located in remote locations.

## Physical Location Mechanisms Examples: 

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
      <td style="border: 1px solid gray; padding: 8px;">Authenticated Access</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">Biometric Scanner</td>
      <td style="border: 1px solid gray; padding: 8px;">Uses user's fingerprints as part of the authentication process</td>
      <td style="border: 1px solid gray; padding: 8px;">Physical</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data Integrity</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Transparent Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Files are encrypted transparently and automatically</td>
      <td style="border: 1px solid gray; padding: 8px;">Network</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data Availability</td>
      <td style="border: 1px solid gray; padding: 8px;">Both</td>
      <td style="border: 1px solid gray; padding: 8px;">Secure Boot & Root</td>
      <td style="border: 1px solid gray; padding: 8px;">Ensures that all parts of system are authenticated and verified</td>
      <td style="border: 1px solid gray; padding: 8px;">Physical</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data Confidentiality</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">App sandboxes</td>
      <td style="border: 1px solid gray; padding: 8px;">Prevents unauthorized access to specific files</td>
      <td style="border: 1px solid gray; padding: 8px;">Application</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Data Security</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">Full Disk Encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">Encrypts all data on device</td>
      <td style="border: 1px solid gray; padding: 8px;">Network</td>
    </tr>
  </tbody>
</table>
