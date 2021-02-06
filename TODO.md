ToDo
====

Issues
------
* Resolutions need to try lookup from Search first
* SpecResultionSummary, Resolution, and all that junk needs better class
  naming. Keep getting confused on what is supposed to go where.
  Components field should maybe be renamed too?
* SearchService abstraction and cleanup TODOs around exceptions.
* Cache the inventory/recipes endpoint. This may negate the need to look
  up the searchable version.

High-Level Features
-------------------
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* InventoryValidator
* some way for custom/unknown bottles to be tracked in inventory
* Notebook (all Notes, similar to Biblio)

API Functions
-------------
* /inventory/{id}/suggestions(increase?): Suggest common ingredients youre missing
* /inventory/{id}/statistics (counts, recipes-available)
* /construction/{slug}

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