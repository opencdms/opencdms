"""Console script for opencdms."""
import sys
import click

from codespace import codespace_command, cs_command


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


main.add_command(codespace_command)
main.add_command(cs_command)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
