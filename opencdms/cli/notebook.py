import click
import sh


@click.command()
def notebook() -> None:
    sh.jupyter('notebook')
