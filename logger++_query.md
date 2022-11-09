///// for http request smuggling
(Request.Headers CONTAINS "Transfer-Encoding") AND Request.Host CONTAINS "web-security-academy.net"


///// HOst header chace posining
(Response.Headers CONTAINS "X-Cache" or Response.Headers CONTAINS "Set-Cookie" or Response.Headers CONTAINS "Cache-Control") AND Request.Host CONTAINS "web-security-academy.net"

//// param miner
(Request.Headers CONTAINS "X") AND Request.Host CONTAINS "web-security-academy.net"

//// CORs
(Response.Headers CONTAINS "Access-Control-Allow-Origin") AND Request.Host CONTAINS "web-security-academy.net"
