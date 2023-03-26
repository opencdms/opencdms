import importlib
import click

#from opencdms.utils.tests import run_tests


# TODO: need a long term solution to lazy loading that
#       will install requirements as needed
def run_tests(*args, **kwargs):
    run_tests = importlib.import_module("opencdms.utils.tests.run_tests")
    return run_tests


@click.group(invoke_without_command=True)
@click.pass_context
def test(context):
    if context.invoked_subcommand is None:
        click.echo('No subcommand specified, running all tests...')
        click.echo(run_tests())


@test.command()
def unit():
    click.echo('Running unit tests...')
    click.echo(run_tests('unit'))


@test.command()
def integration():
    click.echo('Running integration tests...')
    click.echo(run_tests('integration'))
