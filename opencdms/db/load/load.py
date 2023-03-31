# Initial load command used by `opencdms db load`
# Note that this command makes a lot of assumptions about the
# data to load and needs improvements
#
# opencdms install
# opencdms db start
# opencdms db load /workspaces/opencdms-test-data/data/cdm/`  # creates db it not exists
#
import csv
# TODO: replace with imports from CDM model
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy.engine import Engine

from opencdms.adapters import opencdmsdb
from opencdms.db.config import get_connection_string, get_engine
from opencdms.utils.db import DatabaseError
from opencdms.utils.db.postgres import create_db_and_schemas
from opencdms.utils.paths import base_path


DEFAULT_DATA_PATH = base_path('../../opencdms-test-data/data/cdm/')


def create_model(engine):
    """ Create model """
    # TODO: What it the model already exists??
    opencdmsdb.start_mappers()
    opencdmsdb.mapper_registry.metadata.create_all(engine)


def load_data():
    """ Load sample data """
    connection_string = get_connection_string('CDM')
    cdm_engine = get_engine()

    create_db_and_schemas('opencdmsdb', ['cdm'], connection_string)
    try:
        create_db_and_schemas('opencdmsdb', ['cdm'], connection_string)
    except DatabaseError:
        pass

    create_model(cdm_engine)

    # Load data from CSV
    #    code_tables
    #    data_tables
    #    hosts.geojson

    with cdm_engine.connect() as conn:
        result = conn.execute("SELECT * FROM cdm.observation")
        for row in result:
            print(row)


def load_csv_to_db(csv_file_path: str, engine: Engine, table_name: str, headers: list):
    """
    Loads data from a CSV file into a database table using SQLAlchemy.

    Args:
        csv_file_path (str): The file path to the CSV file.
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object to use for the database connection.
        table_name (str): The name of the table to insert the data into.
        headers (list): A list of column names in the CSV file.

    Returns:
        None
    """
    # create metadata object
    metadata = MetaData()

    # create table object
    # TODO: get this from cdm model
    table = Table(table_name, metadata, *[Column(name, String) for name in headers])

    # load data from csv file
    with open(csv_file_path, 'r') as f:
        conn = engine.connect()
        conn.execute(table.insert(), [row for row in csv.DictReader(f)])

    # commit changes
    conn.close()


__all__ = ['DEFAULT_DATA_PATH', 'create_model', 'load_data', 'load_csv_to_db']
