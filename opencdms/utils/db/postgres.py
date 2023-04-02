"""
This module contains database utils that are specific to Postgres

"""
import subprocess
from typing import Optional

from sqlalchemy import create_engine, text
from sqlalchemy_utils import create_database, database_exists

from opencdms.db.config import get_engine, DEFAULT_DATABASE


def launch_psql(database_name: Optional[str] = None, *args, **kwargs) -> None:
    """
    Launches the `psql` command-line tool with the connection string parameters
    for the specified database, or using the default database if no database
    name is given.

    Args:
        database_name: The name of the database to connect to. If not provided,
        the `psql` command will be launched for the default database.
        *args: Any additional arguments that should be included in the `psql`
        command.
        **kwargs: Additional keyword arguments to pass directly to subprocess.run()
        e.g., `input="text to pipe to psql"`

    Raises:
        subprocess.CalledProcessError: If the `psql` command returns a non-zero
        exit code.

    Returns:
        None
    """
    if not database_name:
        database_name = DEFAULT_DATABASE

    # Get the SQLAlchemy engine object for the specified database
    engine = get_engine(database_name)

    # Extract connection string parameters from the SQLAlchemy engine object
    db_name = engine.url.database
    db_user = engine.url.username
    db_password = engine.url.password
    db_host = engine.url.host
    db_port = engine.url.port

    if database_exists(engine.url):
        psql_command = f'psql postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    else:
        psql_command = f'psql postgresql://{db_user}:{db_password}@{db_host}:{db_port}/'

    # Add any additional arguments to the `psql` command
    for arg in args:
        psql_command += f' {arg}'

    subprocess.run(psql_command, shell=True, check=True, **kwargs)


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
    #       we can pass engine.url to sqlalchemy_utils.create_database and it will create the
    #       db_name from the engine's connection string
    if connection_string is None:
        connection_string = get_connection_string()
    if schema_names is None:
        schema_names = []

    try:
        engine = create_engine(connection_string)

        if not database_exists(engine.url):
            create_database(engine.url)

        connection = engine.connect()

        for schema_name in schema_names:
            if not engine.dialect.has_schema(connection, schema_name):
                connection.execute(text(f"CREATE SCHEMA {schema_name}"))
                # TODO: not clear whether connection always has a commit method
                try:
                    connection.commit()
                except AttributeError:
                    pass
                finally:
                    connection.close()

        # Create the specified schemas
#        for schema_name in schema_names:
#            if not engine.dialect.has_schema(connection, schema_name):
#                connection.execute(schema.CreateSchema(schema_name))
#                raise ValueError(engine.dialect.has_schema(connection, schema_name))
                
    finally:
        # Dispose of the engine to close any remaining connections
        engine.dispose()
