ToDo
====

Issues
------
* Unify slug and ID to a single field. CHeck on inventory.
* Reconsider TableScanCache linking to factory.
  https://stackoverflow.com/questions/7336802/how-to-avoid-circular-imports-in-python

High-Level Features
-------------------
* Background worker daemon with queuing
* Add authentication to redis and zookeeper
* User Preferences, specifically quantity units

Frontend
--------
* Components
  * Naming convention on component files (and structure)
  * Components to Objects mapping
  * How to structure components? (Viewport, Breadcrumb, etc)
  * Relative vs Absolute imports
  * React/Material tags or HTML? 
  * What the fuck? https://material-ui.com/components/tabs/
* Major Features
  * Are views components? How to orchestrate a "page".
  * State tracking, routes
  * Swagger API client
* Definitions: React vs Angular
* What other UI kits exist besides Material and Bootstrap
* React/JS General
  * let, const, var - for loop
  * Does key have to be globally unique? Generate random value?
  * async

API Functions
-------------
* GET /api/v1/cocktails/martinez/rail-stop (specify a slug and limit the output?)

Test Cases
----------
* InventoryItem CRUD

Low-Priority
------------
* Consider SQLAlchemy validators? https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
* some way for custom/unknown bottles to be tracked in inventory

Tortuga Data
------------
* Do sanity check on units and see if there is any consistency that needs to be enforced.
* Actually do tags (need seperate object, i'm ignoring them for now in the factory)
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families
* ABV
* Field for type of ice

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.
* "make me something" spin the wheel. Dice + Coin? Roll a base and 
  flip for refreshing/boozy. Slider for creation complexity (aka ingredient counts)
* Recommend drinks to friends. Fuck is this turning into a social thing?
* Cache invalidation via queue, Cassandra-esque read-repair for update?
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?
* Proof Calculation (requires ABV for ingredients)
