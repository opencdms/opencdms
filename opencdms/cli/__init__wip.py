"""Console script for opencdms."""
import importlib
import pkgutil
import sys
import click

from opencdms.cli.docs import docs
from opencdms.cli.install import install
from opencdms.cli.test import test


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


if pkgutil.find_loader('opencdms_test_databases') is None:
    cli.add_command(
        click.Command(
            name='db', 
            help='Database related commands',
            callback=lambda: click.echo('Hello, world!')
        )
    )

else:
    db = importlib.import_module("opencdms.cli.db")
    #main.add_command(db)


main.add_command(docs)
main.add_command(install)
main.add_command(test)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
