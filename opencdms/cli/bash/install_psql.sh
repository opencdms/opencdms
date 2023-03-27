#!/bin/bash

# Usage: ./install_psql.sh
# Install psql into the current environment

# Check psql is not already installed
if ! command -v psql &> /dev/null; then
    sudo apt-get update
    sudo apt-get install postgresql-client -y
    echo "psql installation completed."
else
    echo "psql is already installed, skipping installation."
fi
