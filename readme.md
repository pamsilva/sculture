# Main difficulties
- had issues connecting to the RDS instance I created so used a localdatabase instead
- had friction handling the differences between flask and fast api.

# Achievements
- basic functionality and tests

# Would do next
- try to simplify the schemas
- streamline the db management with make files to ensure schemas were present and up to date
- would do proper error handling
- clean up the tests such that we can reset the database everytime, and the scenario setup is simpler

# notes on executing
- alembic needs to be initialized and ran after replacing the adequate sqlalchemy.url
- initialise, generate and run the migrations
- then, it should be possible to execute the tests with pytest
