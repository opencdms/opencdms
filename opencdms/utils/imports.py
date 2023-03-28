""" A collection of functions for assisting with imports, including lazy importing """
# TODO: This module is depreciated, see requirement module instead
import importlib


def test_import(package_name: str) -> bool:
    """
    Test if a package is available.

    Args:
        package_name (str): The name of the package to test.

    Returns:
        bool: True if the package is available, False otherwise.
    """
    try:
        importlib.import_module(package_name)
    except ImportError:
        return False

    return True



