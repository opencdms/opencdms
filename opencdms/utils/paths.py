import os
import sys


def config_directory(package_name='opencdms'):
    """Get the path to the configuration directory for the specified package.

    This function returns the path to the configuration directory for the specified package,
    using the XDG Base Directory Specification. If the $XDG_CONFIG_HOME environment variable
    is set, the configuration directory will be located there. Otherwise, the configuration
    directory will be located in the default location, ~/.config/package_name/. If the directory
    does not exist, it will be created.

    Args:
        package_name (str, optional): The name of the package. Defaults to 'opencdms'.

    Returns:
        str: The path to the configuration directory for the specified package.
    """
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME')
    if xdg_config_home:
        config_dir = os.path.join(xdg_config_home, package_name)
    else:
        config_dir = os.path.expanduser(f'~/.config/{package_name}')

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    return config_dir


def base_path(path: str = ''):
    """Returns the required path for the opencdms package.

    Args:
        path (str): Optional directory path to append to the base path.

    Returns:
        str: The requested path.
    """
    module_path = os.path.dirname(sys.modules['opencdms'].__file__)
    path = os.path.abspath(os.path.join(module_path, path))
    return path


def requirements_path(name: str):
    """Returns the path for the named requirements file.

    Args:
        name (str): Name of requirements file

    Returns:
        str: The path to the requirements file.

    """
    full_name = f'{name}.txt' if not name.endswith('txt') else 'name'
    return base_path(f'requirements/{full_name}')


def tests_path(name: str = ''):
    """Returns the tests path.

    Args:
        name (str): Optional, limit to 'unit|integration'

    Returns:
        str: The required path

    """
    # TODO: if package installed with pip then tests won't be available
    return base_path(f'../tests/{name}')


def docs_path(name: str = ''):
    """Returns the path to the docs directory.

    Args:
        name (str): Optionally request 'source|build|html'

    Returns:
        str: The required path

    """
    append = {
        '': '',
        'source': 'source',
        'build': 'build',
        'html': 'build/html',
    }
    return base_path(f'../docs/{append[name]}')
