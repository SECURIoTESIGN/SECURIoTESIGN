## Secure Java and C # Deployment

Since mobile-application security for the permissions-based Android platform and currently use Java and C# programming languages, in order to ensure security in the software, the SDLC should take into account the following procedures:

* Use mechanisms that enforce access control of applications to system resources, by defining permissions and protection domains and by using access control algorithms;
* Pay attention to setting the access level (private, package, protected and public) for each reference to an element of a primitive data or to an object;
* Use mechanisms that enforce language conventions, that is, lower-level mechanisms that require, among other things, that programs interfere with the normal operation of the sandbox, during compilation, loading in the virtual machine (VM) of the bytecodes, and execution. For compilation and loading in the VM of the bytecodes, static code analysis is used, and dynamic code analysis is performed.

In the event of runtime authorization failures, when an access control policy does not grant sufficient permissions to a user or an access control policy grants users unneeded permissions, the system may be exposed to security attacks. In this case, it is recommended to use the two major approaches in the Java and .Net Common Language Runtime platforms:

* Stack-based Access Control (SBAC): Ensure that only programs that satisfy a set of permission requirements gain access to restricted resources. SBAC systems should always stick to the Principle of Least Privilege;
* Role-based Access Control (RBAC): is a mechanism to restrict access to authorized users. RBAC systems provide access control based on permissions and roles.

## Not addressing this requirement may lead to vulnerabilities explored by attacks such as: 
 * Missing authentication: Missing authentication is a security vulnerability that occurs in software that does not perform any authentication for functionalities that require a provable user identity or consume a significant amount of resources.
