:html_theme.sidebar_secondary.remove:

source_type
====

Download the definition as a CSV file: :download:`csv <source_type.csv>`.

.. csv-table:: Definition of the *source_type* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _inScheme:

   inScheme","str",,"Required","The scheme/vocabulary that this record is from."
   ".. _name:

   name","str",,"Required","Name of source type"
   ".. _description:

   description","str",,"Required","Description of source type, e.g. file etc"
   ".. _IANA_scheme:

   IANA_scheme","str",,"Optional","IANA scheme (if applicable)"
   ".. _links:

   links","str",,"Optional","Links providing further definition of source type"
   ".. _version:

   _version","int",,"Required","Version number of this record"
   ".. _change_date:

   _change_date","datetime",,"Required","Date this record was changed"
   ".. _user:

   _user","str","`admin.user.id <../admin/user.html#id>`_","Required","Which user/agent last modified this record"
   ".. _status:

   _status","str","`reference_data.status.id <../reference_data/status.html#id>`_","Required","Whether this is the latest version or an archived version of the record"
   ".. _comments:

   _comments","str",,"Required","Free text comments on this record, for example description of changes made etc"

