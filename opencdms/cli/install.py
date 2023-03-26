import sys
import click
import sh
from opencdms.utils.paths import requirements_path


@click.group()
def install():
    pass


@install.command()
def docs():
    """Installs the requirements for building the documentation."""
    try:
        sh.pip('install', '-r', requirements_path('docs'))
        print('Documentation requirements installed successfully.')
    except sh.ErrorReturnCode as e:
        print(f'Error installing requirements: {e}', file=sys.stderr)
        sys.exit(1)
