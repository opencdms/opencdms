:html_theme.sidebar_secondary.remove:

sensor_characteristics
====

Download the definition as a CSV file: :download:`csv <sensor_characteristics.csv>`.

.. csv-table:: Definition of the *sensor_characteristics* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","Primary key for this record."
   ".. _equipment:

   equipment","str","`master_data.equipment.id <../master_data/equipment.html#id>`_","Required","The equipment / sensor to which this record applies."
   ".. _observed_property:

   observed_property","str","`reference_data.observed_property.id <../reference_data/observed_property.html#id>`_","Required","The observed parameter to which this record applies."
   ".. _observing_method:

   observing_method","str","`reference_data.observing_method.id <../reference_data/observing_method.html#id>`_","Required","Primary method/principles by which the sensor makes measurements."
   ".. _observing_method_details:

   observing_method_details","str",,"Optional","A description of the method of measurement/observation used."
   ".. _measurement_units:

   measurement_units","int",,"Optional","The units used in this record."
   ".. _drift_per_unit_time:

   drift_per_unit_time","float",,"Optional","Intrinsic capability of the measurement/observing method - drift per unit time. Typically a percentage per unit time but could be absolute e.g. 1 degree per year."
   ".. _unit_time:

   unit_time","int",,"Optional","Unit time for drift per unit time (seconds)."
   ".. _valid_min:

   valid_min","float",,"Optional","Minimum observable value by sensor, in units specified by measurement units."
   ".. _valid_max:

   valid_max","float",,"Optional","Maximum observable value by sensor, in units specified by measurement units."
   ".. _specified_absolute_uncertainty:

   specified_absolute_uncertainty","float",,"Optional","Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measurement units."
   ".. _specified_relative_uncertainty:

   specified_relative_uncertainty","float",,"Optional","Measurement uncertainty for measurements from this sensor, 2 sigma. Units in %, e.g. 20 %."
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

