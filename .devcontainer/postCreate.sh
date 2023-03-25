# Link the .devcontainer README.md to our workspaces root so that it
# previews automatically when the devcontainer starts.
ln -s /workspaces/opencdms/.devcontainer/README.md /workspaces/

cp /workspaces/opencdms/.devcontainer/.bash_aliases ~/
source /workspaces/opencdms/.devcontainer/.bash_aliases

# Setup opencdms cli ready for further setup
#pip3 install -e /workspaces/opencdms

# TODO: The following setup will be moved to opencdms cli

git clone https://github.com/opencdms/pyopencdms
git clone https://github.com/opencdms/opencdms-app
git clone https://github.com/opencdms/opencdms-api
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

pip3 install -e /workspaces/pyopencdms
## pip3 install -e /workspaces/opencdms-api
## pip3 install -e /workspaces/opencdms-workshop

# TODO: Run requirement-dev as setup option
#pip install -r /workspaces/pyopencdms/requirement-dev.txt
