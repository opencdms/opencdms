import csv
from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.engine import Engine


def load_csv_to_db(csv_file_path: str, engine: Engine, table_name: str, headers: list):
    """
    Loads data from a CSV file into a database table using SQLAlchemy.

    Args:
        csv_file_path (str): The file path to the CSV file.
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object
            to use for the database connection.
        table_name (str): The name of the table to insert the data into.
        headers (list): A list of column names in the CSV file.

    Returns:
        None
    """
    # create metadata object
    metadata = MetaData()

    # create table object
    table = Table(table_name, metadata, *[Column(name, String) for name in headers])

    # load data from csv file
    with open(csv_file_path, 'r') as f:
        conn = engine.connect()
        conn.execute(table.insert(), [row for row in csv.DictReader(f)])

    # commit changes
    conn.close()
