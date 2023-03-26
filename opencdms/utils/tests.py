import pytest

from opencdms.utils.paths import tests_path


def run_tests(type: str = ''):
    """
    Runs all tests or tests of a specific type using pytest.

    Args:
        type (str, optional): Type of tests to run. Valid options are
                              'unit' or 'integration'. Defaults to ''.

    Returns:
        None
    """
    result = pytest.main([tests_path(type)])
    if result == 0:
        return f"All {'type ' if type else ''}tests passed successfully"
    else:
        return f"Some {'type ' if type else ''}tests failed"