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

# Let's leave our users in the opencdms workspace, otherwise
# launching Python and typing `import opencdms` imports the
# directory, not the Python package (need to see if we can
# make the directory unimportable)
cd /workspaces/opencdms