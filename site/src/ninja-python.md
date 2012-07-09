Date: 2012-07-06 12:15:00
Title: Ninja Python - Sneaking python into large Java enterprises
Tags: python,sneaky,java,enterprise
Category: 2012europython
Slug: ninja-python

# How did you do that? - Sneaking python into large organization #

- if you do it right, you wont have to ask for forgiveness; but you should ask for a raise ;)
- if your code is not older than you are.. then its not legacy.


### How the smuggling trade works ###

- as a business analyst need to take responsibility for hundred of thousands of transactions and changes to loans
- very test intensive process
- company had 0 automatic testing process

#### Step 1 ####

- get the data
- ensure your using appropriate indexes
- system could not be changed AT ALL
- x20 manual queries needed to be imported.. into excel... per load.... 200000 loans

#### Step 2 ####

- formatting: pivots everywhere

#### Step 3 ####
- format only step that has business value

#### Downsides ####

- really slow
- mind numbing
- really really slow
- inconsistent
- sloooow
- lots of room for error..
- and yes did i mention it was really slow

### How to fix ###

- no admin rights... use "portable python" and ensure the manager cant see it
- DB2... how to get a driver... well ibm-db ibm actually made a wrapper
- openpyxl

## Take aways ###

- Fail Early.. adn Fail silently!
- know your problem
- people are fiddley about their own work.. dont tell people that you can do it better faster and less error prone
- do it for yourself first!
- do it on your own time.... at first
- this is important cos if the company loses money because of a prototype..... very important
- Low hanging fruit first.. choose something easy
- Don't over-reach
- ALWAYS .. measure the value.. managers love metrics.. show stats on time saved numbers crunched errors found and fixed etc... numbers numbers numbers
- if you cost the company nothing they will not complain.. and your life gets slowly better
- involve your colleagues.. SLOWLY.. and selectively
- be patient... let it grow.. and honest.. if asked... then tell... but humbly
- if they are REALLY against it and no rational explanation works.... well maybe its time to reconsider your place of work
- remember.. this is about making your manager look good.... and if it works.. it will flow down..
- no backstabbing be honest always
