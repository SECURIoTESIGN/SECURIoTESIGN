# XML Injection Attacks

It is an attacking technique used against XML-based applications to modify or compromise their normal operation.

## Definition

XML Injection (XMLi) attacks are carried out by injecting pieces of XML code along with malicious content into user inputs in order to produce harmful XML messages. The aim of this type of attacks is to compromise the system or system component that receives user inputs, making it malfunction (e.g. crash), or to attack other systems or subsequent components that process those injected XML messages. This type of attack can be classified into 4 categories:
  
 * Deforming: Attack input values of Type 1 are XML meta-characters, such as <, >, ]] >, that are intro- duced to compromise the structure of generated XML messages;
 * Random closing tags: Attack input values of Type 2 are random XML closing tags (e.g., < /test>), aiming at deforming the generated XML messages to reveal their structure;
 * Replicating: Attack input values of Type 3 are strings of characters consisting of XML tag names and malicious content;
 * Replacing: Attack input values of Type 4 are similar to those of Type 3 but they involve multiple input fields in order to comment out some existing XML elements and inject new ones with malicious content.

## Attacker Powers

 * Obtain confidential information;
 * Change the underlying business logic of the destination.

## Recommendations

To ensure that the mobile application is resilient or immune to Spoofing attacks, it is recommended that the measures described in the good practice report and the security tests present in the full report are followed to ensure authenticity, integrity, privacy and authenticity of the data.
 
 
## XML Injection Attacks Diagram


