OpenCDMS default database
=========================
The OpenCDMS database includes several schemas:

- *master_data*: A collection of tables containing the observations and metadata on the observations, such as sensor and station information.
- *reference_data*: A collection of tables defining code lists / controlled vocabulary referenced by the *master_data* tables.
- *admin*: A series of tables containing administrative information, not publicly available.

Each of the tables defined within the database, both in the *master_data* and *reference_data* schemas, include
elements to record the history of changes for each row to enable
a full tracking of the provenance of a record after it enters the CDMS. When a record is changed the previous is archived
together with the following information:

- *version*: A version number associated with each version of the record.
- *change date*: The data and time the change was made / applied.
- *user / agent*: The user or agent (e.g. automated computer process) responsible for the change.
- *status*: The status of the record, e.g. raw, provisional, final, archived etc.
- *comments / description*: A description of the changes made and the reasons why.

The main method for interacting with the data contained in the CDMS is via its API. The definition of the API can be
found at: `API definition  <./CDM/index.html>`_.

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Schemas:

   master_data
   reference_data
