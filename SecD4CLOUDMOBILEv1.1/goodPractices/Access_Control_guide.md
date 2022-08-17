# Access Control	

Authorization is the process where requests to access a particular resource should be granted or denied. It should be noted that authorization is not equivalent to authentication - as these terms and their definitions are frequently confused. 
Authentication is providing and validating identity. 
Authorization includes the execution rules that determines what functionality and data the user (or Principal) may access, ensuring the proper allocation of access rights after authentication is successful. 

Web applications need access controls to allow users (with varying privileges) to use the application. They also need administrators to manage the applications access control rules and the granting of permissions or entitlements to users and other entities. 


## Role Based Access Control
	
Access decisions are based on an individual's roles and responsibilities within the organization or user base. An RBAC access control framework should provide web application security administrators with the ability to determine who can perform what actions, when, from where, in what order, and in some cases under what relational circumstances. 

Advantages: 

 * Roles are assigned based on organizational structure with emphasis on the organizational security policy 
 * Easy to use 
 * Easy to administer 
 * Built into most frameworks 
 * Aligns with security principles like segregation of duties and least privileges 

Problems: 

 * Documentation of the roles and accesses has to be maintained stringently. 
 * Multi-tenancy can not be implemented effectively unless there is a way to associate the roles with multi-tenancy capability requirements e.g. OU in Active 	Directory	
 * There is a tendency for scope creep to happen e.g. more accesses and privileges can be given than intended for. Or a user might be included in two roles if proper access reviews and subsequent revocation is not performed.
 * Does not support data based access control 

Areas of caution: 

* Roles must be only be transferred or delegated using strict sign-offs and procedures. 
* When a user changes his role to another one, the administrator must make sure that the earlier access is revoked such that at any given point of time, a user is assigned to only those roles on a need to know basis.  
* Assurance for RBAC must be carried out using strict access control reviews. 

## Discretionary Access Control 

Discretionary Access Control is a means of restricting access to information based on the identity of users and/or membership in certain groups. Access decisions are typically based on the authorizations granted to a user based on the credentials he presented at the time of authentication. The owner of information or any resource is able to change its permissions at his discretion. 

Advantages: 

 * Easy to use; 
 * Easy to administer; 
 * Aligns to the principle of least privileges; 
 * Object owner has total control over access granted. 

Problems: 
 
 * Documentation of the roles and accesses has to be maintained stringently; 
 * Multi-tenancy can not be implemented effectively unless there is a way to associate the roles with multi-tenancy capability requirements;   
 * There is a tendency for scope creep to happen e.g. more accesses and privileges can be given than intended for. 

Areas of caution: 
 * While granting trusts; 
 * Assurance for DAC must be carried out using strict access control reviews.

## Mandatory Access Control
 
Ensures that the enforcement of organizational security policy does not rely on voluntary web application user compliance. MAC secures information by assigning sensitivity labels on information and comparing this to the level of sensitivity a user is operating at.MAC is usually appropriate for extremely secure systems including multilevel secure military applications or mission critical data applications. 

Advantages: 

 * Access to an object is based on the sensitivity of the object; 
 * Access based on need to know is strictly adhered to and scope creep has minimal possibility; 
 * Only an administrator can grant access. 

Problems: 

 * Difficult and expensive to implement; 
 * Not agile. 

Areas of caution: 

 * Classification and sensitivity assignment at an appropriate and pragmatic level; 
 * Assurance for MAC must be carried out to ensure that the classification of the objects is at the appropriate level. 

## Permission Based Access Control
	
Is the abstraction of application actions into a set of permissions. A permission may be represented simply as a string based name, for example "READ". Access decisions are made by checking if the current user has the permission associated with the requested application action. 

The has relationship between the user and permission may be satisfied by creating a direct relationship between the user and permission (called a grant), or an indirect one. In the indirect model the permission grant is to an intermediate entity such as user group. 

A user is considered a member of a user group if and only if the user inherits permissions from the user group.  Systems that provide fine-grained domain object level access control, permissions may be grouped into classes. The system can be associated with a class which determines the permissions applicable to the respective domain object. 
>In such a system a "DOCUMENT" class may be defined with the permissions "READ", "WRITE" and "DELETE"; a "SERVER" class may be defined with the permissions "START", "STOP", and "REBOOT".