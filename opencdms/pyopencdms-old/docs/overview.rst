======================
Overview of pyopencdms
======================

The `pyopencdms` package is a Python implementation of the Climate Data Mangement System (CDMS)
specificiations, `WMO No. 1131 <lhttps://library.wmo.int/index.php?lvl=notice_display&id=16300>`_.

These specifications, that outline the high-level business logic required of a CDMS,
are implemented in `pyopencdms` following Domain Driven Design (DDD) principles.

`Domain-driven design <https://en.wikipedia.org/wiki/Domain-driven_design>`_ is a
software design approach that focuses on modeling software to match a domain according to
input from that domain's experts.

Domain Models
-------------

We start by representing the `Climate Data Model (CDM) Standard <https://github.com/wmo-im/tt-cdm>`_
as a set of Python `data classes <https://docs.python.org/3/library/dataclasses.html>`_.

.. mermaid::

   ---
   title: Example data classes
   ---
   classDiagram
    DomainModel <|-- Observation
    DomainModel <|-- Host

    class DomainModel{
        +table_info()
        +column_info(column)
    }
    class Observation{
        -str location
        -float elevation
        -int observation_type_id
        -str host_id
        +ingest(observations)
    }
    class Host{
        -str id
        -str name
        -str description
        -str location
        -float elevation
    }

In the Observation() class above, we can see that the process of adding/creating/saving new observations is 
referred to as `ingest()`. This is an example of using the common language (or "ubiquitous language")
shared by domain experts, users, and developers.

In this case, data ingestion is a term commonly used in Climate Data Management Systems and is also
a component of the Climate Data Management Systems Specifications (`5.1.1 <https://spec.opencdms.org/cdms/v1.0/5.1/>`_).

In addition to storing data, the `ingest` method on the Observation class is responsible for ensuring that the
data that is to be ingested is valid.

Like the other methods in the Domain Model, the `ingest` method is implemented independently of any
database backend. The specifics of how the data is stored will depend on the backend being used.

In fact, the `pyopencdms` package can be used without any database backend. This is especially useful
in cases where you are not making use of a database and are working with data that is exchanged in the
Climate Data Model Standard's JSON exchange format.


Provider plugins
----------------

The provider plugins are responsible for implementing the domain model for a specific storage backend.

This section looks at the `opencdmsdb` provider plugin, which is the default, and we also look at the
`surface` provider plugin.

opencdmsdb provider plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^

The `opencdmsdb` provider SQLAlchemy to manage an implementation of the domain models that uses PostgreSQL
with the TimescaleDB and PostGIS extensions.

SURFACE provider plugin
^^^^^^^^^^^^^^^^^^^^^^^

The `surface` provider providers mappings between the domain models and the SURFACE data model using
the Django ORM which is used in SURFACE.
