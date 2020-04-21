ToDo
====

Code
----
* Implement some nesting of serializers to cover slug/displayname. Generic module for those? include Text there too.
* Pull parent calculation out of drink GETing? Should only need for index.
* Prevent empty []'s from getting stored in the database
* Import tree should drop index
* Cocktail API model - set required fields.
* Make API creation actually a thing. (also need ingredients)
* Refactor import commands to use API endpoints instead.
* Clean up factory methods.
* Implement images

* Make proper ElasticSearch index models
* Move ingredient validator code from model to dedicated validator framework
* auto-generate instructions?
* Tests 

API Functions
-------------


Data Model
----------
* Rip out status
* Collections (based on book, bar, something)
* Actually do tags
* Servings

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.
* "make me something" spin the wheel