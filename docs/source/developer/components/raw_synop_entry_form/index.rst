Raw FM-12 SYNOP entry form
==========================

This component allows a user to enter one or more FM-12 SYNOP messages into a form and to submit these to an
API endpoint for further processing. The API is specified via the components props.

Context
-------

The sequence diagram below shows the context of the "Raw FM-12 SYNOP entry from" component.

.. plantuml:: ./sequence.puml

Requirements
------------

Vue3 + Vuetify3

Installation
------------

TBD

Usage
-----

Props
+++++

- *api*: Host / base path to the API.
- *path*: relative path on the host to the API endpoint.


Example
+++++++
.. code-block:: html

    <template>
      <div>
        <synop-form api="https://api.opencdms.org" path="/processes/submit_synop/execution"/>
      </div>
    </template>

    <script>
    import SynopForm from '@/web-components/forms/synop-raw.vue';

    export default {
      name: 'synop',
      components: {
        SynopForm
      },
    };
    </script>

API prototype
-------------

.. openapi:: openapi.yml
