:html_theme.sidebar_secondary.remove:

host
====

Download the definition as a CSV file: :download:`csv <host.csv>`.

.. csv-table:: Definition of the *host* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _name:

   name","str",,"Required","Preferred name of host."
   ".. _description:

   description","str",,"Optional","Description of host."
   ".. _links:

   links","dict",,"Optional","URI to host, e.g. to OSCAR/Surface."
   ".. _wigos_station_identifier:

   wigos_station_identifier","str",,"Optional","WIGOS station identifier."
   ".. _facility_type:

   facility_type","str","`reference_data.facility_type.id <../reference_data/facility_type.html#id>`_","Optional","Type of observing facility, fixed land, mobile sea, etc."
   ".. _date_established:

   date_established","datetime",,"Optional","Date host was first established."
   ".. _date_closed:

   date_closed","datetime",,"Optional","Date host was first established."
   ".. _wmo_region:

   wmo_region","str","`reference_data.wmo_region.id <../reference_data/wmo_region.html#id>`_","Optional","WMO region in which the host is located."
   ".. _territory:

   territory","str","`reference_data.territory.id <../reference_data/territory.html#id>`_","Optional","Territory the host is located in."
   ".. _time_zone:

   time_zone","str","`reference_data.time_zone.id <../reference_data/time_zone.html#id>`_","Optional","Time zone the host is located in."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date from which the details for this record are valid."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Date after which the details for this record are no longer valid."
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

