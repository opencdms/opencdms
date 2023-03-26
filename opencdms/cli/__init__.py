"""Console script for opencdms."""
import sys
import click

from opencdms.cli.db import db
from opencdms.cli.install import install
from opencdms.cli.docs import docs


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


main.add_command(db)
main.add_command(install)
main.add_command(docs)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
