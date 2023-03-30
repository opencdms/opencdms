"""
This module contains generic database utils that are not database specific

"""

class DatabaseError(Exception):
    """
    A custom exception class for database-related errors.

    This exception can be raised when there is an error with the
    database connection or query execution.

    Example usage:
    try:
        # execute database query
    except DatabaseError as e:
        # handle database error
    """


__all__ = ['DatabaseError']
