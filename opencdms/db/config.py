"""
This module provides functions for managing connection strings

Example usage:

    from opencdms.db.config import get_engine

    # Get the engine object for the "CDM" database
    engine = get_engine("CDM")

    # Use the engine to execute SQL queries
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM observation")
        for row in result:
            print(row)

"""
import configparser
import sqlalchemy
from sqlalchemy import create_engine

from opencdms.utils.paths import base_path


DEFAULT_DATABASE = 'CDM'


def get_connection_string(database: str = DEFAULT_DATABASE) -> str:
    """
    Returns the SQLAlchemy connection string for the specified database
    using the default alembic.ini file.

    Args:
        database: The name of the database to connect to. Default is "CDM".

    Returns:
        The connection string for the specified database.

    Raises:
        ConfigParser.NoSectionError: If the specified database name is not found in the alembic.ini file.
        ConfigParser.NoOptionError: If the "sqlalchemy.url" option is not found in the specified database section.
    """
    config = configparser.ConfigParser()
    config.read(base_path('db/alembic/alembic.ini'))

    # Get the connection string for the named database
    conn_str = config.get(database, "sqlalchemy.url")

    return conn_str


def get_engine(database: str = DEFAULT_DATABASE) -> sqlalchemy.engine.base.Engine:
    """
    Returns an SQLAlchemy engine for the specified database.

    Args:
        database: The name of the database to connect to. Default is "CDM".

    Returns:
        An SQLAlchemy engine instance.

    Raises:
        sqlalchemy.exc.ArgumentError: If the connection string is not valid.
    """
    conn_str = get_connection_string(database)

    # Create an SQLAlchemy engine using the connection string
    return create_engine(conn_str)
