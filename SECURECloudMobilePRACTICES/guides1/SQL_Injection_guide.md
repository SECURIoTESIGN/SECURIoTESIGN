# SQL Injection  

An SQL injection attack consists of insertion or "injection" of either a partial or complete SQL query via the data input or transmitted from the client (browser) to the web application. 
SQL Injection flaws are introduced when software developers create dynamic database queries that include user  supplied input. To avoid SQL injection flaws is simple. Developers need to either: 
a) stop writing dynamic queries; 
b) prevent user supplied input which contains malicious SQL from affecting the logic of the executed query. 

## Primary Defenses: 

* Option 1: Use of Prepared Statements (with Parameterized Queries) 
* Option 2: Use of Stored Procedures 
* Option 3: White List Input Validation 
* Option 4: Escaping All User Supplied Input 

## Additional Defenses: 

* Also: Enforcing Least Privilege 
* Also: Performing White List Input Validation as a Secondary Defense
