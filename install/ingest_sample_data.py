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
    "cdm.observation": ["CA_6016527_1990.csv",
                        "CA_6016527_1991.csv",
                        "CA_6016527_1992.csv",
                        "CA_6016527_1993.csv",
                        "CA_6016527_1994.csv",
                        "CA_6016527_1995.csv",
                        "CA_6016527_1996.csv",
                        "CA_6016527_1997.csv",
                        "CA_6016527_1998.csv",
                        "CA_6016527_1999.csv",
                        "CA_6016527_2000.csv",
                        "CA_6016527_2001.csv",
                        "CA_6016527_2002.csv",
                        "CA_6016527_2003.csv",
                        "CA_6016527_2004.csv",
                        "CA_6016527_2005.csv",
                        "CA_6016527_2006.csv",
                        "CA_6016527_2007.csv",
                        "CA_6016527_2008.csv",
                        "CA_6016527_2009.csv",
                        "CA_6016527_2010.csv",
                        "CA_6016527_2011.csv",
                        "CA_6016527_2012.csv"],
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

