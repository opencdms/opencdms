:html_theme.sidebar_secondary.remove:

host_affiliation
====

Download the definition as a CSV file: :download:`csv <host_affiliation.csv>`.

.. csv-table:: Definition of the *host_affiliation* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","Primary key for this record."
   ".. _host:

   host","str","`master_data.host.id <../master_data/host.html#id>`_","Required","Host described by this record."
   ".. _program:

   program","str","`reference_data.observing_program.id <../reference_data/observing_program.html#id>`_","Optional","Observing program that this host is affiliated with."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date from which the details for this record are valid."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Date after which the details for this record are no longer valid."
   ".. _reporting_status:

   reporting_status","str",,"Optional","Declared reporting status of an observing facility with respect to a certain program/network affiliation."
   ".. _program_specific_id:

   program_specific_id","str","`master_data.host_aliases.alternative_id <../master_data/host_aliases.html#alternative_id>`_","Optional","WIGOS station identifier."
   ".. _version:

   _version","int",,"Required","Version number of this record."
   ".. _change_date:

   _change_date","datetime",,"Required","Date this record was changed."
   ".. _user:

   _user","str","`admin.user.id <../admin/user.html#id>`_","Required","Which user/agent last modified this record."
   ".. _status:

   _status","str","`reference_data.status.id <../reference_data/status.html#id>`_","Required","Whether this is the latest version or an archived version of the record."
   ".. _comments:

   _comments","str",,"Required","Free text comments on this record, for example description of changes made etc."

