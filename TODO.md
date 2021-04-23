ToDo
====

Work Queue
----------
* Some kind of standardized auto-generated origin summary. Maybe make this part of the API?
* Race condition with rendering <Spec> where the spec var isnt there yet. useEffect?
* ContentPane toolbar with buttons and stuff (back to list, previous/next, display settings?)
* Search box

Backend Issues
--------------

High-Level Features
-------------------
* Background worker daemon with queuing
* Add authentication to redis and zookeeper
* User Preferences, specifically quantity units
* Unify slug and ID to a single field. Check on inventory.
* Reconsider TableScanCache linking to factory.
  https://stackoverflow.com/questions/7336802/how-to-avoid-circular-imports-in-python

Frontend
--------
* Questions
  * https://stackoverflow.com/questions/52237855/support-for-the-experimental-syntax-classproperties-isnt-currently-enabled
    `npm install @babel/plugin-proposal-class-properties --save-dev`
    Babelrc
    https://github.com/babel/babel/issues/8577
    https://github.com/swagger-api/swagger-codegen/issues/8024
    `java -jar swagger-codegen-cli.jar generate -i http://localhost:8080/api/swagger.json -l javascript -o ~/Projects/amari/panama/sdk`
  * What is clsx and useTheme?
  * Calculate grid spacing and stuff based on media query
  * `<div className={classes.scrollPane + ' ' + classes.scrollPaneInactive}>` Simplify this
* Major Features
  * State tracking, routes
  * Swagger API client
* Useful bits
  * HideOnScroll
  * AppBar, ToolBar, LocalBar, Typography
* Random little things for later:
  * Have a dropdown or some other mechanism for selecting an inventory (or no inventory)
    to address SpecResolution.
  * Add auto-generated spec description based on closest ingredient parent. Example:
    "Dead Rabbit Irish Whiskey, Simple Syrup" -> "Irish Whiskey, Simple Syrup"
    Might have to factor in customs here? Or maybe they should count?

API Functions
-------------
* GET /api/v1/cocktails/martinez/rail-stop (specify a slug and limit the output?)

Test Cases
----------
* InventoryItem CRUD

Low-Priority
------------
* Consider SQLAlchemy validators? https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
* some way for custom/unknown bottles to be tracked in inventory

Tortuga Data
------------
* Do sanity check on units and see if there is any consistency that needs to be enforced.
* Actually do tags (need seperate object, i'm ignoring them for now in the factory)
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families
* ABV
* Field for type of ice

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
