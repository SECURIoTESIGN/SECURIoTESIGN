## IoT Security

**Internet of Things (IoT) devices** fall into three main categories:

* Sensors, which gather data
* Actuators, which effect actions
* Gateways, which act as communication hubs and may also implement some 
automation logic.

All these device types may stand alone or be embedded in a larger product. They may also be complemented by a web application or mobile device app and cloud based service.
IoT devices, services and software, and the communication  channels that connect them, are at risk of attack by a variety of malicious parties,

Malicious intent commonly takes advantage of poor design, but even unintentional leakage of data due to ineffective security controls can also bring dire consequences to consumers and vendors. Thus it is vital that IoT devices and services have security designed in from the outset.


**Classification of Data**

* Define a data classification scheme and document it. 
* Assess every item of data stored, processed, transmitted or received by a device and apply a data classification rating to it.
* Ensure the security design protects every data item and collections of items against unauthorised viewing, changing or deletion,to at least its classification rating or higher.


**Physical Security**

* Any interface used for administrationor test purposes during development should be removed from a production device, disabled or made physically inaccessible.
* All test access points on production units must be disabled or locked, for example by blowing on-chip fuses to disable JTAG.
* If a production device must have an administration port, ensure it has effective access controls, e.g. strong credential management, restricted ports, secureprotocols etc.
* Make the device circuitry physically inaccessible to tampering, e.g. epoxy chips to circuit board, resin encapsulation, hiding data and address lines under thesecomponents etc.
* Provide secure protective casing and mounting options for deployment of devices in exposed locations.
* For high-security deployments, consider design measures such as active masking or shielding to protect against side-channel attacks


**Device Secure Boot**

* Make sure the ROM-based secure boot function is always used. Use a multi-stage bootloader initiated by a minimal amount of read-only code 
* Use a hardware-based tamper-resistant capability (e.g. a microcontroller security subsystem, Secure Access Module (SAM) or Trusted Platform Module (TPM)) to store crucial data items and run the trusted authentication/cryptographic functions required for the boot process. Its limited secure storage capacity must hold the read-only first stage of the bootloader and all other data required to verify the authenticity of firmware.
* Check each stage of boot code is valid and trusted immediately before running that code. Validating code immediately before its use can reduce the risk of attacks 
* At each stage of the boot sequence, wherever possible, check that only the expected hardware is present and matches the stage's configuration parameters.
* Do not boot the next stage of device functionality until the previous stage has been successfully booted.
* Ensure failures at any stage of the boot sequence fail gracefully into a secure state, to ensure no unauthorised access is gained to underlying systems, code or data. Any code run must have been previously authenticated.


**Secure Operating System**


* Include in the operating system (OS) only those components (libraries, modules, packages etc.) that are required to support the functions of the device.
* Shipment should include the latest stable OS component versions available.
* Devices should be designed and shipped with the most secure configuration in place. 
* Continue to update OS components to the latest stable versions throughout the lifetime of a deployed device.
* Disable all ports, protocols and services that are not used.
* Set permissions so users/applications cannot write to the root file system.
* If required, accounts for ordinary users/applications must have minimum access rights to perform the necessary functions. Separate administrator accounts (if required)will have greater rights of access. Do not run anything as root unless genuinely unavoidable.
* Ensure all files and directories are given the minimum access rights to perform the required functions.
* Consider implementing an encrypted file system.


**Application Security**


* Applications must be operated at the lowest privilege level possible, not as root. Applications must only have access to those resources they need. 
* Applications should be isolated from each other. For example, use sandboxing techniques such as virtual machines, containerisation, Secure Computing Mode (seccomp), etc
* Ensure compliance with in-country data processing regulations.
* Ensure all errors are handled gracefully and any messages produced do not reveal any sensitive information.
* Never hard-code credentials into an application. Credentials must be stored separately in secure trusted storage and must be updateable in a way that ensures security is maintained.
* Remove all default user accounts and passwords.
* Use the most recent stable version of the operating system and libraries.
* Never deploy debug versions of code. The distribution should not include compilers, files containing developer comments, sample code, etc.
* Consider the impact on the application/system if network connectivity is lost. Aim to maintain  normal functionality and security wherever possible.


**Credential Management**

* A device should be uniquely identifiable by means of a factory-set tamper resistant hardware identifier if possible.
* Use good password management techniques, for example no blank or simple passwords allowed,  never send passwords across a network (wired or wireless) in clear text, and employ a secure password reset process.
* Each password stored for authenticating credentials must use an industry standard hash function, along with a unique salt value that is not obvious (for example, not a username). 
* Store credentials or encryption keys in a Secure Access Module (SAM), Trusted Platform Module  (TPM), Hardware Security Module (HSM) or trusted key store if possible.
* Aim to use 2-factor authentication for accessing sensitive data if possible.
* Ensure a trusted & reliable time source is available where authentication methods require this, e.g. for digital certificates.
* A certificate used to identify a device must be unique and only used to identify that onedevice. Do not reuse the certificate across multiple devices.
* A "factory reset" function must fully remove all user data/credentials stored on a device.


**Encryption**

* When configuring a secure connection, if an encryption protocol offers a negotiable selection of algorithms, remove weaker options so they cannot be selected for use in a downgrade attack.
* Store encryption keys in a Secure Access Module (SAM), Trusted Platform Module (TPM), Hardware Security Module (HSM) or trusted key store if possible.
* Do not use insecure protocols, e.g. FTP, Telnet.
* It should be possible to securely replace encryption keys remotely
* If implementing public/private key cryptography, use unique keys per device and avoid using global keys. A device's private key should be generated by that device or supplied by an associated secure credential solution, e.g. smart card. It should remain on that  device and never be shared/visible to elsewhere. 


**Network Connections**

* Activate only those network interfaces that are required (wired, wireless - including Bluetooth etc.).
* Run only those services on the network that are required.
* Open up only those network ports that are required.
* Run a correctly configured software firewall on the device if possible.
* Always use secure protocols, e.g. HTTPS, SFTP.
* Never exchange credentials in clear text or over weak solutions such as HTTP Basic Authentication.
* Authenticate every incoming connection to ensure it comes from a legitimate source.
* Authenticate the destination before sending sensitive data.


**Logging**

* Ensure all logged data comply with prevailing data protection regulations.
* Run the logging function in its own operating system process, separate from other functions.
* Store log files in their own partition, separate from other system files.
* Set log file maximum size and rotate logs.
* Where logging capacity is limited, just log start-up and shutdown parameters, login/access attempts and anything unexpected.
* Restrict access rights to log files to the minimum required to function.
* If logging to a central repository, send log data over a secure channel if the logs carry sensitive data and/or protection against tampering of logs must be assured.
* Implement log "levels" so that lightweight logging can be the standard approach, but with the option to run more detailed logging when required.
* Monitor and analyse logs regularly to extract valuable information and insight.
* Passwords and other secret information should not ever be displayed in logs.


(https://www.iotsecurityfoundation.org/wp-content/uploads/2019/03/Best-Practice-Guides-Release-1.2.1.pdf)[https://www.iotsecurityfoundation.org/wp-content/uploads/2019/03/Best-Practice-Guides-Release-1.2.1.pdf]