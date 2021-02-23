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