:html_theme.sidebar_secondary.remove:

territory
====

Download the definition as a CSV file: :download:`csv <territory.csv>`.

.. csv-table:: Definition of the *territory* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _inScheme:

   inScheme","str",,"Required","The scheme/vocabulary that this record is from."
   ".. _name:

   name","str",,"Required","Short name / abbreviation for the territory."
   ".. _description:

   description","str",,"Required","Official name of territory."
   ".. _ISO3c:

   ISO3c","str",,"Required","ISO 3 character country code."
   ".. _wmo_region:

   wmo_region","str","`reference_data.wmo_region.id <../reference_data/wmo_region.html#id>`_","Optional","WMO region that represents the territory."
   ".. _links:

   links","dict",,"Optional","Link(s) to further information."
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

