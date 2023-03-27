import pytest

from opencdms.utils.paths import tests_path


def run_tests(test_type: str = ''):
    """
    Runs all tests or tests of a specific type using pytest.

    Args:
        test_type (str, optional): Type of tests to run. Valid options are
                                   'unit' or 'integration'. Defaults to ''.

    Returns:
        None
    """
    result = pytest.main([tests_path(test_type)])
    if result == 0:
        return f"All {'type ' if test_type else ''}tests passed successfully"
    else:
        return f"Some {'type ' if test_type else ''}tests failed"