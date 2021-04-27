ToDo
====

Work Queue
----------
* Search box
* /cocktails scrolling is broken on mobile.

Backend Work
------------
* Add auto-generated spec description based on closest ingredient parent. Example:
  "Dead Rabbit Irish Whiskey, Simple Syrup" -> "Irish Whiskey, Simple Syrup"
  Might have to factor in customs here? Or maybe they should count?
* Some kind of standardized auto-generated origin summary.

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
* Things to review:
  * Calculating "active" (ScrollPane/ContentPane routing)
    * `useLocation` hook to figure out the route and render (or not) the scrollpane)
    * Sub-routers to move all /cocktail logic into that specific component. https://reactrouter.com/web/api/Hooks/useroutematch
    * https://www.npmjs.com/package/classnames
  * More better way of props children than just `{children}`?
    * Yup, that's how you do that.
  * Worth trying to maintain some sense of h1-h7?
    * Still enforces hierarchy. Just don't worry about style. Do that yourself.
  * `index.js` - when best or always?
    * Always, unless its private
* Major Features
  * State tracking, routes
  * Swagger API client
* Useful bits
  * HideOnScroll
  * AppBar, ToolBar, LocalBar
* Random little things for later:
  * Have a dropdown or some other mechanism for selecting an inventory (or no inventory)
    to address SpecResolution.
* API Client
  * https://stackoverflow.com/questions/52237855/support-for-the-experimental-syntax-classproperties-isnt-currently-enabled
    `npm install @babel/plugin-proposal-class-properties --save-dev`
    Babelrc
    https://github.com/babel/babel/issues/8577
    https://github.com/swagger-api/swagger-codegen/issues/8024
    `java -jar swagger-codegen-cli.jar generate -i http://localhost:8080/api/swagger.json -l javascript -o ~/Projects/amari/panama/sdk`

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
