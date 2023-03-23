"""Console script for opencdms."""
import sys
import click


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


if __name__ == "__main__":
    sys.exit(main())  # pragma: no coveR
