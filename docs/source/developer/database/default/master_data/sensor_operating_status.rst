:html_theme.sidebar_secondary.remove:

sensor_operating_status
====

Download the definition as a CSV file: :download:`csv <sensor_operating_status.csv>`.

.. csv-table:: Definition of the *sensor_operating_status* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","Primary key for this record."
   ".. _deployment:

   deployment","str","`master_data.deployment.id <../master_data/deployment.html#id>`_","Required","The deployment this record belongs to."
   ".. _operating_status:

   operating_status","str","`reference_data.operating_status.id <../reference_data/operating_status.html#id>`_","Required","The operating status of the deployed equipment."
   ".. _valid_from:

   valid_from","datetime",,"Optional","The date from which this status applies."
   ".. _valid_to:

   valid_to","datetime",,"Optional","The date from which this status is no longer valid."
   ".. _version:

   _version","int",,"Required","Version number of this record."
   ".. _change_date:

   _change_date","datetime",,"Required","Date this record was changed."
   ".. _user:

   _user","str","`admin.user.id <../admin/user.html#id>`_","Required","Which user/agent last modified this record."
   ".. _status:

   _status","str","`reference_data.status.id <../reference_data/status.html#id>`_","Required","Whether this is the latest version or an archived version of the record."
   ".. _comments:

   comments","str",,"Required","Free text comments on this record, for example description of changes made etc."

