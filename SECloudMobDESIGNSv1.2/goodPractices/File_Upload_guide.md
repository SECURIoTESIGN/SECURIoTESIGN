# File Uploading

Into web applications, when we expect upload of working documents from users, we can expose the application to submission of documents that we can categorize as malicious.	
We use the term "malicious" here to refer to documents that embed malicious code that will be executed when another user (admin, back office operator...) will open the document with the associated application reader.	
Usually, when an application expect his user to upload a document, the application expect to receive a document for which the intended use will be for reading/printing/archiving. The document should not alter is content at opening time and should be in a final rendered state.

The most common file types used to transmit malicious code into file upload feature are the following:

* Microsoft Office document: Word/Excel/Powerpoint
* Adobe PDF document: Insert malicious code as attachment.
* Images: Malicious code embedded into the file or use of binary file with image file extension.



For Word/Excel/Powerpoint/Pdf documents:
 
* Detect when a document contains "code"/OLE package, if it's the case then block the upload process.
For Images document:
* Sanitize incoming image using re-writing approach and then disable/remove any "code" present (this approach also handle case in which the file sent is not an image).





## Upload Verification

* Use input validation to ensure the uploaded filename uses an expected extension type;
* Ensure the uploaded file is not larger than a defined maximum file size;

## Upload Storage

* Use a new filename to store the file on the OS. Do not use any user controlled text for this filename or for the temporary filename;
* Store all user uploaded files on a separate domain. Archives should be analyzed for malicious content (anti-malware, static analysis, etc).

## Public Serving of Uploaded Content

* Ensure the image is served with the correct content-type (e.g. image/jpeg, application/x-xpinstall).

## Beware of "special" files

* The upload feature should be using a whitelist approach to only allow specific file types and extensions. However, it is important to be aware of the following file types that, if allowed, could result in security vulnerabilities;

* "crossdomain.xml" allows cross-domain data loading in Flash, Java and Silverlight. If permitted on sites with authentication this can permit cross-domain data theft and CSRF attacks. Note this can get pretty complicated depending on the specific plugin version in question, so its best to just prohibit files named "crossdomain.xml" or "clientaccesspolicy.xml".

* ".htaccess" and ".htpasswd" provides server configuration options on a per-directory basis, and should not be permitted. 