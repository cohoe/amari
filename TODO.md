ToDo
====

Work Queue
----------
* Formik for forms.
* Make a GoGoGo not reload the page. Should be able to update and intercept in JS.
* Consider adding lists functionality.
* Instance of Jamaica to Columbia.

Backend Work
------------
* Search
  * Search endpoint for no customs.
  * Support multiple construction options.
  * Move search endpoints to `/api/v1/search/${resource}`.
* Add auto-generated spec description based on closest ingredient parent. Example:
  "Dead Rabbit Irish Whiskey, Simple Syrup" -> "Irish Whiskey, Simple Syrup"
  Might have to factor in customs here? Or maybe they should count?
* Some kind of standardized auto-generated origin summary.
* Changing the tree doesn't regenerate all resolutions.
* First run of a report needs to resolve all recipes otherwise you get a bogus
  report contianing not much.
* Add metric to report for which ingredients would enable the most recipes.
  I'm pretty sure leaderboard is just count of missing.

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
* Major Features
  * State?
  * Swagger API client
* Useful bits
  * HideOnScroll
  * AppBar, ToolBar, LocalBar
* Random little things for later:
  * Have a dropdown or some other mechanism for selecting an inventory (or no inventory)
    to address SpecResolution.
  * "Random" button for random result from list (also limits scope to search).
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
* Restructure liqueur factoring in the imbibe article
* Do sanity check on units and see if there is any consistency that needs to be enforced.
* Actually do tags (need seperate object, i'm ignoring them for now in the factory)
* Ingredient Descriptions - semi auto-generate.
* Servings (single, multi, batch)
* Parse Upneat and MixTech scrapes (blehhhhh)
* "original" specs should not exist.
* More families
* ABV
* Field for type of ice
