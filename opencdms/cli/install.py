import sys
import click
import sh
from opencdms.utils.paths import base_path, requirements_path


@click.group(invoke_without_command=True)
@click.pass_context
def install(context):
    """Installs all package requirements (or specify, e.g. docs)."""
    if context.invoked_subcommand is None:
        click.echo('Installing required packages to current environment...')
        try:
            sh.pip('install', '-r', requirements_path('all'))
            sh.bash(f'{base_path("cli/bash/install_docker.sh")}')
            sh.bash(f'{base_path("cli/bash/install_gh.sh")}')
            sh.bash(f'{base_path("cli/bash/install_psql.sh")}')
            print('Package requirements installed successfully.')
        except sh.ErrorReturnCode as error:
            print(f'Error installing requirements: {error}', file=sys.stderr)
            sys.exit(1)


@install.command()
def docs():
    """Installs the requirements for building the documentation."""
    try:
        sh.pip('install', '-r', requirements_path('docs'))
        print('Documentation requirements installed successfully.')
    except sh.ErrorReturnCode as e:
        print(f'Error installing requirements: {e}', file=sys.stderr)
        sys.exit(1)
