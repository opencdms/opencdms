import click
import os
import sh
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

# ensure sphinx is importable (if not the error will be caught by cli)
import sphinx

from opencdms.utils.paths import docs_path


@click.group()
def docs():
    """Includes commands to build and serve docs"""
    pass


@docs.command()
@click.option('--port', '-p', default=48008, help='Port to serve documentation on (default 48008).')
def serve(port):
    """Starts a simple web server to serve documentation."""
    os.chdir(docs_path('html'))
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f'Serving documentation at http://localhost:{port}/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server...')
        httpd.server_close()
        sys.exit()


@docs.command()
def build():
    """Builds the documentation using Sphinx."""
    try:
        sh.make('html', directory=docs_path())
        print('Documentation build successful.')
    except sh.ErrorReturnCode as e:
        print(f'Error building documentation: {e}', file=sys.stderr)
        sys.exit(1)
