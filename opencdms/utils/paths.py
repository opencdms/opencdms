import os
import sys

def get_base_path():
    """Returns the base path for the opencdms package."""

    module_path = sys.modules['opencdms'].__file__
    # Construct the base path by going up one level from the 'mypackage' module path
    base_path = os.path.abspath(os.path.join(module_path, os.pardir))
    return base_path
