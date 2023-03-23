"""Console script for opencdms."""
import sys
import subprocess
import os
import click


@click.group()
def main(args=None):
    """Console script for opencdms."""
    # See click documentation at https://click.palletsprojects.com/
    pass


@click.command(name="codespace")
@click.argument("command")
@click.option("--codespace-name", default=os.environ.get("CODESPACE_NAME"), help="Name of the codespace")
def codespace_command(command, codespace_name):
    """
    A command-line interface for GitHub Codespaces.

    This command accepts any of the GitHub CLI codespace commands
    (e.g. code, create, delete, ...) and then calls `gh codespace <command>`
    and adds `--codespace $CODESPACE_NAME` to the end of the command.

    Args:
        command: A required argument that specifies the GitHub CLI codespace
            command to execute.
        codespace_name: An optional argument that specifies the name of the
            codespace to operate on. If not provided, the value of the
            $CODESPACE_NAME environment variable will be used as the default.

    Returns:
        None.

    Raises:
        click.ClickException: If `codespace_name` is not provided by the user or set in the environment.

    See also:
        https://cli.github.com/manual/gh_codespace

    """
    if not codespace_name:
        click.echo("Error: codespace name not provided and $CODESPACE_NAME not set.")
        raise click.ClickException("codespace name not provided and $CODESPACE_NAME not set.")
    gh_command = ["gh", "codespace", command]
    if codespace_name:
        gh_command.append(f"--codespace={codespace_name}")
    subprocess.run(gh_command)


# add an alias for the `codespace` command
@click.command(name="cs", short_help="Alias for `codespace` command")
@click.pass_context
def cs_command(ctx):
    ctx.invoke(codespace_command)


main.add_command(codespace_command)
main.add_command(cs_command)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no coveR
