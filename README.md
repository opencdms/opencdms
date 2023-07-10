# OpenCDMS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This repository contains, in a single place, everything that is needed to install the OpenCDMS software and also includes the source of the documentation that is published at [docs.opencdms.org](https://docs.opencdms.org).

## Installation

If you want to install OpenCDMS for production use, please see the instructions at https://docs.opencdms.org/administrator.

To set up containers see install/docker-compose.yaml

If you are just interested in working with the OpenCDMS Python package locally then follow the instructions below.

```
# First use pip to install the `opencdms` command line tool
pip install opencdms

# Then install all dependencies into current environment
opencdms install

```

**Note:** If you are developing locally, it is recommended to create a virtual environment before installing all of the opencdms dependencies, you can do this with the following commands:
```
# Create a venv directory to contain the virtual environment
python3 -m venv venv

# Activate the virtual environment
source ./venv/bin/activate

```

To obtain the latest version of the software, clone the repository directly from GitHub:
```
pip uninstall opencdms
git clone https://github.com/opencdms/opencdms.git
pip install -e opencdms
opencdms install

```
