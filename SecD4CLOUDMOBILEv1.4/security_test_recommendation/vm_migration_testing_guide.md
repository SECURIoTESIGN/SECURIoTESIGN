# Testing the VM Migration Attack 

## Testing VM Migration 

VM Migration is a process of migrating virtual machines from one physical host to another. The process is usually done either manually or through automated tools. It is important to test the migration procedure before putting it into production to be sure that it is working correctly. 

In order to properly test VM Migration, the following steps should be followed: 

1. Prepare a test environment with two physical hosts that are connected to a local network.

2. Create a virtual machine on one of the physical hosts.

3. Configure the virtual machine to be migrated with the necessary information, such as network address, data storage, user access, etc.

4. Perform a test migration of the virtual machine from one physical host to the other.

5. Monitor the migration process to make sure that all operations are successfully completed.

6. Once the migration process has completed, verify that the virtual machine is working in the new environment, including checking all the configurations and data. 

7. Finally, test the functionality of the virtual machine in the new environment to ensure that all applications and services work as expected. 

By following these steps, organizations can ensure that the migration process works correctly and that any issues are addressed promptly.

## Testing Tools: 

Target Testing | Testing Technique | Test Analysis | Test Method | Test Tool | Mobile Platform
--- | --- | --- | --- | --- | --- 
Server | White-box | Dynamic | Exploratory | Nessus | N/A
Server | White-box | Static | Code Review | Fortify | N/A 
Server | Grey-box | Static | Comparing Security Policies| nmap | N/A
Client | Black-box | Dynamic | Vulnerability Scanning | Burpsuite | iOS/Android