import os
import socket
import docker


def check_port(port: int, address: str = 'localhost') -> bool:
    """
    Check if a TCP port is open on a given address.

    Args:
        port (int): The port number to check. Must be between 0 and 65535.
        address (str, optional): The address to check, in the form of a string.
            Defaults to 'localhost'.

    Returns:
        bool: True if the port is open, False otherwise.

    Raises:
        ValueError: If the port number is outside the valid range.
    """
    if port < 0 or port > 65535:
        raise ValueError("Port number must be between 0 and 65535.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((address, port)) == 0


# TODO: codespaces version not working
def check_container_port(port: int, address: str = 'localhost') -> bool:
    """
    Check if a TCP port is open on a given address.

    Args:
        port (int): The port number to check. Must be between 0 and 65535.
        address (str, optional): The address to check, in the form of a string.
            Defaults to 'localhost'.

    Returns:
        bool: True if the port is open, False otherwise.

    Raises:
        ValueError: If the port number is outside the valid range.
        RuntimeError: If the function is unable to retrieve the IP address of the container.
    """
    if port < 0 or port > 65535:
        raise ValueError("Port number must be between 0 and 65535.")

    if 'CODESPACES' in os.environ or 'REMOTE_CONTAINERS' in os.environ:
        container_name = os.environ.get('HOSTNAME')
        if not container_name:
            raise RuntimeError("Could not retrieve container name.")

        client = docker.DockerClient()
        container = client.containers.get(container_name)
        container_ip = container.attrs['NetworkSettings']['IPAddress']
        address = container_ip

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((address, port)) == 0
