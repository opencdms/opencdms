header_mapping = {
    "cdm_id": "id",
    "cdm_location": "location",
    "cdm_elevation": "elevation",
    "cdm_observation_type": "observation_type_id",
    "cdm_phenomenon_start": "phenomenon_start",
    "cdm_phenomenon_end": "phenomenon_end",
    "cdm_result_value": "result_value",
    "cdm_result_uom": "result_uom",
    "cdm_result_description": "result_description",
    "cdm_result_quality": "result_quality",
    "cdm_result_time": "result_time",
    "cdm_valid_from": "valid_from",
    "cdm_valid_to": "valid_to",
    "cdm_host": "host_id",
    "cdm_observer": "observer_id",
    "cdm_observed_property": "observed_property_id",
    "cdm_observing_procedure": "observing_procedure_id",
    "cdm_report_id": "report_id",
    "cdm_collection": "collection_id",
    "cdm_parameter": "parameter",
    "cdm_feature_of_interest": "feature_of_interest_id",
    "cdm_version": "version",
    "cdm_change_date": "change_date",
    "cdm_user": "user_id",
    "cdm_status": "status_id",
    "cdm_comments": "comments",
    "cdm_source": "source_id"
}


# Using csv.reader to load csv file failed:
# TODO: The custom csv reader dialect below is not currently working
#       using the funciton in load.py instead to call psql to ingest the file
'''
def load_csv_to_cdm(csv_file_path: str, engine: Engine, table: Table, delimiter: str = ',', header_mapping: Dict[str, str] = None, null_value: str = 'NA', quote_char: str = '"'):
    """
    Loads data from a CSV file into a database table using SQLAlchemy.

    Args:
        csv_file_path (str): The file path to the CSV file.
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object
            to use for the database connection.
        table (sqlalchemy.schema.Table): The table object to insert the data into.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
        header_mapping (dict, optional): A dictionary mapping the headers in the CSV file to the column names in the table.
            If None, it is assumed that the headers in the CSV file match the column names in the table. Defaults to None.
        null_value (str, optional): The string that represents null values in the CSV file. Defaults to 'NA'.
        quote_char (str, optional): The character used to quote fields in the CSV file. Defaults to '"'.

    Returns:
        None
    """
    # Define a custom CSV dialect that uses the specified null_value and quote_char
    csv.register_dialect('custom', delimiter=delimiter, quotechar=quote_char, quoting=csv.QUOTE_MINIMAL, doublequote=False, escapechar=None, lineterminator='\r\n', skipinitialspace=False, strict=False, null=str(null_value))

    with open(csv_file_path, 'r') as csv_file:
        # Read the headers from the first row of the file
        headers = next(csv.reader(csv_file, dialect='custom'))

        # Use the header_mapping if provided, otherwise assume the headers match the column names in the table
        if header_mapping:
            # Check that all headers in the mapping exist in the CSV file
            if not set(header_mapping.keys()).issubset(set(headers)):
                raise ValueError("Header mapping contains keys that are not in the CSV file.")
            # Use the mapped names as headers
            headers = [header_mapping[header] for header in headers]

        # Using begin() makes the start and end of a transaction explicit
        with engine.begin() as conn:
            # Insert the data into the table
            rows = [dict(zip(headers, row)) for row in csv.reader(csv_file, dialect='custom')]
            conn.execute(table.insert(), rows)


# Using `opencdms db psql` command to load csv files one at a time fails due to
#  relations from other files not existing

# Initial load command used by `opencdms db load`
# Note that this command makes a lot of assumptions about the
# data to load and needs improvements
import csv
import glob
import os
from typing import Dict

from sqlalchemy import text, Table
from sqlalchemy.engine import Engine

from opencdms.db.config import get_connection_string, get_engine
from opencdms.utils.db import DatabaseError
from opencdms.utils.db.postgres import create_db_and_schemas
from opencdms.utils.paths import base_path
from opencdms.utils.db.postgres import launch_psql

from .csv import header_mapping


def load_data():
    """ Load sample data """
    connection_string = get_connection_string('CDM')
    cdm_engine = get_engine()

    try:
        create_db_and_schemas('opencdmsdb', ['cdm'], connection_string)
    except DatabaseError:
        pass

    create_model(cdm_engine)

    # Load code tables first
    file_pattern = os.path.join(DEFAULT_DATA_PATH, 'code_tables/*.csv')
    for file_name in glob.glob(file_pattern):
        table_name = os.path.splitext(os.path.basename(file_name))[0]
        # TODO: Let's get status.csv renamed as record_status.csv
        table_name = 'record_status' if table_name == 'status' else table_name
        table_name = 'cmd_' + table_name
        load_csv_to_cdm(table_name, file_name)

    file_pattern = os.path.join(DEFAULT_DATA_PATH, 'data_tables/CA_*.csv')
    for file_name in glob.glob(file_pattern):
        # Execute psql as per https://github.com/opencdms/opencdms-test-data/tree/ceaf5247df1304b6e9acd8af29b7aad9942d760a/data/cdm#ingestion
        load_csv_to_cdm('cdm.observation', file_name)
        break


def load_csv_to_cdm(table_name: str, csv_file_path: str, database_name: str = None):
    """ Load CSV to CDM """
    options = "WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b'"
    command = fr'\COPY {table_name} FROM {csv_file_path} {options};'
    launch_psql(database_name, input=command.encode())

'''