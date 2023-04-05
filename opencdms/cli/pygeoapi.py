"""
Commands for working with pygeoapi

"""
import os
import click

from opencdms.utils.paths import base_path


PYGEOAPI_CONFIG = os.environ.get('PYGEOAPI_CONFIG', '/tmp/pygeoapi-config.yml')
PYGEOAPI_OPENAPI = os.environ.get('PYGEOAPI_OPENAPI', '/tmp/pygeoapi-openapi.yml')


@click.command()
@click.argument('config', default=None, required=False)
def pygeoapi(config: str) -> None:
    """
    Start a pygeoapi instance with a given configuration file.

    Args:
        config (str, optional): The name of the configuration file to
            use. Defaults to '/tmp/pygeoapi-config.yml'

    Returns:
        None

    Raises:
        RuntimeError: If the 'PYGEOAPI_CONFIG' environment variable
            points to a file in the opencdms code repository.

    """
    # Ensure users aren't editing the config files in the code repo
    # the files should exist in another location like /tmp/
    # TODO: Checking whether integrations is in the path is not sufficient
    if 'integrations' in PYGEOAPI_CONFIG:
        raise RuntimeError("PYGEOAPI_CONFIG environment variable shouldn't point to a file in the code repository")
    if config:
        config = f'{config}.yml' if not config.endswith('.yml') else config
        config_path = os.path.join(base_path(), 'integrations/pygeoapi/config/', config)
        os.system(f'cp {config_path} {PYGEOAPI_CONFIG}')

    # Ensure the required environment variables are set
    os.environ['PYGEOAPI_CONFIG'] = PYGEOAPI_CONFIG
    os.environ['PYGEOAPI_OPENAPI'] = PYGEOAPI_OPENAPI

    os.system('pygeoapi openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI')
    os.system('pygeoapi serve')
