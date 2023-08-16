:html_theme.sidebar_secondary.remove:

deployment_responsible_party
====

Download the definition as a CSV file: :download:`csv <deployment_responsible_party.csv>`.

.. csv-table:: Definition of the *deployment_responsible_party* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","Unique identifier for this record."
   ".. _responsible_party:

   responsible_party","str","`master_data.responsible_party.id <../master_data/responsible_party.html#id>`_","Required","The responsible party."
   ".. _role:

   role","str","`reference_data.role.id <../reference_data/role.html#id>`_","Required","The role this responsible party plays."
   ".. _deployment:

   deployment","str","`master_data.deployment.id <../master_data/deployment.html#id>`_","Required","The deployment that this record corresponds to."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date this record is valid from."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Date this record is valid to."
   ".. _version:

   _version","int",,"Required","Version number of this record."
   ".. _change_date:

   _change_date","datetime",,"Required","Date this record was changed."
   ".. _user:

   _user","str","`master_data.user.id <../master_data/user.html#id>`_","Required","Which user/agent last modified this record."
   ".. _status:

   _status","str","`master_data.status.id <../master_data/status.html#id>`_","Required","Whether this is the latest version or an archived version of the record."
   ".. _comments:

   _comments","str",,"Required","Free text comments on this record, for example description of changes made etc."

