import importlib
import click

#from opencdms.utils.tests import run_tests


# TODO: This workaround is currently needed otherwise
# when cli is initiated the import from utils.tests
# attempts to import pytest which may not be installed yet
# We need a longer term solution for lazy loading that
# will install requirements as needed.
def run_tests(*args, **kwargs):
    """Temporary version of run_tests that replaces utils.tests with lazy loading"""
    run_tests = importlib.import_module("opencdms.utils.tests.run_tests")
    return run_tests


@click.group(invoke_without_command=True)
@click.pass_context
def test(context):
    """Run all tests (or specify unit|integration)"""
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
