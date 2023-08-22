import os
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database, drop_database
from opencdms.adapters import opencdmsdb


# set connection details
UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]
DBHOST = os.environ["POSTGRES_HOST"]
DBPORT = os.environ["POSTGRES_PORT"]

engine = create_engine(f"postgresql+psycopg2://{UID}:{PWD}@{DBHOST}:{DBPORT}/{DBNAME}", echo=True)
# check whether we want to start clean
CLEAN = True
if CLEAN:
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

with engine.begin() as conn:
    # Create schema
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS admin"))
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS reference_data"))
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS master_data"))
    # Add PostGIS extension
    conn.execute(text("CREATE EXTENSION Postgis;"))

# create tables
opencdmsdb.mapper_registry.metadata.create_all(engine)

# disconnect
engine.dispose()
