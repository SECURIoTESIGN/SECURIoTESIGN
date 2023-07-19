# CSRF Attack 

CSRF attack stands for Cross-Site Request Forgery. It is a type of malicious exploit of a website where unauthorized commands are sent from a user that the website trusts. 

In this attack, a malicious website, email, or program causes the victim's web browser to perform an unwanted action on a trusted site when the user is authenticated. For example, a CSRF attack can be used to transfer funds or change a password without the user's knowledge.

To prevent CSRF attacks, websites should implement Cross-Site Request Forgery tokens, which are randomly generated tokens that are sent along with the user's request. The server will only process a request with a valid token. Additionally, websites should implement other security measures such as logging user activity and using security headers.