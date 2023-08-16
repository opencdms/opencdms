:html_theme.sidebar_secondary.remove:

exposure
====

Sensor exposure classification code list.


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

        Download the definition as a CSV file: :download:`csv <exposure.csv>`.

        .. csv-table:: Definition of the *exposure* table.
           :header: "Property","Kind","References","Requirement","Description"

           ".. _id:

           id","str",,"Required","ID / primary key."
           ".. _inSchema:

           inSchema","str",,"Required","The scheme/vocabulary that this record is from."
           ".. _name:

           name","str",,"Optional","Short name / abbreviation for exposure classification."
           ".. _description:

           description","str",,"Required","Description of sensor exposure according to WMO-No. 8."
           ".. _links:

           links","dict",,"Optional","Links providing further definition of exposure class."
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

        Download the example CSV file: :download:`csv <./examples/exposure.csv>`.

        .. csv-table:: Example data
           :file: ./examples/exposure.csv
           :header-rows: 1
           :quote: '
