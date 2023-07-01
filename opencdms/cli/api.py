"""
In order to customise pygeoapi, we use the OpenCDMS CLI to call our own
implementation of flask_app.serve which replaces pygeoapi's default.

Usage:

pygeoapi_path="$(python3 -c "import pygeoapi; import os; print(os.path.dirname(os.path.dirname(pygeoapi.__file__)))")"
cp "$pygeoapi_path/pygeoapi-config.yml" example-config.yml
export PYGEOAPI_CONFIG=example-config.yml
export PYGEOAPI_OPENAPI=example-openapi.yml

# update paths to point at pygeoapi example data  (NOT WORKING? Use manual find and replace)
sed -i 's/, "tests/data/"/"$pygeoapi_path/tests/data/"/g' example-config.yml  # linux
sed -i '' 's|, "tests/data/"|, "'"$pygeoapi_path"'/tests/data/"|g' example-config.yml  # macOS

# enable, and set, template and static folder locations ($pygeoapi_path/pygeoapi/templates | static)
    # templates:
      # path: /path/to/Jinja2/templates
      # static: /path/to/static/folder # css/js/img

opencdms api openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI
opencdms api serve

# in another terminal
curl http://localhost:5000  # or open in a web browser

"""
import click

from pygeoapi.config import config
from pygeoapi.openapi import openapi

from opencdms.api.flask_app import serve


@click.group(invoke_without_command=True)
@click.pass_context
def api(context) -> None:
    pass


api.add_command(config)
api.add_command(openapi)
api.add_command(serve)
