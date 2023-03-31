# Initial load command used by `opencdms db load`
# Note that this command makes a lot of assumptions about the
# data to load and needs improvements
#
# opencdms install
# opencdms db start
# opencdms db load /workspaces/opencdms-test-data/data/cdm/`  # creates db it not exists
#
import csv
import glob
import os
from typing import Dict

from sqlalchemy import text, Table
from sqlalchemy.engine import Engine

from opencdms.adapters import opencdmsdb
from opencdms.db.config import get_connection_string, get_engine
from opencdms.utils.db import DatabaseError
from opencdms.utils.db.postgres import create_db_and_schemas
from opencdms.utils.paths import base_path
from opencdms.utils.db.postgres import launch_psql

from .csv import header_mapping


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

    file_pattern = os.path.join(DEFAULT_DATA_PATH, 'data_tables/CA_*.csv')
    for file_name in glob.glob(file_pattern):
        # load_csv_to_cdm(file_name, cdm_engine, opencdmsdb.observation,
        #                 delimiter='|', header_mapping=header_mapping,
        #                 null_value='NA', quote_char="'")

        # TODO:
        raise ValueError('Resume here')
        load_csv_to_cdm()
        break

    # Load data from CSV
    #    code_tables
    #    data_tables
    #    hosts.geojson
    with cdm_engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM cdm.observation'))
        for row in result:
            print(row)


def load_csv_to_cdm(csv_file_path: str, database_name: str = None):
    launch_psql()


__all__ = ['DEFAULT_DATA_PATH', 'create_model', 'load_data', 'load_csv_to_cdm']
