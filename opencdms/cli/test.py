import unittest
import click

from opencdms.utils.paths import get_tests_path


@click.group()
def test():
    pass


@test.command()
@click.option('--type', type=click.Choice(['unit', 'integration']), default='')
def test(type):
    """Run specified type of tests"""
    loader = unittest.TestLoader()
    test_suite = loader.discover(get_tests_path(type), pattern='*_test.py')

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        click.echo(f"All {'type ' if type else ''}tests passed successfully")
    else:
        click.echo(f"Some {'type ' if type else ''}tests failed")