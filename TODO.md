ToDo
====

Code
----
* Build a container image (or at least a Dockerfile)
* Implement some nesting of serializers to cover slug/displayname. Generic module for those? include Text there too.
* Cocktail API model - set required fields.
* Create ingredients by API
* Refactor import commands to use API endpoints instead.
* Clean up factory methods.

* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 

API Functions
-------------
* cache /cocktails and eliminate index

Data Model
----------
* Collections (based on book, bar, something)
* Actually do tags
* Servings
* "original" specs should not exist.

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.
* "make me something" spin the wheel
* Recommend drinks to friends. Fuck is this turning into a social thing?