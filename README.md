# OpenCDMS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This repository contains, in a single place, everything that is needed to install the OpenCDMS software and also includes the source of the documentation that is published at [docs.opencdms.org](https://docs.opencdms.org).

```
# First use pip to install the `opencdms` command line tool
pip install opencdms

# Then install all dependencies into current environment (see opencdms/requirements/)
opencdms install

```

**Note:** If you are developing locally, it is recommended to create a virtual environment before installing all of the opencdms dependencies, you can do this with the following commands:
```
# Create a venv directory to contain the virtual environment
python3 -m venv venv

# Activate the virtual environment
source ./venv/bin/activate

pip install opencdms
opencdms install

```
