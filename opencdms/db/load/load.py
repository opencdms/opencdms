"""
    $ opencdms install
    $ opencdms db start
    $ opencdms db load /workspaces/opencdms-test-data/data/cdm/`  # creates db it not exists

"""
import os
import subprocess

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

    try:
        create_db_and_schemas('opencdmsdb', ['cdm'], connection_string)
    except DatabaseError:
        pass

    create_model(cdm_engine)

    # Use shell script to load data
    
    # Location of cdm.sh
    load_cdm = os.path.join(os.path.dirname(__file__), 'cdm.sh')
    connection_string = str(get_engine().url)
    result = subprocess.run(
        ['/bin/bash', load_cdm, connection_string],
        cwd=DEFAULT_DATA_PATH,
        capture_output=True
    )
    if result.returncode != 0:
        print("Error occurred: ")
        print(result.stderr.decode())
    else:
        print(result.stdout.decode())


__all__ = ['DEFAULT_DATA_PATH', 'create_model', 'load_data']
