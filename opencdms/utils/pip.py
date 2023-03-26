import sh
from opencdms.utils.paths import requirements_file

def install_requirements(requirements_file):
    # Construct the pip command to install the package
    pip_cmd = ['pip', 'install', package_name]

    # Run the pip command and capture the output
    output = sp.run(pip_cmd, capture_output=True)

    # Print the output to the console
    click.echo(output.stdout.decode('utf-8'))