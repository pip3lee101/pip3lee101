1. Broken access control
Access controls define how users interact with data and resources including what they can read or edit. A broken access control vulnerability exists when a user has the ability to interact with data in a way that they don’t need. For example, if a user should only be able to read payment details but can actually edit them, this is a broken access control. Malicious actors use this vulnerability to gain unauthorized access to systems, networks, and software. They can then escalate the privileges, give the user ID additional access within the ecosystem, to negatively impact data confidentiality, integrity, or availability.

2. Broken authentication
Broken authentication vulnerabilities also focus on user access. However, in this case, malicious actors compromise the information that confirms a user’s identity, such as by stealing passwords, keys, or session tokens. The malicious actor gains unauthorized access to the systems, networks, and software because the company failed to adequately set appropriate identity and access management controls.

3. Carriage Return and Line Feed (CRLF) Injection
Carriage return is a command that indicates the start of a line of code, normally denoted as \r. Line feed is a command that indicates the end of a line of code, normally denoted as \n. Like many other software, each operating system uses a different combination of carriage return and line feed. When malicious actors engage in CRLF injections, the inserted code changes the way that the web application responds to commands. This can be used to either disclosure sensitive information or execute code.

4. Cipher transformation insecure
Cipher, a standard term for “encryption algorithm,” is the math behind an encryption/decryption process. Transformation is the list of operations performed on an input to provide the expected output. So, a cipher transformation is the set of operations that turn unreadable encrypted data back to readable, decrypted data. A cipher transformation insecure vulnerability means that the encryption algorithm is easy to break, ultimately undermining the purpose of encryption in the first place.

5. Components with known vulnerabilities
Every web application relies on other components to work. For example, if you’re running an application on an unpatched web/application server, the server is the component with known vulnerabilities. The Common Vulnerabilities and Exposures (CVE) list includes all known security vulnerabilities. Since malicious actors are aware of the list, they regularly look for components without the appropriate security patch updates. Once they can compromise one component of the web application, they can gain access to the application’s data, too.

6. Cross-Origin Resource Sharing (CORS) Policy
Every web-based application uses a URL as a way to connect the user’s browser to its server. One common protection is called a Same Origin Policy. According to this, the server will only respond to a URL that has the same protocol, top-level domain name, and path schema. This means that you can access http://company.com/page1 and http:/company.com/page2 because they both have the following in common:

Protocol: HTTP
Domain: Company.com
Path schema: /page#
Although secure, the Same Origin Policy becomes restrictive when working with web-based applications that need access to resources that connect to subdomains or third-parties.

A CORS policy gives the browser permission to access these shared resources by creating a set of allowed HTTP headers considered “trusted.” For example, an application may need to pull data from two databases on different web servers. Creating a specific “allowed” list becomes too much work as you add more servers. Since the application is “shared” by both servers, the organization creates a CORS policy that lets browsers connect to both. However, if a CORS policy is not well defined, then the policy might allow the servers to provide access when a malicious actor requests it.

7. Credentials management
User credentials consist of a user ID and password. To gain access to an application, the user must input both pieces of information into the login page. The application compares this data to that stored in its database. If both pieces match, then it grants the user access. However, databases often store this information in plaintext or use weak encryption. Poor credentials management makes it easy for attackers to steal credentials and use them to gain access to web applications.

8. Cross-site request forgery (CSRF)
A CSRF attack leverages social engineering methods to get a user to change information, like user name or password, in an application. Unlike malware or cross-site scripting (XXS) attacks, a CSRF requires a user to be logged into the application that uses only session cookies for tracking sessions or validating user requests. Once the user takes the intended action, the attacker leverages the browser to perform the rest of the attack, such as transferring funds, without the user realizing what happened. For example, as OWASP explained, the “buy now” feature on retail websites is easy to exploit through a CSRF attack because the attacker can use the cookies stored on the browser that saves the payment data to complete the attack.

9. Cross-site scripting (XSS)
Distinct from a CSRF which requires a user logged into an application to be tricked into doing something, an XSS attack requires the cybercriminal to insert code into a web page, usually in some element of the page like an image. When the user opens the web page on their browser, the malicious code downloads and executes in the browser. For example, the code may redirect users from a legitimate site to a malicious one.

10. Directory indexing
Web servers often list all the files stored on them in a single directory. If a user is trying to locate a specific file in a web application, they normally include the file name as part of the request. If that file is not available, the application will return a list of all indexed files, giving the user a way to choose something else.

However, web servers automatically index the files. If the application returns a list of all files stored, a malicious actor exploiting vulnerabilities in the directory index can gain access to information that can tell them more about the system. For example, it can tell them about naming conventions or personal user accounts. Both of these data points can be used to locate sensitive information or engage in credential theft attacks.

11. Directory traversal
Also called directory climbing, dot-dot-slash, and backtracking attack, the directory traversal method leverages the way in which an application gets data from the webserver. Generally, Access Control Lists (ACLs) limit user access to specific files within a root directory.

Consider a set of nested folders that follow this order:

Root directory: My Very Sensitive Data (MVSD)
Inside MVSD folder: Protecting from H@x0rs (PfH) folder
Inside PfH folder: My Password is Bad (MPiB) folder
Inside MPiB folder: H@x0rs Stole My Info file
Now, you might have an additional set of folders outside that root folder including Pictures, Videos, and Downloads. Unless you have access to each of these other root folders, you can’t access the information they contain.

Web applications organize information the same way, even if you don’t see it. In a directory traversal attack, malicious actors figure out the URL structure that the application uses to request files. Using the hypothetical above, that URL might be:

www.myinsecurewebapp.com/MyPas... “.asp?item=” indicates that this URL pulled the file “H@x0rsStoleMyInfo” from the “My Password is Bad” folder. Now, they know the structure of folders and how to start getting different files.

Using this structure, they add “../” at the end. The “../” indicates moving from one folder to one just above it in the hierarchy. The new request might look like this:

www.myinsecurewebapp.com/MyH@cking.asp?item=../

They keep adding the ../ until they gain access to another file. If they know the name of the file, such as an operating system file name, they might do this:

www.mywebsiteinfo.com/MyPasswordisBad.asp?item=../genericoperatingsystemfile

At this point, they just keep adding more “../” after the equal sign until they get to the folder level and file they want.

12. Encapsulation
Unlike some of the other vulnerabilities that leverage web browser access to applications, encapsulation vulnerability exploits focus on weaknesses in the way a developer coded the application. The programming term encapsulation refers to bundling data and actions that can be taken on that data into a single unit. Encapsulation protects data by hiding details about how the code works which creates a better user interface. Users don’t need to know how the application brings them data; they just need access to it.

For example, a developer can bundle access controls, like read/write permissions, into an application’s ability to retrieve data. When the user requests information in the application, it returns only the data that they have permission to access.

However, if the developers fail to clearly define the boundaries between the data and the actions taken across different areas of the application, the application has an encapsulation vulnerability. Attackers exploit this by sending the application a request that they know will result in an error message. The error message gives them information about how the application works, enabling additional attack types such as a denial of service.

13. Error handling
Several different attack methods rely on how an application responds to abnormal inputs or conditions. One example of an error message is the “404 not found” message when you try to access a website. For most enterprise applications and systems, error messages provide valuable information about how to fix a problem.

However, for web applications, too much information returned through an error message can give malicious actors that same information. Often, attackers send the web application a query that they know will return an error message. They usually do this during the reconnaissance phase, where they try to get as much information as possible so they can find exploitable vulnerabilities.

14. Failure to restrict URL access
As with many other web application vulnerabilities, this one also aligns with access control rights. Applications use URL restrictions to prevent non-privileged users from accessing privileged data and resources. Every clickable button in a web application directs to a URL. A failure to restrict access vulnerability means that while clicking the button in the application would prevent access, directly using the URL into the browser allows access. When an application fails to restrict URL access, malicious actors can use “forced browsing” for an attack.

For example, a web application might have a URL structure that looks like this:

www.insecurewebapp.com/failure... the attackers know that the last item in that URL is the data type, they can try to take guesses at the URL structure for a specific type of sensitive information.

www.insecurewebapp.com/failure... the application has a failure to restrict URL access vulnerability, plugging that URL directly into the browser gives the attacker access.

15. HTTP response splitting
HTTP response splitting is a type of CRLF injection attack. HTTP is the way that a browser sends queries and a server sends back responses. In an HTTP response splitting attack, the malicious actors use the CR and LF notations to manipulate how the browser and server “talk” to one another that sends a request but asks the server to “split” the response into different parts. Splitting the response into two parts gives the attacker control over what data the server sends in response to the second part of the request. When that requested data is sensitive or user ID data, the malicious attacker has completed the attack.

16. HTTP verb tampering
HTTP is the protocol that lets applications respond to requests and retrieve data. An HTTP verb is one of several actions that the application can use when querying the server. Common ones HTTP verbs include:

GET: retrieves data from specified source
HEAD: requests preview of specified resource
POST: submits entity to specified resource, such as editing data
PUT: transmits new data to the specified resource replacing the old information
DELETE: deletes the specified resource entirely
Most web applications use HTTP verbs to authenticate users and manage access privileges. Malicious actors can bypass authentication and access controls intended to protect privileged information.

17. Improper certificate validation
SSL certificates bind a domain name, server name, or hostname to a company and location. For example, GoodSecureCo installs the SSL certificate data files on its US web servers. Every time a browser asks for data from the US web server, the SSL certificate checks to make sure that the user’s browser connects with an approved owner. The two securely connect if the answer is yes.

When software refuses to validate or incorrectly validates the certificate, it has an improper certificate validation vulnerability. Most often, attackers create a false trusted entity that tricks the server or application into thinking the certificate is valid so it accepts the data transfer as legitimate. Often, malicious actors use improper certificate validation vulnerabilities as a way to install malware on endpoints.

18. Injection flaw
An injection flaw enables a variety of different attack methods. Any application that enables users to update a database, shell command, or operating system call can have an injection flaw. In computing, an interpreter is a program that takes a command, generates an instruction, and performs the action within the application.

Malicious actors use injection flaws to change the commands which leads to new and unintended actions within the application. Leveraging these flaws, attackers can create, read, update, or delete data.

19. Insecure cryptographic storage
Encrypting stored data is a common best practice for preventing unauthorized access to or use of sensitive information. Encryption takes information stored in a readable format, such as PlainText, then uses mathematical algorithms to scramble it, making it unreadable. Encryption typically requires an encryption key, which is the technology that applies the algorithm that scrambles the data and is also used to make the information readable again. However, if someone finds the encryption key, the protection no longer works.

The insecure cryptographic storage vulnerability means you have a problem with one or more of the following:

Not encrypting all sensitive data
Improper key storage and management
Easy to crack encryption algorithms
Internally-designed, untested algorithm
20. Insecure deserialization
Applications handle complex data structures. Serialization converts the structures into an object that can be stored and transmitted easily. For example, think about different actions that go into making a peanut butter and jelly sandwich:

Get plate
Get bread
Open bread
Take out bread 1
Put bread 1 on plate
Take out bread 2
Put bread 2 on plate
Get knife
Get peanut butter
Open peanut butter
Get jelly
Open jelly
Get peanut butter on knife
Put peanut butter on bread 1
Get jelly on knife
Put jelly on bread 2
Smoosh bread 1 and bread 2 together with covered sides facing
You need all of these things to happen as part of making the sandwich, but they aren’t necessarily step-by-step in this order. Having to send all 17 of these data points, like individual messages, every time someone asks for a peanut butter and jelly sandwich can be time-consuming to write down and send. Most likely, you’d group them in a document as “Peanut Butter and Jelly Sandwich” that you send when someone asks, similar to serialization. When the person opens the document, they can see each individual data point, similar to deserialization.

Deserialization is the process of reconstructing the original, expanded data structure. With a deserialization vulnerability, malicious actors can change the application logic or execute code remotely, one of the most serious attack types.

21. Insecure digest
Another cryptographic vulnerability, an insecure message-digest vulnerability reduces the effectiveness of encryption. A message-digest contains the cryptographic hash function, which is the algorithm that maps an arbitrary length of data to the fixed bit array, a way of compactly storing data. Unlike encryption that requires the sender and user to have keys, hash functions do not.

Malicious actors leverage insecure digest vulnerabilities to engage in a “hash collisions attack.” The goal of the attack is to see if sending an input results in generating a duplicative hash. If the attackers brute force a shared hash, then they can offer a malicious file for download using this hash, which leaves the end-user assuming that the file is valid.

22. Insecure direct object references (IDOR)
Web application URLs can expose the format/pattern used for directing users to backend storage locations. For example, a URL might indicate the format/pattern for a record identifier in a storage system such as a database or file system.

Alone, the IDOR may be a low-risk issue. However, an IDOR in combination with a failed access control check gives attackers a way to successfully launch an enumeration attack.

23. Insufficient logging and monitoring
Insufficient logging and monitoring vulnerabilities occur when your data event logs fail to capture the necessary information that can prevent an attack. Every user, device, and resource generates an event log that tells your security team what is happening in your systems, networks, and applications.

Since successful attacks often use vulnerability probing during the reconnaissance stage, collecting the right event log data is a way to mitigate risk. Common logging and monitoring weaknesses include:

Failure to collect logs for auditable events like logins, failed logins, and high-value transactions
Failure to generate an adequate and clear warning and error logs
Failure to monitor application and API logs for abnormal activity
Storing logs locally
Failure to effectively set alerting thresholds and response escalation processes
Lack of alert triggers during penetration tests and dynamic application security testing (DAST) scans
Lack of real-time or near real-time application detection, escalation, and alerting functions
24. Insufficient session expiration
Session timeout is when an application automatically logs a user out after being idle for a specified amount of time. When an application is idle and open, attackers look to steal the credentials associated with the account.

Some examples of insufficient session expiration weaknesses include:

Lack of session timeout
Session timeouts that are longer than necessary
Inability to trace session creation/destruction to analyze trends
25. Insufficient transport layer protection
Transport layer security (TLS) is the way that computer applications securely “talk” to one another on the internet. Some applications only use TLS during the authentication process, leaving data and ID session information exposed when someone uses the application.

Attackers can use this vulnerability to intercept data as it travels across the internet between the user’s device and the application server.

26. Lightweight Directory Access Protocol (LDAP) injection
LDAP is a protocol that lets applications talk with directory services servers that store user IDs, passwords, and computer accounts. When applications accept user input and execute it, attackers can exploit the LDAP server by sending malicious requests.

Some examples of LDAP coding issues include:

Excess access privileged assigned to LDAP accounts
Lack of output regulation
Inability to perform dynamic checks
Lack of static source code analysis
27. Malicious code
Traditionally, code that intends to cause harm is considered malicious code. For example, people normally consider malicious code in terms of viruses, malware, and ransomware.

However, it also refers to code that can provide a backdoor into an application that lets people gain remote access to a computer. Lack of secure coding practices can lead to application backdoors. Although unintended, these programming errors make the web application vulnerable. Additionally, since modern applications often copy and paste code from one place to another, a mistake in one source can lead to the same malicious code being used in multiple applications.

28. Missing function level access control
Once users authenticate to an application, the function level access controls define the actions they can take within it. For example:

www.insecurewebapp.com/genericusername/read

www.insecurewebapp.com/SuperAd... on this example, Generic Username can read files in this application while Super Adminuser can edit within this application. Because the access rights are included in the URL, no one needs the authentication that protects these actions. Authenticated non-administrative users or unauthenticated users can type in a URL hoping to gain administrative access. For example, the malicious actors might try to type:

www.insecurewebapp.com/SuperAd... missing function level access control means that the malicious actor doesn’t need to authenticate to the system and can now delete data.

29. Missing PT_DENY_ATTACH
Although a bit more specific and technical than other web application vulnerabilities, this one is increasingly important as companies build out more mobile applications. A debugger is a program that helps application developers find errors in their coding. They often use debuggers to keep the application to prevent downtime from errors. However, malicious actors can leverage these same debuggers to learn how the application works and find ways to exploit them.

Process trace, more commonly called ptrace, is a system call that many debuggers and code analysis tools use. However, ptrace calls give tools a way to control their targets. The PT_DENY_ATTACH is a command for iOS mobile applications that prevents debuggers from attaching to applications. A missing PT_DENY_ATTACH command leaves an iOS mobile application at risk because malicious attackers can launch ptrace, connect to the application, and infiltrate it.

30. Operating System (OS) command injection
Some web applications make calls to operating systems so that they can communicate with the operating system or hardware. OS calls include functions like:

Process control: monitoring what an application is doing and providing for termination
File management: giving the application access to interact with files
Device management: requesting or managing hardware like processing power
Information maintenance: managing or maintaining information as part of keeping data updated
Inter-process communication: coordinating processes for effective operation
Insecure OS command calls allow users to supply unvalidated inputs. In other words, the malicious actors can take the OS command call, add an additional query notation, and gain valuable information about how to exploit the application.

31. Race condition
Web application processes generally rely on a series of actions, run in order, to do a task. For example, consider the following process:

Click Word icon
Wait for Word to open
Click “open file”
Wait for list of file storage locations
Look for file name you want
Click file with the right name
Wait for file to open in Word
Edit document
You need to do these steps in that precise order so that you can write in a new Word document. Functionally, many applications rely on a similar approach, where each step relies on the completion of the previous one.

However, application tasks are often more complex and need to be faster. This means that they use multi-threaded and asynchronous order. For example, if you’re collaborating in real-time with a co-worker on a document in a shared drive, you’re both giving the application tasks. This is where the race condition vulnerability comes into play.

Incorrectly coded web applications might have logic adjusting for asynchronous actions but lack the appropriate controls. When this happens, malicious attackers can manipulate the timing of actions, which throws off the sequencing and leads to unexpected, often maliciously intended, application behaviors.

32. Remote code execution (RCE)
RCE vulnerabilities are coding mistakes in web applications that allow malicious actors to input code regardless of their geographic location. RCEs are a larger category of web application injection vulnerabilities where malicious actors insert their own code into an application that does not verify user inputs so that the server views it as legitimate application code. Generally, attackers will leverage unpatched commonly known vulnerabilities and input their code into the application.

33. Remote file inclusion (RFI)
Developers use “include” statements in their code to connect common directories to an application. For example, an application might want to pull information from a database. Instead of manually coding it to pull each file, the “include” statement can be used to connect to the entire source directory so that it can use everything stored there.

If a web application has an RFI vulnerability, malicious actors can direct the application to upload malware or other malicious code to the website, server, or database.

34. Security misconfiguration
One of the most prevalent web application vulnerabilities is the potential for a security misconfiguration. Generally, this vulnerability occurs when an organization fails to change default Security settings. For example, off-the-shelf software generally ships with a default administrative ID and password. Failure to change these is considered a security misconfiguration.

Typical security misconfigurations include:

Use of default accounts/passwords
Lack of secure password policy
Unpatched software
Lack of appropriate file and directory configurations
Leaving unused features, components, and other resources
Lack of encryption
Poor firewall policies
35. Sensitive data exposure
Unlike a data breach where a cybercriminal steals information, sensitive data exposure vulnerabilities leave information visible to the public.

Several sensitive exposure vulnerabilities exist, including:

Lack of Secure Sockets Layer (SSL) protocol that authenticates and encrypts data
Misconfigured cloud storage locations storing data in plaintext
Data transmitted in clear text
Outdated or weak encryption algorithms
Weak or default cryptography keys used
36. Session ID leakage
Session IDs are the unique identifiers that authenticate users and track their activities when they use a web application. Web application vulnerabilities that lead to session leakage include:

Storing the session ID in the query string. By storing the session ID in the part of the URL that asks the application to retrieve information from the database, sharing of that URL allows the recipient to inherit that session without new authentication.
Storing the session ID in HTTP cookies: By storing the session ID in the small data files that let a web server remember a web browser and using the unencrypted HTTP protocol, the application gives the attacker the ability to steal the session ID and impersonate the user.
37. SQL Injection
Structured Query Language (SQL) is a programming language for databases that enables data retrieval and manipulation for relational databases. A SQL injection vulnerability falls under the larger group of unvalidated user inputs. When cybercriminals send requests that they know are false, the web application returns an error message that gives them information about how the database is organized and protected.

38. Unrestricted File Upload
Web applications often incorporate file upload capabilities. For example, if you want to input data in bulk, you might upload a CSV file to a database. An unrestricted file upload vulnerability can be a lack of authentication/authorization when someone tries to upload a file. This means that the application fails to verify the user, giving malicious actors the ability to upload compromised files. Additionally, the application may fail to sanitize files prior to uploading, thus giving attackers a way to leave malicious content in the files, like macros that hide malware.

Additional file upload vulnerabilities include:

Allows all file extensions
Fails to authorize or authenticate users
Fails to scan content to ensure the file type is expected
Allows webserver to fetch files
Stores files in a publicly accessible directory
39. Unvalidated automatic library activation
Developers use third-party libraries to save time when coding. Often, this allows them to use pre-tested code that speeds up the application development process. However, the use of publicly available, open-source code increases security risks, including:

Abandoned projects that are no longer updated
Lack of documented ownership increases the risk of malicious code added
Monitoring for library updates to fix vulnerabilities
Since many applications involve third-party library dependencies, this vulnerability is becoming more common.

40. Unvalidated redirects and forwards
Web applications can use redirects or forwards after a user submits a form. For example, if your marketing website has a form so that visitors can download a whitepaper, the page redirects or forwards them to the “thank you” page when they submit the form. However, malicious actors can impersonate these redirected or forwarded page URLs to steal user information.

Examples of this vulnerability include web applications with:

Large numbers of destination pages
Fail to store full URLs
Lack identifiers for these redirects/forwards
Lack of identifiers used as request parameters
Failure to filter out untrusted URL inputs
41. XML External Entities (XXE)
Extensible Markup Language (XML) describes data, like the contents of a webpage or database file. XML formatting allows applications to understand information and share data consistently. In order to read this data, you need to have an XML processor. Also referred to as an XML parser, these automated tools read files, transform the content, update databases, and deliver that content so the program can access it.

However, when web applications use XML format to transmit data between the browser and server, they often use APIs to process the data. Within the XML standard, storage units are called “entities.” External entity refers to a storage unit that can access local or remote content.

An XXE vulnerability can arise from failure to:

Know the source before accepting or uploading XML data
Disable document type definitions (DTDs)
Use less complex data formats like JSON
Patch XML processors or underlying operating system
Detect XXE in source code
