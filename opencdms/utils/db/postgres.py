"""
This module contains database utils that are specific to Postgres

"""
from sqlalchemy import create_engine

from opencdms.utils.db import DatabaseError


def create_db_and_schemas(db_name: str, schema_names: list[str] = None, connection_string: str = None) -> None:
    """
    Create a database and specified schemas if they do not exist.

    Args:
        db_name (str): The name of the database to create or connect to.
        schema_names (list[str], optional): A list of schema names to create in the database.
        connection_string (str): A SQLAlchemy connection string to connect to the server.

    Raises:
        ProgrammingError: If the specified database or schemas already exist.

    Returns:
        None
    """
    if connection_string is None:
        # TODO: add default connection string behaviour?
        raise ValueError('connection_string must be specified')
    if schema_names is None:
        schema_names = []

    # Connect to the default 'postgres' database
    engine = create_engine(connection_string)

    # Check if the specified database already exists
    with engine.connect() as connection:
        result = connection.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        if result.fetchone() is not None:
            raise DatabaseError(f"Database '{db_name}' already exists")

    # Create the specified database
    with engine.connect() as connection:
        connection.execute(f"CREATE DATABASE {db_name}")

    # Dispose of the engine to close any remaining connections
    engine.dispose()

    # Connect to the newly created or existing database
    new_connection_string = connection_string.rsplit("/", 1)[0] + f"/{db_name}"
    engine = create_engine(new_connection_string)

    # Check if the specified schemas already exist
    with engine.connect() as connection:
        for schema_name in schema_names:
            result = connection.execute(f"SELECT 1 FROM pg_namespace WHERE nspname='{schema_name}'")
            if result.fetchone() is not None:
                raise ProgrammingError(f"Schema '{schema_name}' already exists")

    # Create the specified schemas
    with engine.begin() as connection:
        for schema_name in schema_names:
            connection.execute(f"CREATE SCHEMA {schema_name}")

    # Dispose of the engine to close any remaining connections
    engine.dispose()
