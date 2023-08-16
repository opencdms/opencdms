:html_theme.sidebar_secondary.remove:

responsible_party
====

Download the definition as a CSV file: :download:`csv <responsible_party.csv>`.

.. csv-table:: Definition of the *responsible_party* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","A value uniquely identifying a party (individual or organization)."
   ".. _individual_name:

   individual_name","str",,"Optional","The name of the organization or the individual."
   ".. _position_name:

   position_name","str",,"Optional","Role or position of the responsible person."
   ".. _organization_name:

   organization_name","str",,"Optional","Organization/affiliation of the individual/responsible person. In case of an organization, the name property should be used and this property is not to be used."
   ".. _contact_information:

   contact_information","dict",,"Optional","Contact information"
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

