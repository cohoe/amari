ToDo
====

Issues
------
* Need some kind of better exception for when an object cannot be built
  SpecFactory is using ValidationException. Not sure that's a good thing.
* Missing construction triggers exception on GET if deleted (example, delete
  stir then get martinez). Find a way to represent this error at a 500 level.

High-Level Features
-------------------
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* some way for custom/unknown bottles to be tracked in inventory
* Notebook (all Notes, similar to Biblio)
* Search by arbitrary text (no specific fields)

API Functions
-------------
* /inventory/{id}/suggestions(increase?): Suggest common ingredients youre missing
* /inventory/{id}/statistics (counts, recipes-available. aka InventoryReport obj)

Low-Priority
------------
* Factory Cleanup
  * Refactor the old factories to the new (inventory) style
  * See about using ObjectIndexer in the obj_to_index() calls.
  * Move "all" factories under factories. This includes indexes, indexers, etc.
* auto-generate instructions?
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?
* More BarbadosObject for objects
* QueryCondition validator
* Consider SQLAlchemy validators? https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
* Can I use SQLAlchemy relationships?
* Expand validators

Tortuga Data
------------
* Actually do tags
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families
* list(Image(href, text, credit))

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
* Tests