ToDo
====

* Somewhere I've broken implicit resolution. daiquiri says implicit
  for lime-juice when I definitely don't have it in the inventory
  on purpose.
* indexes should imply their elements.

Issues
------
* Cleanup inventory endpoints
  * unify resolve under inventory recipes endpoint.
  * shard the inventories/recipes endpoints into more manageable classes.
* Enhance importers
  * --delete needs to be specific and not the entire thing, unless that swhat you want
  * Counts of adds, duplicates, etc (for ingredients)
* Fix rebuilding of inventoryspecresolution entries.
* Add garnish, citation* to the resolution
* Search name='oaxaca-old-fashioned' fails (dashes?)
* Convert tree data to an object rather than dictionary.
  Helps with some Treelib components

High-Level Features
-------------------
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* InventoryValidator
* some way for custom/unknown bottles to be tracked in inventory
* Notebook (all Notes, similar to Biblio)

API Functions
-------------
* /inventory/{id}/recipes/{id}: Specific recipe resolution
* /inventory/{id}/suggestions(increase?): Suggest common ingredients youre missing
* /inventory/{id}/statistics (counts, recipes-available)
* /construction/{slug}

#### Low-Priority
* Factory Cleanup
  * Refactor the old factories to the new (inventory) style
  * See about using ObjectIndexer in the obj_to_index() calls.
  * Move "all" factories under factories. This includes indexes, indexers, etc.
* auto-generate instructions?
* Tests 
* See if there is a way to make Redis/ElasticSearch come from Registry
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?
* More BarbadosObject for objects
* QueryCondition validator

Tortuga Data
------------
* elderflower, flower, violette are not a thing
* syrups too (what did this mean????)
* Actually do tags
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families

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
