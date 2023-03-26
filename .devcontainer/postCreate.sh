# Link the .devcontainer README.md to our workspaces root so that it
# previews automatically when the devcontainer starts.
ln -s /workspaces/opencdms/.devcontainer/README.md /workspaces/

cp /workspaces/opencdms/.devcontainer/.bash_aliases ~/
source /workspaces/opencdms/.devcontainer/.bash_aliases

# Setup opencdms cli ready for further setup
pip3 install -e /workspaces/opencdms

# TODO: The following dev setup will be moved to opencdms cli
#       and will also be used to create prebuilt containers on ghcr.io
#       for each software release from 0.2.0 onwards
git clone https://github.com/geopython/pygeoapi
git clone https://github.com/opencdms/opencdms-app
git clone https://github.com/opencdms/opencdms-test-data
git clone https://github.com/opencdms/opencdms-test-databases
git clone https://github.com/opencdms/opencdms-workshop

# Setup gh cli
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y

# For development we want editable versions of the installed packages
# even if `opencdms install` is ran later
pip3 install -e /workspaces/pygeoapi
pip3 install -e /workspaces/opencdms-test-databases

#pip3 install -r /workspaces/pygeoapi/requirements-dev.txt
#pip3 install -r /workspaces/pygeoapi/requirements-django.txt
#pip3 install -r /workspaces/pygeoapi/requirements-docker.txt
# this one takes a long time (especially installing pandas?)
#pip3 install -r /workspaces/pygeoapi/requirements-provider.txt

## pip3 install -e /workspaces/opencdms-api
## pip3 install -e /workspaces/opencdms-workshop

# TODO: Run requirement-dev as setup option
#pip install -r /workspaces/pyopencdms/requirement-dev.txt
