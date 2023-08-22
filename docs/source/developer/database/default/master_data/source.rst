:html_theme.sidebar_secondary.remove:

source
====

Download the definition as a CSV file: :download:`csv <source.csv>`.

.. csv-table:: Definition of the *source* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _name:

   name","str",,"Required","Name of source."
   ".. _description:

   description","str",,"Required","Description of source type, e.g. file etc."
   ".. _source_type:

   source_type","str","`reference_data.source_type.id <../reference_data/source_type.html#id>`_","Required","The type of source."
   ".. _links:

   links","dict",,"Optional","Link(s) to further information on source."
   ".. _processor:

   processor","str",,"Optional","Name of processor used to ingest the data."
   ".. _parameters:

   parameters","dict",,"Optional","Parameters required to access the data from this source (NEED TO CHECK THIS, ENCRYPT?)."
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

