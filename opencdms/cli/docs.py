import click
import os
import sh
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler


@click.group()
def docs():
    pass


@docs.command()
@click.option('--port', '-p', default=8000, help='Port to serve documentation on.')
@click.option('--directory', '-d', default='docs/build/html', help='Directory to serve documentation from.')
def serve(port, directory):
    """Starts a simple web server to serve documentation."""
    os.chdir(directory)
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f'Serving documentation at http://localhost:{port}/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server...')
        httpd.server_close()
        sys.exit()


@docs.command()
def build(source_dir, build_dir):
    """Builds the documentation using Sphinx."""
    os.chdir(source_dir)
    try:
        sh.make('html')
        print('Documentation build successful.')
    except sh.ErrorReturnCode as e:
        print(f'Error building documentation: {e}', file=sys.stderr)
        sys.exit(1)