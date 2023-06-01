import os
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker

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
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS cdm"))
    # Add PostGIS extension
    conn.execute(text("CREATE EXTENSION Postgis;"))

# create tables
opencdmsdb.mapper_registry.metadata.create_all(engine)

opencdmsdb.start_mappers()

session = sessionmaker(bind=engine)()
cursor = session.connection().connection.cursor()

code_tables = {
    "cdm.user": "user.csv",
    "cdm.status": "status.csv",
    "cdm.observation_type": "observation_type.csv",
    "cdm.facility_type": "facility_type.csv",
    "cdm.feature_type": "feature_type.csv",
    "cdm.wmo_region": "wmo_region.csv",
    "cdm.territory": "territory.csv",
    "cdm.observed_property": "observed_property.csv",
    "cdm.observing_procedure": "observing_procedure.csv",
    "cdm.time_zone": "time_zone.csv",
    "cdm.source_type": "source_type.csv",
    "cdm.media_type": "media_type.csv",
    "cdm.climate_zone": "climate_zone.csv",
    "cdm.surface_cover": "surface_cover.csv",
    "cdm.surface_roughness": "surface_roughness.csv",
    "cdm.topography": "topography.csv",
    "cdm.season": "season.csv",
    "cdm.programme": "programme.csv",
    "cdm.observing_method": "observing_method.csv",
    "cdm.exposure": "exposure.csv",
    "cdm.reference_surface": "reference_surface.csv",
    "cdm.role": "role.csv"
}
# note, order is important
data_tables = {
    "cdm.host": ["hosts.csv"],
    "cdm.source": ["source.csv"],
    "cdm.observer": ["observer.csv"],
    "cdm.deployment": ["deployment.csv"],
    "cdm.observer_characteristics": ["observer_characteristics.csv"],
    # "cdm.observation": ["CA_6016527_1990.csv"],
    "cdm.feature": ["features.csv"]
}

for key, value in code_tables.items():
    with open(f"/local/app/data/code_tables/{value}") as fh:
        cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'", fh)

for key, value in data_tables.items():
    if isinstance(value, list):
        for item in value:
            with open(f"/local/app/data/data_tables/{item}") as fh:
                cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'", fh)
    else:
        with open(f"/local/app/data/data_tables/{value}") as fh:
            cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'", fh)

session.commit()
session.close()

