:html_theme.sidebar_secondary.remove:

equipment_responsible_party
====

Download the definition as a CSV file: :download:`csv <equipment_responsible_party.csv>`.

.. csv-table:: Definition of the *equipment_responsible_party* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required",""
   ".. _equipment:

   equipment","str","`master_data.equipment.id <../master_data/equipment.html#id>`_","Required","The equipment that this record corresponds to."
   ".. _responsible_party:

   responsible_party","str","`master_data.responsible_party.id <../master_data/responsible_party.html#id>`_","Required","The responsible party associated with the record."
   ".. _role:

   role","str","`reference_data.role.id <../reference_data/role.html#id>`_","Required","The role the responsible party plays."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Date this record is valid from."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Date this record is valid to."
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

