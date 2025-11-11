# Cryptographic Algorithms Mechanisms 

Cryptographic algorithms are used to ensure data confidentiality, authenticity, integrity and non-repudiation in cloud-based mobile apps. To achieve these goals, cryptographic algorithms are often used in combination with mechanisms, such as Digital Signatures, Secret Key Cryptography and Public Key Cryptography. 

Digital Signatures validate the identity and authenticity of communications, while Secret Key Cryptography algorithms like AES, DES and 3DES protect transmitted data through the use of encryption. Public Key Cryptography algorithms like RSA, ECDSA and Diffie-Hellman can also be used to authenticate, encrypt and exchange secret keys between the mobile device and the cloud provider. In addition, protocols such as SSL / TLS can add an extra layer of security while protecting and verifying the communication and providing message integrity.

## Cryptographic Algorithms Mechanisms Examples: 

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="border: 1px solid gray; padding: 8px;">Security Requirement</th>
      <th style="border: 1px solid gray; padding: 8px;">Mobile Platform</th>
      <th style="border: 1px solid gray; padding: 8px;">Mechanism</th>
      <th style="border: 1px solid gray; padding: 8px;">Description</th>
      <th style="border: 1px solid gray; padding: 8px;">OSI Layer</th>
      <th style="border: 1px solid gray; padding: 8px;">Use for coding</th>
      <th style="border: 1px solid gray; padding: 8px;">Use for runtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Integrity</td>
      <td style="border: 1px solid gray; padding: 8px;">Android</td>
      <td style="border: 1px solid gray; padding: 8px;">HMAC-SHA256</td>
      <td style="border: 1px solid gray; padding: 8px;">A cryptographic hash function based on SHA256 that combines a shared secret and the message</td>
      <td style="border: 1px solid gray; padding: 8px;">7</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Confidentiality</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">AES-128</td>
      <td style="border: 1px solid gray; padding: 8px;">AES with 128 bit key size that supports authenticated encryption</td>
      <td style="border: 1px solid gray; padding: 8px;">6</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
    </tr>
    <tr>
      <td style="border: 1px solid gray; padding: 8px;">Authentication</td>
      <td style="border: 1px solid gray; padding: 8px;">iOS</td>
      <td style="border: 1px solid gray; padding: 8px;">ECDSA</td>
      <td style="border: 1px solid gray; padding: 8px;">Elliptic Curve Digital Signature Algorithm that provides digital signatures</td>
      <td style="border: 1px solid gray; padding: 8px;">7</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
      <td style="border: 1px solid gray; padding: 8px;">Yes</td>
    </tr>
  </tbody>
</table>
