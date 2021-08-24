Database technologies
=====================

Configuration
-------------

Default
~~~~~~~

By default, unit tests and other code run will run against an in-memory
SQLite database (a warning should be given).

User specified
^^^^^^^^^^^^^^

The user creates a configuration object with details of available
database connections.

Docker
------

TimescaleDB (PostgreSQL)
~~~~~~~~~~~~~~~~~~~~~~~~

``pyopencdms`` using SQLAlchemy and alembic

DB-Group
~~~~~~~~

The ``opencdms-test-data`` repository contains the original SQL DDL for
each support CDMS

db-group/

Restore from original DDL

+------------------+-------------------+----------------+
| CDMS             | Database          | Notes          |
+==================+===================+================+
| clide            | Timescale         |
+------------------+-------------------+----------------+
| climsoft-4.1.1   | MariaDB 10.1 \*   |                |
+------------------+-------------------+----------------+
| MCH-english      | MySQL 5.1.73      | Experimental   |
+------------------+-------------------+----------------+

Production
~~~~~~~~~~

production/docker-compose.yml

+------------------+-----------------+----------------------------------+
| CDMS             | Database        | Notes                            |
+==================+=================+==================================+
| clide            | PostgreSQL 13   | Postgres version not confirmed   |
+------------------+-----------------+----------------------------------+
| climsoft-4.1.1   | MariaDB 10.1    |                                  |
+------------------+-----------------+----------------------------------+
| MCH-english      | MySQL 5.1.73    | Experimental                     |
+------------------+-----------------+----------------------------------+

