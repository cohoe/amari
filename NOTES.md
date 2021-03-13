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
