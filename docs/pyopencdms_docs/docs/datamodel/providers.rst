=========
Providers
=========

Provider plugins are listed below along with a summary of the capabilities that will, in the future, be available when using that provider.

As an initial example, the table shows that versioning of data will only be implemented and available were the CDMS
backend is able to support this capability.

Support for reading data from other systems is more straight-forward via database views than writing data.
The later may need to be implemented outside of the database and, as a result, may not be as performant.

.. csv-table::
   :header: Provider, Read, Write, Versioning
   :align: left

   opencdmsdb,✅,✅,✅
   surface,✅,✅,❌
   climsoft,✅,❌,❌
   clide,✅,❌,❌

