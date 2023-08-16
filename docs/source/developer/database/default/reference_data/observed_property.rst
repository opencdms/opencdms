:html_theme.sidebar_secondary.remove:

observed_property
====

Observed property code list.


.. raw:: html

   <style>

      /*disable page width for wide tables*/
      .bd-page-width {max-width: none;}
      .bd-article-container {max-width: 100% !important;}

      /* Limit primary side bar width for wide pages */
      .bd-sidebar-primary {max-width: 400px;}

   </style>

.. tabs::
    .. tab:: Table definition

        Download the definition as a CSV file: :download:`csv <observed_property.csv>`.

        .. csv-table:: Definition of the *observed_property* table.
           :header: "Property","Kind","References","Requirement","Description"

           ".. _id:

           id","str",,"Required","ID / primary key."
           ".. _inScheme:

           inScheme","str",,"Required","The scheme/vocabulary that this record is from."
           ".. _name:

           name","str",,"Required","Short name / abbreviation of observed property, e.g. 'at' for air temperature."
           ".. _description:

           description","str",,"Required","Description of observed property."
           ".. _standard_name:

           standard_name","str",,"Optional","CF standard name (if applicable), e.g. 'air_temperature'."
           ".. _units:

           units","str",,"Required","Canonical units, e.g. 'Kelvin'."
           ".. _links:

           links","dict",,"Optional","Link(s) to definition / source of observed property."
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

    .. tab:: Example data

        Download the example CSV file: :download:`csv <./examples/observed_property.csv>`.

        .. csv-table:: Example data
           :file: ./examples/observed_property.csv
           :header-rows: 1
           :quote: '
