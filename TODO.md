ToDo
====

High-Level Features
-------------------
* Collections (browse by "source")
* User Identity
* Inventory
* Finish re-indexing endpoint
* Unify all object contruction via the factory
  * model = thing & c = model_to_obj() calls
  * Mostly affects deletes.
  * Remove all calls to models in Jamaica?
* Remove valueerror -> keyerrors

#### Low-Priority
* Clean up factory methods.
* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 
* See if there is a way to make Redis/ElasticSearch come from Registry
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?

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

API Functions
-------------

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
