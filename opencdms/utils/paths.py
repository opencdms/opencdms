import os
import sys


def base_path(path: str = ''):
    """Returns the required path for the opencdms package.

    Args:
        path (str): Optional directory path to append to the base path.

    Returns:
        str: The requested path.
    """
    module_path = sys.modules['opencdms'].__file__
    base_path = os.path.abspath(os.path.join(module_path, path))
    return base_path


def requirements_path(name: str):
    """Returns the path for the named requirements file.

    Args:
        name (str): Name of requirements file

    Returns:
        str: The path to the requirements file.

    """
    full_name = f'{name}.txt' if not name.endswith('txt') else 'name'
    return base_path(f'requirements/{full_name}')


def tests_path():
    """Returns the tests path."""
    # TODO: if package installed with pip then tests won't be available
    return base_path('../tests')
