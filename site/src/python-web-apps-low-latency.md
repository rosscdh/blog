Date: 2012-07-05 09:00:00
Title: Low latency web apps with python
Tags: python,latency,web,apps
Category: 2012europython
Slug: python-web-apps-low-latency

# Low latency webapps with python #

- speaker woks for financial banking systems with high throughput and where speed is **everything**
- key is visualization of all moving parts.. easy to use and digest graphs
- scatter histograms and line are most useful

### WSGI frameworks ###

- all work in more or less the same way
- create request, dispatch url, execute controller render view and return response

### Shared state ###

- sql or nosql
- lock files
- messaging AMQP
- XML-RPC, JSON-RPC SOAP etc
- DLM distributed lock manager - speaker wrote his own and will demo

### DLM ###

- provides mutex over network
- from dlm import LockClient
- all clients have unique name
- create a lock in each uwsgi process
- unique lock name
- lock.acquire()
- with lock: perform statements
- demo with multiple clients connecting to central DLM manager

### Background processes mod_wsgi ###

- can run as daemons
- and useful for background tasks
- prone to hanging

### Summary ###

- presented by diverman @ Deutsche Boerse AG
- a little boring/simplistic presentation but ok