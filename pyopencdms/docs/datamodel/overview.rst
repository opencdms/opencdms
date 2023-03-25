=====================================
OpenCDMS Physical Data Model Overview
=====================================

The OpenCDMS physical data model is conceptualized in layers made up of base tables and derived tables.

The data model currently consists of the following layers:

Climate Data Model
==================

This layer contains our implementation of the WMO Climate Data Model Standard.
This layer can be used independently of the other layers and can either be realised as
a relational database for long-term storage and management
or as a set of files for data exchange.

Application database
====================

This layer contains user specific information and application configuration. It is only
required if OpenCDMS is being used as a web application. It is possible to interact with
the Climate Data Model layer without requiring this or other layers.

Derived tables
==============

The derived tables layer consists of a set of tables that are derived from the base tables.
These tables do not store data directly and are implemented as views in the database.

There are two occassions where derived tables are used:

- To assist with the creation of products and services that are derived from the Climate Data Model
- To transform other supported CDMS data models so that they look at behave like their OpenCDMS equivalent

Access control
==============

The final layer contains additional tables that are required to support access control. Access control
is applied to all other layers.
