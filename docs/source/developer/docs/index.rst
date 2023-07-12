Updating the docs
=================

To build the docs locally:

.. code-block:: shell

    python3 -m venv venv
    cd venv
    . bin/activate
    git clone https://github.com/opencdms/opencdms
    cd opencdms/docs

    pip install -r ../opencdms/requirements/docs.txt
    make html


To build and deploy the docs, follow the instructions above and use:

.. code-block:: shell

    make deploy
