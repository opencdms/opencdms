OpenCDMS Architecture
=====================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

Containers
==========
The C4 container diagram below shows the main components in the OpenCDMS software.
These are described in more detail below.

.. plantuml:: ./containers.puml

opencdms-app
------------
This container is the main interface for interacting with the OpenCDMS software, including data entry, data
and metadata management, system configuration, and visualisation.


opencdms-api
------------
This container implements OGC-APIs for access to the data and metadata, including processes. These are implemented
via pygeoapi.

pyopencdms
----------
This container acts as an event handler, listening for events via the message broker. Scheduled events also run on this
container. Interaction with the data occurs via the opencdms-api container.

Datastore
---------
This container hosts the backend database for storing the climate data and metadata as well as configuration settings.

File bucket
-----------
S3 compatible object store. Used for incoming data for providing static files to external services.

Message broker
--------------
Internal message broker for event driven workflows. This can also be used for connecting with the WIS2.0.
