## OpenCDMS Python Package

This directory contains the `opencdms` package that can be downloaded
from the [Python Package Index (PyPI)](https://pypi.org/project/opencdms/)
and then imported using `import opencdms`.

The package includes subpackages for:
* `adapters` - Concreate implementations of opencdms.models
* `cli` - The `opencdms` command line interface
* `integrations` - Adapters for other software like pygeoapi
* `models` - Our Reference Implementation of the WMO Climate Data Model standard
* `requirements` - Software dependencies for each subpackage
* `utils` - Reusable utilities

Depending on which subpackage(s) you use, you may need to install additional dependencies, see:

    `opencdms install --help`

📚 See [docs.opencdms.org/developer/installation][developer] for more information

[developer]: https://docs.opencdms.org/developer/installation
