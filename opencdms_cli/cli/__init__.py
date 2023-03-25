"""Console script for opencdms."""
import sys
import click

from opencdms_cli.db import db


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


main.add_command(db)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
