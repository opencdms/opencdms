host_alias
====

Download the definition as a CSV file: :download:`csv <host_alias.csv>`.

.. csv-table:: Definition of the *host_alias* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","Primary key for this record."
   ".. _host:

   host","str","`master_data.host.id <../master_data/host.html#id>`_","Required","Primary ID by which the host is known."
   ".. _alternative_id:

   alternative_id","str",,"Optional","Alternative ID by which the host is known."
   ".. _alternative_name:

   alternative_name","str",,"Optional","Alternative name by which the host is known."
   ".. _alternative_authority:

   alternative_authority","str",,"Optional","ID scheme / authority assigning alternative ID."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date the alternative id/name was used from."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Last date the alternative id/name was used."
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

