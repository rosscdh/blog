Date: 2012-07-05 14:00:00
Title: Disqus realtime
Tags: python,Disqus,realtime
Category: 2012europython
Slug: euro-python-discuss-real-time

# Disqus in Real time #

- redis
- gevent : spawn as many threads as you like (bitly geventspawn)
- exponential time sensitive backoff.. start fail start fail start fail.. kill it
- has priority threading
- yield thread is yield 0

### front end has to be fast ###

- pool redis connections
- cant maintain infinite connections to redis
- no dependency in the system
- request cycle: request -> flask -> get channel -> subscription pool -> returns queue to the request -> 
- uwsgi servers can use generators to stream data (of course great idea)
- ** long polling **: hold connection stream json, use new line as the delimiter just keeps the thing open
- not websockets because.. well they don't work yet (not fully supported)
- websockets will be the option with fallback to long polling .. soon in 2.0
- header MUST be application/json else the browser will cache the response
- pubsub is not threadsafe (halfduplex)

### test measure repeat ###

- darktime use existing network to loadtest (user complaints), 
- gargoyle turns features on and off

### stats ##

- measure all the things!
- graphite
- good when numbers dont add up (differential script results)
- testing in dist systems in **hard**
- express as +1 and -1
- try "scales" "metrics metrics everywhere"
- thunk? ent to end ack <http://zesty.ca/python/thunk.html>
- nginx - proxy_buffering off; is a MUST!
- nydis consistent hashin opensource github
