ToDo
====

High-Level Features
-------------------
* Collections (browse by "source")
* User Identity
* Unify slug and ID to a single field. CHeck on inventory.
* Ingredient name search doesn't work on slugs (search name=mount-gay)
* create inventory validator
  * ingredient exists
* add simple inventory count attribute (inventory/stats endpoint?)
* some way for custom/unknown bottles to be tracked
* ingredients might need the same search tweaks as cocktails (barr -> barrel)

#### Low-Priority
* Clean up factory methods.
* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 
* See if there is a way to make Redis/ElasticSearch come from Registry
* Can scrapers be built for Imbibe/PUNCH/various other reliable sources?
* Rename all package files to be sane names (see Caches)
* Rename services to ThingService? (LogService, RegistryService)

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
* bitters needs more organization. bitters -> citrus -> orange
* smith cross jamaican overproof something
* syrups too

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
* Pisco / Mezcal / Calvados categories


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
