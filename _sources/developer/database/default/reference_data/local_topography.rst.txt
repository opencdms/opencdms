:html_theme.sidebar_secondary.remove:

local_topography
====

Local topography classification code list.


.. raw:: html

   <style>

      /*disable page width for wide tables*/
      .bd-page-width {max-width: none;}
      .bd-article-container {max-width: 100% !important;}

      /* Limit primary side bar width for wide pages */
      .bd-sidebar-primary {max-width: 400px;}

      .sphinx-tabs-panel {overflow-x: scroll;}

   </style>

.. tabs::
    .. tab:: Table definition

        Download the definition as a CSV file: :download:`csv <local_topography.csv>`.

        .. csv-table:: Definition of the *local_topography* table.
           :header: "Property","Kind","References","Requirement","Description"

           ".. _id:

           id","str",,"Required","ID / primary key."
           ".. _inScheme:

           inScheme","str",,"Required","The scheme/vocabulary that this record is from."
           ".. _name:

           name","str",,"Optional","Short name / abbreviation of the local topography classification."
           ".. _description:

           description","str",,"Required","Description of local topography classification."
           ".. _links:

           links","dict",,"Optional","Links providing further definition of local topography classification."
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

        Download the example CSV file: :download:`csv <./examples/local_topography.csv>`.

        .. csv-table:: Example data
           :file: ./examples/local_topography.csv
           :header-rows: 1
           :quote: '
