ToDo
====

Deployment
----------
* Kibana password
* Operator or at least persistent configs
* Finish London

High-Level Features
-------------------
* Collections (browse by "source")
* User Identity
  * Inventory
* Change env var names because Kubernetes steps on us

Code
----
* Build a container image (or at least a Dockerfile) - maybe s2i?

#### Low-Priority
* Clean up factory methods.
* Make proper ElasticSearch index models
* auto-generate instructions?
* Tests 

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
