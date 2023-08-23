import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from opencdms.adapters import opencdmsdb

# set connection details
UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]
DBHOST = os.environ["POSTGRES_HOST"]
DBPORT = os.environ["POSTGRES_PORT"]
DATADIR = os.environ["OPENCDMS_SAMPLE_DATA"]

engine = create_engine(f"postgresql+psycopg2://{UID}:{PWD}@{DBHOST}:{DBPORT}/{DBNAME}", echo=True)

opencdmsdb.start_mappers()

session = sessionmaker(bind=engine)()
cursor = session.connection().connection.cursor()

admin_tables = {
    "admin.user": "user.csv"
}

for key, value in admin_tables.items():
    with open(f"{DATADIR}/admin/{value}") as fh:
        cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS ',' NULL AS 'NULL' QUOTE E'\\''", fh)

code_tables = {
    "reference_data.status": "status.csv",
    "reference_data.altitude": "altitude.csv",
    "reference_data.application_area": "application_area.csv",
    "reference_data.climate_zone": "climate_zone.csv",
    "reference_data.communication_method": "communication_method.csv",
    "reference_data.equipment_type": "equipment_type.csv",
    "reference_data.exposure": "exposure.csv",
    "reference_data.facility_type": "facility_type.csv",
    "reference_data.feature_type": "feature_type.csv",
    "reference_data.geopositioning_method": "geopositioning_method.csv",
    "reference_data.local_topography": "local_topography.csv",
    "reference_data.measurement_quality": "measurement_quality.csv",
    "reference_data.media_type": "media_type.csv",
    "reference_data.observation_type": "observation_type.csv",
    "reference_data.observed_property": "observed_property.csv",
    "reference_data.observing_method": "observing_method.csv",
    "reference_data.observing_procedure": "observing_procedure.csv",
    "reference_data.observing_program": "observing_program.csv",
    "reference_data.operating_status": "operating_status.csv",
    "reference_data.reference_surface": "reference_surface.csv",
    "reference_data.relative_elevation": "relative_elevation.csv",
    "reference_data.reporting_status": "reporting_status.csv",
    "reference_data.representativeness": "representativeness.csv",
    "reference_data.role": "role.csv",
    "reference_data.source_of_observation": "source_of_observation.csv",
    "reference_data.source_type": "source_type.csv",
    "reference_data.surface_cover": "surface_cover.csv",
    "reference_data.surface_roughness": "surface_roughness.csv",
    "reference_data.territory": "territory.csv",
    "reference_data.time_zone": "time_zone.csv",
    "reference_data.topographic_context": "topographic_context.csv",
    "reference_data.wmo_region": "wmo_region.csv"
}

for key, value in code_tables.items():
    with open(f"{DATADIR}/reference_data/{value}") as fh:
        cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS ',' NULL AS 'NULL' QUOTE E'\\''", fh)

session.commit()
session.close()

