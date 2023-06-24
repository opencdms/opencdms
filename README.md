This README file is maintained in the `/docs/source` directory of the main
`opencdms` repository.

  https://github.com/opencdms/opencdms

When the docs are built, this README is copied to the root directory of the
`gh-pages` branch along with the HTML documentation that is displayed at
docs.opencdms.org.

To build and deploy the documentation run the following command from the root
of the repository (assuming you have permissions to write to the repo):

```
pip install -r opencdms/requirements/docs.txt
cd docs
make deploy
```
