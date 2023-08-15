:html_theme.sidebar_secondary.remove:

media
====

Download the definition as a CSV file: :download:`csv <media.csv>`.

.. csv-table:: Definition of the *media* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Optional","ID / primary key."
   ".. _media_type:

   media_type","str","`reference_data.media_type.id <../reference_data/media_type.html#id>`_","Optional","The type of media described by this entry."
   ".. _description:

   description","str",,"Optional","Description of the media."
   ".. _created:

   created","datetime",,"Optional","Date the media was created/uploaded."
   ".. _creator:

   creator","str",,"Optional","Who uploaded the media. "
   ".. _rights:

   rights","int",,"Optional","Digital rights associated with the media."
   ".. _source:

   source","str",,"Optional","Source of the media."
   ".. _data:

   data","dict",,"Optional","TBD"

