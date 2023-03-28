import os
import re
import subprocess


# TODO: Add tests, especially for line beginning `-r` and requirements coming
#       from web and git, e.g.
#       `-r more_requirements.txt` and
#       `-r https://github.com/org/repo/requirements.txt`.
#       `opencdms@git+https://github.com/opencdms/pyopencdms@main`


def check_requirements(filepath: str, verbose: bool = False) -> List[str]:
    """
    Check if all packages specified in a requirements file have been installed.

    Args:
        filepath: The path to the requirements file to check.
        verbose: Whether to print out each package that has been found or not. Defaults to False.

    Returns:
        A list of package names that are not installed.
    """
    # Read the requirements file
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Process the lines in the requirements file
    not_installed = []
    for line in lines:
        line = line.strip()
        # Check if the line is a requirement file reference
        if line.startswith('-r'):
            # If so, recursively process the referenced file
            # Note that we also support remote files over HTTPS
            ref_path = line.split(' ')[1]
            if ref_path.startswith('http') or ref_path.startswith('https'):
                # Download the remote file to a temporary location
                ref_filename = os.path.basename(ref_path)
                subprocess.run(['curl', '-sSL', '-o', ref_filename, ref_path], check=True)
                # Recursively process the downloaded file
                ref_not_installed = check_requirements_file(ref_filename, verbose)
                # Delete the temporary file
                os.remove(ref_filename)
            else:
                # Recursively process the referenced file
                ref_not_installed = check_requirements_file(ref_path, verbose)
            # Add any packages not installed in the referenced file to the list
            not_installed.extend(ref_not_installed)
        # Check if the line is a Git repo reference
        elif 'git+' in line:
            # Extract the package name from the Git repo URL
            package_name = re.search(r'\/([^\/]+)\.git', line).group(1)
            # Check if the package is installed
            try:
                subprocess.run(['pip', 'show', package_name], check=True, stdout=subprocess.PIPE)
                if verbose:
                    print(f'Found package: {package_name}')
            except subprocess.CalledProcessError:
                # If not, add it to the list
                not_installed.append(package_name)
                if verbose:
                    print(f'Missing package: {package_name}')
        # Check if the line is a package reference
        elif line and not line.startswith('#'):
            # Extract the package name and version, if present
            package_name = line.split('==')[0]
            # Check if the package is installed
            try:
                subprocess.run(['pip', 'show', package_name], check=True, stdout=subprocess.PIPE)
                if verbose:
                    print(f'Found package: {package_name}')
            except subprocess.CalledProcessError:
                # If not, add it to the list
                not_installed.append(package_name)
                if verbose:
                    print(f'Missing package: {package_name}')

    return not_installed
    