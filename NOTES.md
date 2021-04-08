Notes
=====

Database
--------
Cannot take substantial advantage of SQLAlchemy Relationships since I don't
have dedicated columns to a lot of useful things. For example, the number one
use case of this would be to guarantee an Ingredient exists. This would prevent
RECREATE actions on it due to the foreign key relationship. Also because I don't
have a column for spec.components I can't refer to it anyway. This is cheated
and implemented in the validator (CocktailModelValidator) to ensure that the
ingredient exists.

AWS Aurora Serverless provides on-demand Postgres-compatible database which
is an intriguing proposition. I think having hopes and dreams of DynamoDB are
going out the window. It's all a moot point until the free tier of ElasticSearch
becomes not-12-months.

Examples
--------
Constructions has the latest pattern for good API endpoints including
docs and return codes.

Caches
------
Should tablescans be eliminated in favor of Flask request caching? I feel
like yes but I don't have a good way to do this yet. Also can't directly
associate caches with factories because the cache requires the factory.

Authentication
--------------
Doing it myself with Flask-Security[-Too] requires managing User and Role models,
handling sign-up and account confirmation, ensuring against abuse of the register
endpoint, managing credentials, sending confirmation emails, and all sorts of
other stuff like that. Auth0 was the easiest to integrate with but does not support
any kind of RBAC on the free tier. AWS Cognito is a hot mess of documentation (or
lack thereof) but is the free-est of the solutions. After going back and forth
a flow diagram would have helped me deal with a lot of the architectural challenges
way earlier and saved myself a ton of work.

What I ended up with is that user registration/confirmation/signin is handled
by Cognito. My API returns some redirects to the appropriate login/logout URLs
hosted in AWS. Login spits back a JSON Web Token (JWT) which my web application
which does not exist yet can store and place in an HTTP request header for each
API request that needs the token (X-Jamaica-Authorization). RBAC is handled in
Cognito. Memberships can be managed via future API endpoints in Jamaica talking
directly to the Cognito management API. This solution has the advantage of offloading
all the security-bullshit to Cognito and simply honoring/trusting the tokens that it
generates. Note that tokens cannot be revoked after they are issued (only on expire).

Frontend Development
--------------------
Random notes from talks with Ben:
* Working out UI flows in a wireframe tool such as Figma/Balsamiq/Draw.io will save
  a lot of headache later. This turned out to be true because I had no idea what
  I wanted this thing to look like. I still don't, but at least I can visualize it.
* Literally everything should be a component. UpperCase component names. Absolute
  imports are a lot harder to do than I feel they should be, so I'm stuck with relative
  hell. Use React/Material tags rather than straight HTML. Saves hassle later on.
  I should be able to map components to Barbados Objects. Under no circumstances do
  class inheritance in components. See https://reactjs.org/docs/composition-vs-inheritance.html
* Certain Material documentation is garbage. see https://material-ui.com/components/tabs/
* Jamaica v2.0 can be GraphQL based. No way am I spiritually prepared to re-write the
  entire API yet.
* `setThing()` functions are async, and you just gotta deal with it. Having multiple
  `useEffect()`'s are OK (including when they do a simple `if ($thing) {} return`)
* Keys in a mapping context need to be unique within their scope, not globally. Phew!
* `const` == unchanging, `let` == changing
* useStyles/makeStyles is a Material thing for defining CSS in JS. Resultant classes
  are component-specific so that's nice.
* React Fragments (`<>`, `<React.Fragment`) let you shortcut the React requirement
  to return a single element from a component but still have things adjacent.
* CssBaseline, useTheme also a Material thing.
* Redux is way too heavy for me right now. Should be able to get away with using React
  Contexts instead.
* You can build with `npm run build`.
* React-Router (URLs hold all data). Routers can be sharded like the API namespaces in Flask. 
* React-Query (Better loading management, caching, etc) https://react-query.tanstack.com/overview
* Formik (form editing/posting/etc)

Sizing of device styles:
* xs == Phone
* sm == Tablet
* md == Desktop