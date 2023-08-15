observation
====

Download the definition as a CSV file: :download:`csv <observation.csv>`.

.. csv-table:: Definition of the *observation* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","ID / primary key."
   ".. _location:

   location","Geography",,"Required","Location of observation."
   ".. _elevation:

   elevation","float",,"Required","Elevation of observation above mean sea level (in meters)."
   ".. _observation_type:

   observation_type","str","`reference_data.observation_type.id <../reference_data/observation_type.html#id>`_","Optional","Type of observation."
   ".. _phenomenon_start:

   phenomenon_start","datetime",,"Optional","Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end."
   ".. _phenomenon_end:

   phenomenon_end","datetime",,"Required","End time of the phenomenon being observed or observing period."
   ".. _result_value:

   result_value","float",,"Required","The value of the result in float representation."
   ".. _result_uom:

   result_uom","str",,"Required","Units used to represent the value being observed."
   ".. _result_description:

   result_description","str",,"Optional","str representation of the result if applicable."
   ".. _result_quality:

   result_quality","dict",,"Optional","JSON representation of the result quality, key / value pairs."
   ".. _result_time:

   result_time","datetime",,"Optional","Time that the result became available."
   ".. _valid_from:

   valid_from","datetime",,"Optional","Time that the result starts to be valid."
   ".. _valid_to:

   valid_to","datetime",,"Optional","Time after which the result is no longer valid."
   ".. _host:

   host","str","`master_data.host.id <../master_data/host.html#id>`_","Required","Host associated with making the observation, equivalent to OGC OMS 'host'."
   ".. _observer:

   observer","str","`master_data.equipment.id <../master_data/equipment.html#id>`_","Optional","Observer associated with making the observation, equivalent to OGC OMS 'observer'."
   ".. _observed_property:

   observed_property","str","`reference_data.observed_property.id <../reference_data/observed_property.html#id>`_","Required","The phenomenon, or thing, being observed."
   ".. _observing_procedure:

   observing_procedure","str","`reference_data.observing_procedure.id <../reference_data/observing_procedure.html#id>`_","Optional","Procedure used to make the observation."
   ".. _dataset:

   dataset","str",,"Optional","Primary dataset that this observation belongs to."
   ".. _parameter:

   parameter","dict",,"Optional","List of key/ value pairs in dict."
   ".. _featureOfInterest:

   featureOfInterest","str","`master_data.feature.id <../master_data/feature.html#id>`_","Optional","Feature of interest that this observation is associated with."
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
   ".. _source:

   _source","str","`master_data.source.id <../master_data/source.html#id>`_","Required","The source of this record."
   ".. _source_identifier:

   _source_identifier","str",,"Required","The original identifier for the record from the data source (if available)."

