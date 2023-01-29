Database technologies
=====================

Configuration
-------------

Default configuration
~~~~~~~~~~~~~~~~~~~~~

By default, unit tests and other code run will run against an in-memory
SQLite database (a warning should be given that a database has not been configured).

User-specified configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user creates a configuration object with details of available
database connections.

Docker
------

Note: Containers are currently not configured to provide persistent storage (i.e. to store data outside of the container)

opencdms-db image
~~~~~~~~~~~~~~~~~

Initially ``opencdms-db`` will provide an empty TimescaleDB/PostGIS database instance.

Database schemas for each supported CDMS can be created later within an ``opencdms-db`` container using SQLAlchemy models
in ``pyopencdms``. The resulting schemas should be equivalent to the originals, but the underlying database technology may
be different and, as a result, other minor difference may exist.

+------------------+------------------------+------------------------------+
| Image            | Database               | Notes                        |
+==================+========================+==============================+
| opencdms-db      | TimescaleDB/PostGIS    | Empty database server        |
+------------------+------------------------+------------------------------+


Database groups
~~~~~~~~~~~~~~~

Database schemas for each CDMS can be created using a database system that is compatible with the original database system
using the original SQL DDL from the ``opencdms-test-data`` repository. When using docker compose the database schema will
be restored. For example:

#. MCH uses MySQL 5.1 in production, when using DB-group the SQL DDL will be restored to MariaDB 1.1.
#. MIDAS uses Oracle Enterprise or Standard Edition in production, when using database groups the SQL DDL will be restored to Oracle eXpression Edition (XE)

+------------------+------------------------+------------------------------+
| Image            | Database               | Notes                        |
+==================+========================+==============================+
| postgres         | PostgreSQL 13          | CliDE, Belize SURFACE        |
+------------------+------------------------+------------------------------+
| mysql            | MySQL 8                | climsoft-4.1.1, mch-english  |
+------------------+------------------------+------------------------------+
| oracle-xe        | Oracle XE 11g          | midas-code (experimental)    |
+------------------+------------------------+------------------------------+


Production
~~~~~~~~~~

For some supported CDMSs, docker images exist for the exact databases and version numbers that are commonly used in production.

In each case, only one CDMS schema is restored.

+------------------+---------------------------------------+------------------------------------+
| CDMS             | Database                              | Notes                              |
+==================+=======================================+====================================+
| belize-surface   | TimescaleDB                           |                                    |
+------------------+---------------------------------------+------------------------------------+
| clide            | PostgreSQL 13                         | *PostgreSQL version not confirmed* |
+------------------+---------------------------------------+------------------------------------+
| climsoft-4.1.1   | MariaDB 10.1                          |                                    |
+------------------+---------------------------------------+------------------------------------+
| mch-english      | MySQL 5.1.73                          | *Experimental*                     |
+------------------+---------------------------------------+------------------------------------+
| midas-core       | Oracle Enterprise or Standard Edition | **Not available**                  |
+------------------+---------------------------------------+------------------------------------+

