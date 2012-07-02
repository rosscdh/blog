Date: 2012-07-02
Title: EuroPython2012 - Guido Van Rossum Keynote
Tags: intro, keynote, europython2012, @europython, conference
Category: EuroPython2012
Slug: EP-2012-bdfl-keynote

# The introduction #

## The hottest week of the year ##

And they are not kidding, its really hot today around 38 degrees celcius. But nevermind were in the hotel and things are hotting up.

Got lots of swag (thanks europython!) shirts mugs and things! all the goodies that come with these conferences!

The #EP people are really friendly and well organized; after picking up my badge after having to spell my surname (sorry Franchesca).

Conference is 10% bigger than last year. We have access to the 5* hotels gardens and surrounding areas with shade and ponds and things.. really nice and relaxing.

Python is also woman-friendly and are hosting a #womanslunch; the python community recognizes that more woman need to become involved in the community and we are all urged to talk with woman and try to get them involved and put an end to this man only image that programming has!

#EP also offeres a free pizza lunch! which we just need to pick tickets up for. But availability is limited so we better book our places.

Importnat to book the trainings as space in the halls is limited.

Intranet is available at #ep to allow participants to deploy and run their demos and software available to all other particippants.

Lightning talks are on offer as well, and if you wish to give one simply register and space shall be yours! As long as your Guido or at least give the correct surname!

Water is available everywhere so stay hydrated, but use your Mongodb Cup.

Weekend sprints are a go as well as coding competitions.

## Guido BDFL KeyNote - all about the trolls ##

Thanks to the python software foundation; logos of osf in coffee (lady in japan) gitlatte.com ?

Completely adlib of his previous talk. Please excuse contradictions if any.

Trolls exist and often crop up at inopportune times. 

Is it not hard to deal with:

- Horrible language that has GIL
- Horrible tabs
- Many silly but also interesting questions that comes from the Trolls

Tip for dealign with Trolls

- Do not engage, they go away eventually

_* Whitespace *_

- Unusual at first, but after a while you will love it

_* Python sucks ruby rules *_

- Ruby people tend to say this loudedst and longest
- but generally the same argument can be applied to any other dynamic language
- all arguments are invalid.. as well as vice versas, "one time at our org we had a very slow python app that was replace with much faster java".. ok fair enough but the same applies jsut as often in the reverse case.
- remember from 30000 feet all dynamic languages are more or less the same; same similar problems, communities, commercial interests etc.. all dynamic languages are in the same boat.
- introspection is the key to everything and all languages make the internal workings of the language available (except c...)
- static language proponents are activly trying to find ways to bridge between static and dynamic (like google dart)
- dart allows optional static binding to dynamic and vice versa

_*When will you admit python3 is a mistake*_

- p3 is **not** a mistake
- more people are still using p2.x and nto p3; but more than he expected.
- knew that py3k would take ages to get traction
- but it gets better every year. i.e. numpy has excellent support but a year ago it was very shaky in terms of support but now they are all in!
- the port of nnupy took effort.... but it was actually not that big a deal!
- constant iterative process, conversion will take some time.
- some customers are *tied* or at least think they are tied to p2.* how do we support them?
- there are a num of strategies to support both 2. and 3k at the same time
- 1 compromise was made in p3k.. string literals prefixed with u u'unicode yay' are *STILL* supported in p3k
- this has been done to allow better support for 2.x python in th p3k future
- is worh getting into p3k because there _will_ be a requirement in teh future from your friends
- because its human nature to want the latest greatest and of course the buzzwords for managers will use p3k
- change sucks, humans hate change and most often the benefits are not obvious to the user; but in a year or two they will think it was silly to make such a fuss

_* PyPy - what is going on, why the delay *_

- Guido does not belive pypy is always better; 
- compat problems, but he is glad they are doing it and taking compat problems so seriously
- they are making it better every iteration and its great and faster
- most systems are dependant on legacy modules and cant simply switch to pypy
- still a moving project; but Guido things its doing a great job and would be happy if it took over has preferred python implemntatio but they need tosort out the p3k issue

_* Dynamic typing troll *_

- used to be tought that static typing was better than dynamic as static would find bugs at compile time rather than runtime
- puritinisim is a sin in itself.. dont be overstrict.. its btter to produce something than let the purity argumetn get in the way.
- make it, refine it, make it better
- pragmatisim over puritinism

_* Python is too slow for real work *_

- n00b statement; 
- compilers are not always the key, dynamic langauges are dynamic for a reason
- the static python compiler is a pipe dream but keep at it maybe someone gets lucky :)
- youtube runs entirely on python (except video encoder codex obviously)... not fast enough? are you serious?

_* The GIL *_

- problem arises from old legacy timeshare problem which has now changd due to new modern hardware
- there are indeed strategies for handeling this problem, but its hard

- python in browser.. cant do it.. but its political and not technical
- python in android.. cant do it.. but its political and not technical
- lambda is NOT broken its great
- Guido loves functional but io in functional is a problem, at least for him.
- Garbage collection, forget about it its all an intellectual excercise;
- Additional language features.. very selective.. as every new feature adds to the learning curve; and python is meant to be simple and elegant; import this

_* Questions *_

- will GAE ever support p3k? : Thats a question for google.
