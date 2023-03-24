import subprocess
import os
import click


# `gh codespace <command>` and whether they accept name of codespace
# `-c, --codespace <string>`
CODESPACE_OPT = {
    'code': True,
    'cp': True,
    'create': False,
    'delete': True,
    'edit': True,
    'jupyter': True,
    'list': False,
    'logs': True,
    'ports': True,
    'rebuild': True,
    'ssh': True,
    'stop': True,
}


def repoHasChanges(details=True):
    summary_status="""find /workspaces -type d -name '.git' | while read dir ; do sh -c "cd $dir/../ && git status -s" ; done"""
    detailed_status="""find /workspaces -type d -name '.git' | while read dir ; do sh -c "cd $dir/../ && echo \"${dir//\.git/}\" && git status -s" ; done"""
    
    if details:
        result = subprocess.run(detailed_status, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = result.stdout.decode()
    else:
        result = subprocess.run(summary_status, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = bool(len(result.stdout.decode().strip()))
    return output


@click.command(name="codespace")
@click.argument('command', type=click.Choice(CODESPACE_OPT.keys()))
@click.option("--codespace-name", default=os.environ.get("CODESPACE_NAME"))
def codespace_command(command, codespace_name):
    """
    A command-line interface for GitHub Codespaces.

    This command accepts any of the GitHub CLI codespace commands
    (e.g. code, create, delete, ...) and then calls `gh codespace <command>`
    
    If the command accepts `--codespace $CODESPACE_NAME` then the name of
    the current codespace is automatically added.

    In the case where command is `delete` we first check that changes in all
    repositories in /workspaces/ have been committed and pushed.

    Args:
        command: A required argument that specifies the GitHub CLI codespace
            command to execute (e.g. `delete`).
        codespace_name: An optional argument that specifies the name of the
            codespace to operate on. If not provided, the value of the
            $CODESPACE_NAME environment variable will be used as the default.

    Returns:
        None.

    See also:
        https://cli.github.com/manual/gh_codespace

    """
    gh_command = ["gh", "codespace", command]
    if codespace_name and CODESPACE_OPT[command]:
        # codespace_name specified and command accepts codespace option
        gh_command.append(f"--codespace={codespace_name}")
    if command == 'delete':
        if(repoHasChanges(details=False)):
            print('Workspace has changes')
            return
        # See changes since last `git tag` release
        # git log --pretty=format:'%s' `git describe --tags --abbrev=0`..HEAD
        raise ValueError()
    
    subprocess.run(gh_command)


# add an alias for the `codespace` command
@click.command(name="cs", short_help="Alias for `codespace` command")
@click.pass_context
def cs_command(ctx):
    ctx.invoke(codespace_command)
