"""
sudo apt-get update
sudo apt-get install ansible
pip install ansible-runner

"""
import os
from ansible_runner import run

# Set the path to the directory containing the playbook
playbook_path = os.path.abspath('install-gh-cli.yml')
inventory='localhost,'
options={'inventory': inventory, 'extravars': {'ansible_python_interpreter': '/usr/bin/python3'}, 'debug': True}
run(playbook=playbook_path, **options)

'''
# Create the runner object
runner = ansible_runner.run(
    private_data_dir=".",
    playbook=playbook,
    inventory=inventory,
)

# Print the results
print(runner.status)
print(runner.stdout)
print(runner.stderr)
'''
