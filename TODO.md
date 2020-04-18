ToDo
====

Code
----
* Build crazy complex cocktail model
* Consider replacing "components" with "ingredients" and figuring out a way to keep them all straight.
* Move ingredient validator code from model to dedicated validator framework
* Ensure validate happens before insert into database or index
* Import recipes needs to invalidate cache like ingredients does
* auto-generate instructions?
* Tests
* Move database connection config to the Config service.

API Functions
-------------
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