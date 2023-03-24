import subprocess


def command_exists(cmd):
    """
    Check if a given command exists.

    Args:
        cmd (str): The command to check for existence.

    Returns:
        bool: True if the command exists, False otherwise.
    """
    try:
        subprocess.check_output(["which", cmd])
        return True
    except subprocess.CalledProcessError:
        return False
