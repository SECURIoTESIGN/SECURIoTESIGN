# Security Best Practices Guidelines for Injection Prevention in Java 

#Injection Prevention in Java

##Best Practices

1. **Input Validation**: Validate user input to ensure that it adheres to acceptable format, length, type, and value before passing it to the application.

2. **Whitelisting**: Use whitelisting for accepting input data instead of blacklisting - that is, allow valid values and reject anything else.

3. **Parameterised Queries**: Use parameterised queries (aka prepared statements) when working with user input. This uses parameter binding instead of concatenation to construct queries, which makes it resistant to SQL injection attacks.

4. **Stored Procedures**: Use stored procedures with input validation instead of dynamic queries.

5. **Object Relational Mapping (ORM)**: Use an ORM framework for accessing a database that provides database query parameterization and avoids the developers from writing dynamic SQL queries.

6. **Use an Escape Mechanism**: Use an escape function for escaping any potentially dangerous characters when user input is passed to a backend system.

7. **Escaping Wildcard Characters**: Escape all wildcard characters in user-supplied data to prevent wildcards expanding into a larger list of values when used in comparison operations.

8. **Disable Object Relational Mapping (ORM) Metacommands**: Disable ORM meta-commands (like Direct SQL) for preventing an application passing user input directly to a database without validation. 

9. **Enforce Timeouts and Request Limits**: Enforce request timeouts and limit the number of requests an application allows from a particular user to limit the risk of attacks.

10. **Regular Security Scanning**: Perform regular security scanning of your application and use automated tools to check for anonymous access points, missing patches, and malicious code.