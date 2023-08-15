equipment
====

Download the definition as a CSV file: :download:`csv <equipment.csv>`.

.. csv-table:: Definition of the *equipment* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _description:

   description","str",,"Required","Description of sensor."
   ".. _equipment_type:

   equipment_type","str","`reference_data.equipment_type.id <../reference_data/equipment_type.html#id>`_","Required","The type of equipment, e.g. temperature sensor, sensor housing, etc"
   ".. _online_resource:

   online_resource","dict",,"Optional","Link(s) to further information."
   ".. _specification_link:

   specification_link","str",,"Optional","Link to manufacturers (or other) specification describing the equipment."
   ".. _firmware_version:

   firmware_version","str",,"Optional","Firmware version of software installed in sensor."
   ".. _manufacturer:

   manufacturer","str",,"Optional","Make, or manufacturer, of sensor."
   ".. _model:

   model","str",,"Optional","Model of sensor."
   ".. _serial_number:

   serial_number","str",,"Optional","Serial number of sensor."
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

