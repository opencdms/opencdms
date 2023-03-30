import importlib
import click
import sh
import subprocess
import socket

from opencdms.db import load, seeder
from opencdms.utils.paths import base_path


# TODO: port assignments must come from opencdms_test_databases package
CONTAINER_PORT = {
    "postgres": 5432,
    "mariadb": 3306,
    "opencdmsdb": 35432,
    "postgresql": 25432,
    "mysql": 23306,
    "oracle": 21521,
    "clide": 35433,
    "climsoft-4.1.1": 33308,
    "mch-english": 33306,
    "midas": 31521,        
    "wmdr": 35434,
    "surface": 45432
}


@click.group()
def db():
    """Database related commands"""
    pass


# TODO: switch to opencdms.utils.network.check_port
def _check_port(port)->bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # TODO: localhost shouldn't be hardcoded
        return s.connect_ex(('localhost', port)) == 0


# TODO: Consider type=click.Choice(['opencdmsdb', 'all', 'climsoft', 'clide'])
#       In which case we would not accept comma separated list
@click.command()
@click.option('--containers', help='Comma separated list of container(s) to be started',
    default='opencdmsdb')
def start(containers: str):
    """ 
    Start database containers
    
    """
    docker_compose_file = f"{ base_path('db') }/docker-compose.yml"

    if containers == 'all':
        # Start all containers
        service_ports = CONTAINER_PORT.values()
        occupied = False
        for port in service_ports:
            if _check_port(port):
                click.echo(f"########### Port {port} is in use by another service. Close the service and run again. #############")
                occupied = True
        if occupied and not click.confirm("Some ports are already in use by another service. Do you want to continue ?"):
            exit(0)
        start_command = f"docker-compose -f {docker_compose_file} up -d"
        compose_args = ['-f', docker_compose_file, 'up', '-d']
        containers_started = CONTAINER_PORT.keys()
    else:
        containers_to_start = containers.split(",")
        containers_started = []
        for container in containers_to_start:
            if container in CONTAINER_PORT.keys():
                if _check_port(CONTAINER_PORT[container]) is True:
                    click.echo(f"########### Service Port {CONTAINER_PORT[container]} for {container} is in use by another service. #############")
                    continue
            else:
                click.echo(f"########### Invalid container name {container} #############")
                continue
            containers_started.append(container)
        if len(containers_started) > 0:
            databases = " ".join(containers_started)
            start_command = f"docker-compose -f {docker_compose_file} up -d {databases}"
            compose_args = ['--verbose', '-f', docker_compose_file, 'up', '-d', databases]
        else:
            exit(0)
    
    click.echo('Starting databases....')
    try:
        out = sh.docker_compose(*compose_args, _cwd=base_path('db/docker'))
    except sh.ErrorReturnCode as err:
        click.echo("Start up not successful")
        click.echo(err.stderr)
        click.echo("please close any conflicting ports")
        return err.exit_code

    click.echo(out)


@click.command()
def stop():
    """ Stops all database containers """
    click.echo('Stopping databases....')
    docker_compose_file = f"{ test_databases_path()}/docker-compose.yml"
    click.echo(docker_compose_file)
    out = subprocess.run(f"docker-compose -f {docker_compose_file} down", shell=True)


@click.command(name="seed")
def seed():
    """ Creates tables and populates them with random data"""
    click.echo("Generating random data....")
    seeder.up()
    click.echo("Successfully inserted random data into DB")


@click.command()
def list():
    """List all running database containers"""
    # TODO: Currently all running containers are listed
    cmd = "docker ps"
    subprocess.run(cmd, shell=True)


@click.command(name='load')
def load_command():
    """List all running database containers"""
    load.load_data()


db.add_command(start)
db.add_command(stop)
db.add_command(seed)
db.add_command(list)
db.add_command(load_command)
