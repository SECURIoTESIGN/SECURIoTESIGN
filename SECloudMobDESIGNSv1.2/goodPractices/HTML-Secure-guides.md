{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # HTML secure fashion\
Below are some good security engineering practices that serve as a guide to implementing HTML 5 in building mobile applications in a secure way.\
## Communication APIs\
### Web Messaging\
Web Messaging (also known as Cross Domain Messaging) provides a means of messaging between documents from different origins in a way that is generally safer than the multiple hacks used in the past to accomplish this task. However, there are still some recommendations to keep in mind:\
 * When posting a message, explicitly state the expected origin as the second argument to postMessage rather than  in order to prevent sending the message to an unknown origin after a redirect or some other means of the target window's origin changing.\
 * The receiving page should always: 1) Check the origin attribute of the sender to verify the data is originating from the expected location; 2) Perform input validation on the data attribute of the event to ensure that it's in the desired format.\
 * Don't assume you have control over the data attribute. A single Cross Site Scripting flaw in the sending page allows an attacker to send messages of any given format.\
 * Both pages should only interpret the exchanged messages as data. Never evaluate passed messages as code (e.g. via eval()) or insert it to a page DOM (e.g. via innerHTML), as that would create a DOM-based XSS vulnerability. For more information see DOM based XSS Prevention Cheat Sheet.\
 * To assign the data value to an element, instead of using a insecure method like element.innerHTML=data;, use the safer option: element.textContent=data;\
 * Check the origin properly exactly to match the FQDN(s) you expect. Note that the following code: if(message.origin.indexOf(".owasp.org")!=-1) \{ /* ... */ \} is very insecure and will not have the desired behavior as www.owasp.org.attacker.com will match.\
 * If you need to embed external content/untrusted gadgets and allow user-controlled scripts (which is highly discouraged), consider using a JavaScript rewriting framework such as Google Caja or check the information on sandboxed frames.\
### Cross Origin Resource Sharing\
 * Validate URLs passed to XMLHttpRequest.open. Current browsers allow these URLs to be cross domain; this behavior can lead to code injection by a remote attacker. Pay extra attention to absolute URLs.\
 * Ensure that URLs responding with Access-Control-Allow-Origin: * do not include any sensitive content or information that might aid attacker in further attacks. Use the Access-Control-Allow-Origin header only on chosen URLs that need to be accessed cross-domain. Don't use the header for the whole domain.\
 * Allow only selected, trusted domains in the Access-Control-Allow-Origin header. Prefer whitelisting domains over blacklisting or allowing any domain (do not use * wildcard nor blindly return the Origin header content without any checks).\
 * Keep in mind that CORS does not prevent the requested data from going to an unauthenticated location. It's still important for the server to perform usual CSRF prevention.\
 * While the RFC recommends a pre-flight request with the OPTIONS verb, current implementations might not perform this request, so it's important that "ordinary" (GET and POST) requests perform any access control necessary.\
 * Discard requests received over plain HTTP with HTTPS origins to prevent mixed content bugs.\
 * Don't rely only on the Origin header for Access Control checks. Browser always sends this header in CORS requests, but may be spoofed outside the browser. Application-level protocols should be used to protect sensitive data.\
### WebSockets\
 * Drop backward compatibility in implemented client/servers and use only protocol versions above hybi-00. Popular Hixie-76 version (hiby-00) and older are outdated and insecure.\
 * The recommended version supported in latest versions of all current browsers is RFC 6455 (supported by Firefox 11+, Chrome 16+, Safari 6, Opera 12.50, and IE10).\
 * While it's relatively easy to tunnel TCP services through WebSockets (e.g. VNC, FTP), doing so enables access to these tunneled services for the in-browser attacker in case of a Cross Site Scripting attack. These services might also be called directly from a malicious page or program.\
 * The protocol doesn't handle authorization and/or authentication. Application-level protocols should handle that separately in case sensitive data is being transferred.\
 * Process the messages received by the websocket as data. Don't try to assign it directly to the DOM nor evaluate as code. If the response is JSON, never use the insecure eval() function; use the safe option JSON.parse() instead.\
 * Endpoints exposed through the ws:// protocol are easily reversible to plain text. Only wss:// (WebSockets over SSL/TLS) should be used for protection against Man-In-The-Middle attacks.\
 * Spoofing the client is possible outside a browser, so the WebSockets server should be able to handle incorrect/malicious input. Always validate input coming from the remote site, as it might have been altered.\
 * When implementing servers, check the Origin: header in the Websockets handshake. Though it might be spoofed outside a browser, browsers always add the Origin of the page that initiated the Websockets connection.\
 * As a WebSockets client in a browser is accessible through JavaScript calls, all Websockets communication can be spoofed or hijacked through Cross Site Scripting. Always validate data coming through a WebSockets connection.\
### Server-Sent Events\
 * Validate URLs passed to the EventSource constructor, even though only same-origin URLs are allowed.\
 * As mentioned before, process the messages (event.data) as data and never evaluate the content as HTML or script code.\
 * Always check the origin attribute of the message (event.origin) to ensure the message is coming from a trusted domain. Use a whitelist approach.\
## Storage APIs\
### Local Storage\
 * Also known as Offline Storage, Web Storage. Underlying storage mechanism may vary from one user agent to the next. In other words, any authentication your application requires can be bypassed by a user with local privileges to the machine on which the data is stored. Therefore, it's recommended not to store any sensitive information in local storage.\
 * Use the object sessionStorage instead of localStorage if persistent storage is not needed. sessionStorage object is available only to that window/tab until the window is closed.\
 * A single Cross Site Scripting can be used to steal all the data in these objects, so again it's recommended not to store sensitive information in local storage.\
 * A single Cross Site Scripting can be used to load malicious data into these objects too, so don't consider objects in these to be trusted.\
 * Pay extra attention to \'93localStorage.getItem\'94 and \'93setItem\'94 calls implemented in HTML5 page. It helps in detecting when developers build solutions that put sensitive information in local storage, which is a bad practice.\
 * Do not store session identifiers in local storage as the data is always accesible by JavaScript. Cookies can mitigate this risk using the httpOnly flag.\
 * There is no way to restrict the visibility of an object to a specific path like with the attribute path of HTTP Cookies, every object is shared within an origin and protected with the Same Origin Policy. Avoid host multiple applications on the same origin, all of them would share the same localStorage object, use different subdomains instead.\
### Client-side databases\
 * Use a new standard Indexed Database API or IndexedDB (formerly WebSimpleDB) is actively developed, which provides key/value database storage and methods for performing advanced queries.\
 * It's recommended not to store any sensitive information in local storage.\
If utilized, WebDatabase content on the client side can be vulnerable to SQL injection and needs to have proper validation and parameterization.\
 * Like Local Storage, a single Cross Site Scripting can be used to load malicious data into a web database as well. Don't consider data in these to be trusted.\
## Geolocation\
 * The Geolocation RFC recommends that the user agent ask the user's permission before calculating location. Whether or how this decision is remembered varies from browser to browser. Some user agents require the user to visit the page again in order to turn off the ability to get the user's location without asking, so for privacy reasons, it's recommended to require user input before calling getCurrentPosition or watchPosition.\
## Sandboxed frames\
 * Use the sandbox attribute of an iframe for untrusted content.\
 * The sandbox attribute of an iframe enables restrictions on content within an iframe. The following restrictions are active when the sandbox attribute is set:\
   * All markup is treated as being from a unique origin.\
   * All forms and scripts are disabled.\
   * All links are prevented from targeting other browsing contexts.\
   * All features that trigger automatically are blocked.\
   * All plugins are disabled.\
## Offline Applications\
 * Whether the user agent requests permission from the user to store data for offline browsing and when this cache is deleted, varies from one browser to the next. Cache poisoning is an issue if a user connects through insecure networks, so for privacy reasons it is encouraged to require user input before sending any manifest file.\
 * Users should only cache trusted websites and clean the cache after browsing through open or insecure networks.\
## HTTP Headers to enhance security\
Consult the project OWASP Secure Headers in order to obtains the list of HTTP security headers that an application should use to enable defenses at browser level.\
}