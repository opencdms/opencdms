"""Implementation of console script for opencdms."""
import os
import click


uninstalled_packages = []


class UnavailablePackagesGroup(click.Group):
    def get_help(self, ctx):
        return super().get_help(ctx) + print_unavailable_packages()


def print_unavailable_packages():
    if uninstalled_packages:
        msg = [
            os.linesep,
            'Uninstalled commands*:',
            *[f'  {pkg}' for pkg in uninstalled_packages],
            f'{os.linesep}  *install using `opencdms install <pkg>`',
            os.linesep,
        ]
        return os.linesep.join(msg)


main = UnavailablePackagesGroup()


try:
    from opencdms.cli.db import db
    main.add_command(db)
except ModuleNotFoundError:
    uninstalled_packages.append('db')

try:
    from opencdms.cli.docs import docs
    main.add_command(docs)
except ModuleNotFoundError:
    uninstalled_packages.append('docs')

try:
    from opencdms.cli.install import install
    main.add_command(install)
except ModuleNotFoundError:
    uninstalled_packages.append('install')

try:
    from opencdms.cli.test import test
    main.add_command(test)
except ModuleNotFoundError:
    uninstalled_packages.append('test')
