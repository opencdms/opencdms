# Overview

Instead of forking pygeoapi, we install the pygeoapi package (in
`/opencdms/requirements/api.txt`) and we pin to a specific version.

The steps below then describe the customization process.

### flask_app.py ✓

Usually, when you run `pygeoapi serve` this uses `pygeoapi.flask_app:serve`
to run a development server locally.

In order to make customisations to the package, we have to use our own version
of `flask_app`. Currently, to achieve this, we use the OpenCDMS command line
interface instead of using the `pygeoapi` CLI. The command `opencdms api serve`
calls our version of `flask_app.py` and this version decides whether to import
customized versions of files, or just to import the original versions directly
from `pygeoapi`.

### api.py ✓

Instead of creating a copy of `api.py` and modifying the file we can inherit
from the `API` class and extend its behaviour. For this reason we use the
filename `api_extended.py` and, instead of using the `API` class, we use the
`APIExtended` class.

Discounting the pygeoapi tests (and the Django and starlette implementations)
the API class is only imported by `flask_app.py`

### requirements.txt

This file currently contains a slightly modified version of pygeoapi
dependencies. However, when we `pip install pygeoapi` our local
`requirements.txt` is currently ignored.
