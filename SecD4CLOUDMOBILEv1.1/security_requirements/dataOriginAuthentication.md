# Data Origin Authentication 
     
Ensures that the data being received by the software comes from the source it claims to be. In other words it ensures that the data being received is authentic and from a trusted party. 

**Note:** *This requirement is applied between the communications.*  

Not addressing this requirement may lead to vulnerabilities explored by attacks such as:

                                                              
### 1. MITM attack:

This type of attacks occurs when an attacker gains access to a packet and re-sends it when it’s beneficial to him, resulting in him gaining the trust of the system.

### 2. Brute Force 

The attacker attempts to gain access to systems' asset (information, functionality, identity, etc.) protected by a finite secret value by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or a value that is functionally equivalent) that will unlock the asset.

### 3. VM Escape

This type of attack occurs whenever an application escapes the VM and obtains control over the VMM, as it escalates its VM privileges to root level. The malicious application accesses the host machine, bypassing the hypervisor.

### 4. Spoofing

Spoofing attacks are a fraudulent act in which an entity fakes its identity to attempt to access resources and critical data. There are four variants of the spoofing attack, namely, content spoofing, identity spoofing, resource location spoofing and action spoofing.

### 5. Cache Poisoning

This type of attack has to do with any attack whereby an attacker caches incorrect or harmful material. The cache targeted can be an application's cache (e.g., a web browser cache) or a public cache (fe.g., a DNS or ARP cache).
