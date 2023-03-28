"""Implementation of console script for opencdms."""
import click

# from opencdms.utils.imports import test_import
from opencdms.cli.db import db
from opencdms.cli.docs import docs
from opencdms.cli.install import install
from opencdms.cli.test import test


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


main.add_command(db)
main.add_command(docs)
main.add_command(install)
main.add_command(test)
