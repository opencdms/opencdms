.. pyopencdms documentation documentation master file, created by
   sphinx-quickstart on Tue Jul 27 16:54:40 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OpenCDMS documentation
======================

This is an early version of the OpenCDMS documentation that is still in development.

.. seealso:: `SURFACE CDMS documentation <https://surface.readthedocs.io>`_


.. panels::
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 text-center
    :img-top-cls: w-50 m-auto px-1 py-2

    ---
    :img-top: _static/evaluation.png

    User Guide
    +++
    .. link-button:: user/index
        :type: ref
        :text: User Guide
        :classes: btn-outline-info btn-block

    ---
    :img-top: _static/laptop.png

    Administrator Guide
    +++
    .. link-button:: administrator/index
        :type: ref
        :text: Administrator Guide
        :classes: btn-outline-info btn-block
    ---
    :img-top: _static/laboratory.png

    Developer Documentation

    +++
    .. link-button:: developer/index
        :type: ref
        :text: Developer Guide
        :classes: btn-outline-info btn-block


.. toctree::
   :caption: User Guide
   :maxdepth: 1
   :name: userguide_index
   :hidden:

   user/index


.. toctree::
   :caption: Developers Guide
   :maxdepth: 1
   :name: developers_index
   :hidden:

   developer/index

.. toctree::
   :caption: Administrator Guide
   :maxdepth: 1
   :name: administrators_index
   :hidden:

   administrator/index
