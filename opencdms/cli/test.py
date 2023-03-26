import unittest
import click

from opencdms.utils.paths import get_tests_path


@click.group()
def test():
    pass


@test.command()
@click.option('--type', type=click.Choice(['unit', 'integration']), default='all')
def test(type):
    """Run specified type of tests"""
    if type == 'all':
        test_directory = 'tests/'
    else:
        test_directory = f'tests/{test_type}'

    loader = unittest.TestLoader()
    test_suite = loader.discover(test_directory, pattern='*_test.py')

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    test_type = f"" if type=='all' else f"{type} "

    if result.wasSuccessful():
        click.echo(f"All {test_type}tests passed successfully")
    else:
        click.echo(f"Some {test_type}tests failed")