ToDo
====

Issues
------
* Cleanup inventory endpoints
  * unify resolve under inventory recipes endpoint.
  * shard the inventories/recipes endpoints into more manageable classes.
* alpha and counts and new stuff isn't in the /recipes endpoint.
* fail validation on crappy glassware
* Enhance importers
  * --delete needs to be specific and not the entire thing, unless that swhat you want
  * Counts of adds, duplicates, etc
* Fix rebuilding of inventoryspecresolution entries.
* Make redis come from the registry, and add to init process.

High-Level Features
-------------------
* Collections (browse by "source")
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* InventoryValidator
* some way for custom/unknown bottles to be tracked in inventory
* Notebook (all Notes, similar to Biblio)
* Rebrand Menu to Lists, make ID driven

API Functions
-------------
* /inventory/{id}/suggestions(increase?): Suggest common ingredients youre missing
* /inventory/{id}/statistics (counts, recipes-available)

#### Low-Priority
* Clean up factory methods.
* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 
* See if there is a way to make Redis/ElasticSearch come from Registry
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?
* Can ObjectSerializer be removed from barbados.objects and use the serializer param instead?
* More BarbadosObject for objects
* Implement reconnect for services with connections?

Deployment
----------
* Kibana password
* Operator or at least persistent configs
* Different ConfigMaps for Init vs Jamaica runtime
* Scale various components

Tortuga Data
------------
* Some TODOs in there about the structure (mezcal, agricole, etc)
* aged jamaica rum 
* is recipe slug actually being used
* make indexes query based on attributes
* ingredient origin attributes?
* elderflower, flower, violette are not a thing
* smith cross jamaican overproof something
* syrups too
* Cocktail vs Punch vs Shot???
* Pisco / Mezcal / Calvados categories
* vermouth

Data Model
----------
* Parse Upneat and MixTech scrapes (blehhhhh)
* Collections (based on book, bar, something)
* Actually do tags
* "original" specs should not exist.
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)

Future Ideas
------------
* Interactive drink builder. Start with a template, and swap out different
  components. Split things, maybe some ML to make suggestions?
* Purchase tracker. Log your purchases to generate an average cost. Maybe
  also have a price logger? Focus on the first one.
* "make me something" spin the wheel. Dice + Coin? Roll a base and 
  flip for refreshing/boozy. Slider for creation complexity (aka ingredient counts)
* Recommend drinks to friends. Fuck is this turning into a social thing?
* Package and Deploy to CSH Openshift (Operator???)
* Cache invalidation via queue, Cassandra-esque read-repair for update?
