ToDo
====

Issues
------
* Unify slug and ID to a single field. CHeck on inventory.
* some way for custom/unknown bottles to be tracked in inventory
* Should cache invalidation be handled in the factory insert/update/delete calls?

High-Level Features
-------------------
* User Identity
* Background worker daemon with queuing

API Functions
-------------

Low-Priority
------------
* Consider SQLAlchemy validators? https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators

Tortuga Data
------------
* Actually do tags (need seperate object, i'm ignoring them for now in the factory)
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families
* ABV

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
