ToDo
====

Issues
------
* Importers are skipping the Jamaica serializers by directly creating via
  the factory. These should be re-worked to dump straight into the API (like
  create/delete/recreate are) to catch more source data issues.
* Citation needs a year field to deal with the date vs year bullshit

* TextFactory
* Parser library for common data types. Need to work out relationship between
  factories and parsers for complex objects (ie, ones that need a raw_to_obj()).

High-Level Features
-------------------
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* some way for custom/unknown bottles to be tracked in inventory
* Notebook (all Notes, similar to Biblio)
* Search by arbitrary text (no specific fields)
* Background worker daemon with q21ueuing

API Functions
-------------
* GET /inventory/{id}/suggestions(increase?): Suggest common ingredients youre missing
  Maybe merge this as part of the report below?
* GET /inventory/{id}/report (counts, recipes-available. aka InventoryReport obj)

Low-Priority
------------
* Factory Cleanup
  * Refactor the old factories to the new (inventory) style
  * Combine and re-use common parser functions in BaseFactory.
    Might need to move these into a seperate object after all
    if I want to take advantage of factories that call other
    factories.
* auto-generate instructions?
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
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?