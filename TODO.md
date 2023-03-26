WIP

Currently the user has to run `opencdms install` to install all conceiveable
dependencies into their current environment. Or they have to be an expert and
`pip install -r opencdms/requirements/file.txt` for the specific requirements
that they have.

Can we do better, without developing a full blown package manager that keeps
track of all dependencies and without having to implement lazy package loading
everywhere?

cli.py can only import modules that are installed - so we have to know what
is installed and what isn't.

Potentially the CLI could list "Unavailable commands" below "Commands" and
they would become available if the prerequisites were installed. Here is an
outline that creates a custom help command that overrides the default help
command in Click, and lists the unavailable commands in this custom help command.

```
import click

class CustomHelpCommand(click.Command):
    def __init__(self, *args, **kwargs):
        super(CustomHelpCommand, self).__init__(*args, **kwargs)

    def format_commands(self, ctx, formatter):
        # Call the default format_commands function
        super(CustomHelpCommand, self).format_commands(ctx, formatter)

        # Add your custom unavailable commands section
        formatter.write_heading('Unavailable Commands')
        with formatter.indentation():
            for cmd in self.list_unavailable_commands(ctx):
                formatter.write_text(cmd)

    def list_unavailable_commands(self, ctx):
        # Your logic to list the unavailable commands
        # This is just a static example
        return ['install-specific-command']

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command(cls=CustomHelpCommand)
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())

@cli.command()
def available_command():
    click.echo('This command is available by default.')

if __name__ == '__main__':
    cli()

```

In this example, the CustomHelpCommand class is created to inherit the Click's click.Command class. The format_commands method is overridden to include the unavailable commands in the help output. The list_unavailable_commands method is where you would provide the logic to list the unavailable commands. For this example, I've returned a static list of commands, but you can customize it as needed.

When you run the script and call the help command, it will show the default available commands and the custom unavailable commands sections.
