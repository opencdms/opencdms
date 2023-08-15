record
====

Download the definition as a CSV file: :download:`csv <record.csv>`.

.. csv-table:: Definition of the *record* table.
   :header: "Property","Kind","References","Requirement","Description"

   ".. _id:

   id","str",,"Required","A unique identifier of the catalogue record."
   ".. _time:

   time","str",,"Required","The temporal extent of the resource. Can be null if there is no associated temporal extent."
   ".. _title:

   title","str",,"Required","A human-readable name given to the resource."
   ".. _location:

   location","Geography",,"Required","A geometry associated with the resource that is used for discovery. Can be null if there is no associated geometry."
   ".. _created:

   created","str",,"Required","Date of creation of this record."
   ".. _updated:

   updated","str",,"Required","The most recent date on which the record was changed."
   ".. _resource_type:

   resource_type","str",,"Required","The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property."
   ".. _description:

   description","str",,"Required","A free-text account of the resource."
   ".. _keywords:

   keywords","str",,"Required","The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes. Semi-colon delimited"
   ".. _language:

   language","str",,"Required","The natural language used for textual values (e.g. titles, descriptions, etc.) of the resource. ISO 639-1/639-2 codes should be used."
   ".. _external_ids:

   external_ids","dict",,"Required","An identifier for the resource assigned by an external (to the catalogue) entity."
   ".. _themes:

   themes","dict",,"Required","A knowledge organization system used to classify the resource."
   ".. _formats:

   formats","dict",,"Required","A list of available distributions of the resource."
   ".. _providers:

   providers","dict",,"Required","A list of providers qualified by their role in association to the record."
   ".. _license:

   license","str",,"Required","A legal document under which the resource is made available. The value should be a code, convenient for filtering the records. Where applicable, the use of the identifiers from the SPDX License List is recommended. If multiple licenses apply, it is recommended to use ''various'.  Where available, links to a URI of each applicable license should be added to the 'links' property."
   ".. _rights:

   rights","str",,"Required","A statement that concerns all rights not addressed by the license such as a copyright statement."
   ".. _links:

   links","dict",,"Required","A list of links for accessing the resource (e.g. download link, access link) in one of the supported distribution formats and/or links to other resources associated with this resource. Also, a list of links for navigating the API (e.g. prev, next, etc.).  Since the specification requires that at least the self link be present then the min items for this list should be one."

