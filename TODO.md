ToDo
====

Code
----
* Implement some nesting of serializers to cover slug/displayname. Generic module for those? include Text there too.
* Deprecate spec_count? Maybe make an Object property instead of an actual data field?
* Unify spec_component and garnish objects
* Pull parent calculation out of drink GETing? Should only need for index.
* Prevent empty []'s from getting stored in the database

* Move ingredient validator code from model to dedicated validator framework
* auto-generate instructions?
* Tests 

API Functions
-------------
* "make me something" spin the wheel

Data Model
----------
* Citation has notes?
* Rip out status
* Convert author to authors and enforce list
* Collections (based on book, bar, something)
* Actually do tags

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.