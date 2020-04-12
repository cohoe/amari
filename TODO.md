ToDo
====

Code
----
* Couple last models to build for the api endpoints that dont have them.
* Consider replacing "components" with "ingredients" and figuring out a way to 
  keep them all straight.
* Notes is double text fielding. Suspect bad import to the database. (la-conferencia)
* Move ingredient validator code from model to dedicated validator framework
* auto-generate instructions?
* Tests
* Split Search views of objects vs Database (parents not in DB but in Search)

API Functions
-------------
* Search by drink name or ingredient
* "make me something" spin the wheel

Data Model
----------
* Collections (based on book, bar, something)

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.