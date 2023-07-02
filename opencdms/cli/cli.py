"""Implementation of console script for opencdms."""
import os
import click


uninstalled_packages = []


class UnavailablePackagesGroup(click.Group):
    """
    A custom click Group class that extends the default click.Group class and adds a message string about uninstalled packages to the help message.

    The class inherits from click.Group, and overrides the `get_help` method to append the message string returned by the `unavailable_packages` function to the end of the help message.

    Attributes:
    ----------
    Inherits all the attributes of the `click.Group` class.

    Methods:
    --------
    get_help(ctx: Context) -> str:
        Overrides the `get_help` method of the `click.Group` class to add a message string about uninstalled packages to the end of the help message.

    """
    def get_help(self, ctx):
        """
        Overrides the `get_help` method of the `click.Group` class to add a message string about uninstalled packages to the end of the help message.

        Parameters:
        ----------
        ctx: click.Context
            The context object for the command group.

        Returns:
        -------
        str
            The help message string, with the message string about uninstalled packages appended to the end.
        """
        return super().get_help(ctx) + unavailable_packages()


def unavailable_packages():
    """
    Returns a string listing all uninstalled packages.

    If there are no uninstalled packages, an empty string is returned.

    Returns:
    --------
    str
        A message string containing information about uninstalled packages.

    """
    if uninstalled_packages:
        msg = [
            os.linesep,
            'Uninstalled commands*:',
            *[f'  {pkg}' for pkg in uninstalled_packages],
            f'{os.linesep}  *install using `opencdms install <pkg>`',
            os.linesep,
        ]
        return os.linesep.join(msg)
    else:
        return ''


main = UnavailablePackagesGroup()


try:
    from opencdms.cli.db import db
    main.add_command(db)
except (ImportError, ModuleNotFoundError):
    uninstalled_packages.append('db')

try:
    from opencdms.cli.docs import docs
    main.add_command(docs)
except (ImportError, ModuleNotFoundError):
    uninstalled_packages.append('docs')

try:
    from opencdms.cli.install import install
    main.add_command(install)
except (ImportError, ModuleNotFoundError):
    uninstalled_packages.append('install')

try:
    from opencdms.cli.api import api
    main.add_command(api)
except (ImportError, ModuleNotFoundError):
    uninstalled_packages.append('api')

try:
    from opencdms.cli.test import test
    main.add_command(test)
except (ImportError, ModuleNotFoundError):
    uninstalled_packages.append('test')
