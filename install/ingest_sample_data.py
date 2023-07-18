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

# note, order is important
data_tables = {
    "cdm.host": ["hosts.csv"],
    "cdm.source": ["source.csv"],
    "cdm.observer": ["observer.csv"],
    "cdm.deployment": ["deployment.csv"],
    "cdm.observer_characteristics": ["observer_characteristics.csv"],
    "cdm.observation": ["CA_6016527_1990.csv"],
    "cdm.feature": ["features.csv"]
}

for key, value in data_tables.items():
    if isinstance(value, list):
        for item in value:
            with open(f"{DATADIR}/data_tables/{item}") as fh:
                cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'", fh)
    else:
        with open(f"{DATADIR}//data/data_tables/{value}") as fh:
            cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'", fh)

session.commit()
session.close()

