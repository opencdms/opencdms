feature
====

Download the definition as a CSV file: :download:`csv <feature.csv>`.

.. csv-table:: Definition of the *feature* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _name:

   name","str",,"Optional","Name of feature."
   ".. _description:

   description","str",,"Optional","Description of feature."
   ".. _feature_type:

   feature_type","str","`reference_data.feature_type.id <../reference_data/feature_type.html#id>`_","Required","Feature type."
   ".. _geometry:

   geometry","Geography",,"Required","Location / geospatial geometry of feature."
   ".. _elevation:

   elevation","float",,"Optional","Mean elevation of feature above mean sea level."
   ".. _parent:

   parent","str","`master_data.feature.id <../master_data/feature.html#id>`_","Optional","Parent feature for this feature if nested."
   ".. _properties:

   properties","dict",,"Optional","Array of named values consistent with that defined for the feature type."
   ".. _links:

   links","dict",,"Optional","Link(s) to further information on feature."
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

