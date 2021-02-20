ToDo
====

Issues
------
* Figure out a pattern to securely update resources. Consider just doing
  a construct-n-replace vs patch-in-place. So far just in /lists/{id}/items
* CustomKind ingredients should support a recipe construct. Perhaps rebrand SpecComponent
  to Component and also utilize a list of Text objects for instructions.
* More BarbadosObject for objects

High-Level Features
-------------------
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* some way for custom/unknown bottles to be tracked in inventory
* Background worker daemon with queuing

API Functions
-------------

Low-Priority
------------
* auto-generate instructions?
* QueryCondition validator
* Consider SQLAlchemy validators? https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
* Expand validators

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
