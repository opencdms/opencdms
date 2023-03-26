import os
import sys

import opencdms_test_databases


def test_databases_path(path: str = ''):
    """Returns the required path for the opencdms_test_databases package.

    Args:
        path (str): Optional directory path to append to the base path.

    Returns:
        str: The requested path.
    """
    module_path = os.path.dirname(sys.modules['opencdms_test_databases'].__file__)
    base_path = os.path.abspath(os.path.join(module_path, path))
    return base_path
