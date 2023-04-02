"""
This module contains a function for working with database connection strings for known databases.

"""
import configparser
import os
from typing import Optional, Union, Dict

from opencdms.utils.paths import base_path


def get_connection_strings(database_name: Optional[str] = None) -> Union[str, Dict[str, str]]:
    """Return dictionary value for given database_name if provided, else return full dictionary.

    Args:
        database_name: Optional name of the database to retrieve the connection string for.

    Returns:
        If `database_name` is provided, return the connection string for that database as a string.
        If `database_name` is not provided, return the entire dictionary of connection strings.

        If the `database_name` is not found in the configuration file, return a string indicating that.

    """
    config = configparser.ConfigParser()
    config.read(base_path('db/alembic/alembic.ini'))
    connections = {}
    for section in config.sections():
        connection = config[section]['sqlalchemy.url']
        if connection.startswith('${') and connection.endswith('}'):
            connection = os.environ.get(connection[2:-1], '')
        if section == 'alembic':
            connections['Default'] = connection
        else:
            connections[section] = connection
    if database_name:
        if database_name in connections:
            return connections[database_name]
        else:
            return f'{database_name} not found'
    else:
        return connections
