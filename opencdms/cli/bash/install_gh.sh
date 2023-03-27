#!/bin/bash

# Usage: ./install_gh.sh
# Install GitHub CLI following the standard instructions at:
#   https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Check gh is not already installed
if ! command -v gh &> /dev/null; then
    type -p curl >/dev/null || sudo apt install curl -y
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && sudo apt update \
    && sudo apt install gh -y
    echo "GitHub CLI installation completed."
else
    echo "GitHub CLI is already installed, skipping installation."
fi