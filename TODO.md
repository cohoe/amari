ToDo
====

High-Level Features
-------------------
* Collections (browse by "source")
* User Identity
  * Drink Lists (also do flagged as a list)
  * Inventory

Code
----
* MixologyTech Connector and recipe scraper
* Build a container image (or at least a Dockerfile) - maybe s2i?

* Refactor import commands to use API endpoints instead.
* switch POST ingredients to single not list.

#### Low-Priority
* Clean up factory methods.
* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 

API Functions
-------------

Data Model
----------
* Parse Upneat scrapes
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