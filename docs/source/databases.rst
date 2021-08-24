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

TimescaleDB (PostgreSQL)
~~~~~~~~~~~~~~~~~~~~~~~~

Docker compose will provide an empty TimescaleDB/PostGIS instance. Database schemas for each CDMS will be created later using SQLAlchemy models in ``pyopencdms``. The resulting schemas should be equivalent to the original, but the underlying database technology may be different and, as a result, other minor difference will exist.

+------------------+-------------------+-----------------------------------------------------------------+
| CDMS             | Database          | Notes                                                           |
+==================+===================+=================================================================+
| clide            | TimescaleDB       | CliDE uses PostgreSQL, therefore high compatibility is expected |
+------------------+-------------------+-----------------------------------------------------------------+
| climsoft-4.1.1   | TimescaleDB       |                                                                 |
+------------------+-------------------+-----------------------------------------------------------------+
| mch-english      | TimescaleDB       |                                                                 |
+------------------+-------------------+-----------------------------------------------------------------+
| midas-core       | TimescaleDB       |                                                                 |
+------------------+-------------------+-----------------------------------------------------------------+

DB-Group
~~~~~~~~

Database schemas for each CDMS will be create using a database system that is compatible with the original database system using the original SQL DDL from the ``opencdms-test-data`` repository. For example:
1. MCH uses MySQL 5.1 in production, when using DB-group the SQL DDL will be restored to MariaDB 1.1
2. MIDAS uses Oracle Enterprise or Standard Edition in productions, when using DB-group the SQL DDL will be restore to Oracle eXpression Edition (XE)
each support CDMS

+------------------+-------------------+-----------------------------------------------------------------+
| CDMS             | Database          | Notes                                                           |
+==================+===================+=================================================================+
| clide            | TimescaleDB       | CliDE uses PostgreSQL, therefore high compatibility is expected |
+------------------+-------------------+-----------------------------------------------------------------+
| climsoft-4.1.1   | MariaDB 10.1      | Climsoft 4.x uses MariaDB 10.1 in production                    |
+------------------+-------------------+-----------------------------------------------------------------+
| mch-english      | MariaDB 10.1      |                                                                 |
+------------------+-------------------+-----------------------------------------------------------------+
| midas            | Oracle XE         | *Experimental*                                                  |
+------------------+-------------------+-----------------------------------------------------------------+


Production
~~~~~~~~~~

For some supported CDMSs, docker images exist for the exact database and version number that is commonly used in production:

+------------------+---------------------------------------+------------------------------------+
| CDMS             | Database                              | Notes                              |
+==================+=======================================+====================================+
| clide            | PostgreSQL 13                         | *PostgreSQL version not confirmed* |
+------------------+---------------------------------------+------------------------------------+
| climsoft-4.1.1   | MariaDB 10.1                          |                                    |
+------------------+---------------------------------------+------------------------------------+
| MCH-english      | MySQL 5.1.73                          | *Experimental*                     |
+------------------+---------------------------------------+------------------------------------+
| MIDAS            | Oracle Enterprise or Standard Edition | **Not available**                 |
+------------------+---------------------------------------+------------------------------------+
