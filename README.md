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

apidocs are not currently part of the build, they can be generated for the
opencdms packeage by running the following command from the repo root:
`sphinx-apidoc -o docs/source/developer/apidocs/opencdms opencdms`
