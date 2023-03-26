#!/bin/bash

# Usage: ./install_docker.sh
# Install docker engine following the standard instructions at:
#   https://docs.docker.com/engine/install/debian/#install-using-the-repository

# Check Docker is not already installed
if ! command -v docker &> /dev/null; then
  sudo apt-get update
  sudo apt-get install ca-certificates curl gnupg

  sudo mkdir -m 0755 -p /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

  echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  echo "Docker installation completed."
else
    echo "Docker is already installed, skipping installation."
fi
