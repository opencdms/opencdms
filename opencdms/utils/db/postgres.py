"""
This module contains database utils that are specific to Postgres

"""
from typing import Optional
import sh
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database

from opencdms.db.config import get_engine, DEFAULT_DATABASE
from opencdms.utils.db import DatabaseError


def launch_psql(database_name: Optional[str] = None) -> None:
    """
    Launches the `psql` command-line tool with the connection string parameters
    for the specified database, or using the default database if no database
    name is given.

    Args:
        database_name: The name of the database to connect to. If not provided,
        the `psql` command will be launched for the default database

    Raises:
        sh.ErrorReturnCode: If the `psql` command returns a non-zero exit code.

    Returns:
        None
    """
    if not database_name:
        database_name = DEFAULT_DATABASE

    # Get the SQLAlchemy engine object for the specified database
    engine: Engine = get_engine(database_name)

    # Extract connection string parameters from the SQLAlchemy engine object
    db_url = str(engine.url)
    db_name = engine.url.database
    db_user = engine.url.username
    db_password = engine.url.password
    db_host = engine.url.host
    db_port = engine.url.port

    # Use `sh.psql` to launch `psql` with the appropriate connection string parameters
    sh.psql(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
        "--set sslmode=require",
    )


def create_db_and_schemas(db_name: str, schema_names: list[str] = None, connection_string: str = None) -> None:
    """
    Create a database and specified schemas if they do not exist.

    Args:
        db_name (str): The name of the database to create or connect to.
        schema_names (list[str], optional): A list of schema names to create in the database.
        connection_string (str, optional): A SQLAlchemy connection string to connect to the server (if not supplied then uses the default database connection)

    Raises:
        ProgrammingError: If the specified database or schemas already exist.

    Returns:
        None
    """
    # TODO: We should probably pass an engine and not a connection string to this function
    if connection_string is None:
        connection_string = get_connection_string()
    if schema_names is None:
        schema_names = []

    conn_str_without_db_name = connection_string.rsplit('/', 1)[0]

    # Create the specified database
    create_database(conn_str_without_db_name, db_name)

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
