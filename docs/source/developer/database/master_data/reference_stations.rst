reference_stations
====

Download the definition as a CSV file: :download:`csv <reference_stations.csv>`.

.. csv-table:: Definition of the *reference_stations* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key for this record."
   ".. _host:

   host","str","`master_data.host.id <../master_data/host.html#id>`_","Optional","The host / station this record is for."
   ".. _reference_station:

   reference_station","str","`master_data.host.id <../master_data/host.html#id>`_","Optional","The host / station acting as a reference station."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date the reference station started as a reference station for this host."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Date the reference station stopped as a reference station for this host."
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

