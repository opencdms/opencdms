# Link the .devcontainer README.md to our workspaces root so that it
# previews automatically when the devcontainer starts.
ln -s /workspaces/opencdms/.devcontainer/README.md /workspaces/

cp /workspaces/opencdms/.devcontainer/.bash_aliases ~/
source /workspaces/opencdms/.devcontainer/.bash_aliases

git clone https://github.com/opencdms/pyopencdms
git clone https://github.com/opencdms/opencdms-app
git clone https://github.com/opencdms/opencdms-api
git clone https://github.com/opencdms/opencdms-test-data
git clone https://github.com/opencdms/opencdms-workshop

pip3 install -e /workspaces/pyopencdms
# pip3 install -e /workspaces/opencdms-api
pip3 install -e /workspaces/opencdms-workshop
