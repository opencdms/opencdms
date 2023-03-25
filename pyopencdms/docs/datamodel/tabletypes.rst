===========
Table types
===========

Base tables
===========

Base tables contain the actual data in the database and are managed using database migration tools. These tables are the foundation of the data model and represent the persistent, underlying data storage in your database. The use of a database migration tool is essential for maintaining the integrity and consistency of the database over time as the underlying data and structure of the database changes. These tools provide a means of making these changes in a controlled, predictable, and repeatable manner.

Derived tables
==============

Derived tables, on the other hand, do not contain data themselves but are instead represented by views in the database. These views provide a simplified, virtual representation of the data in the base tables and are used to improve the accessibility and performance of the data. Derived tables provide several benefits:

- Abstraction: A view provides an abstraction layer that can hide the underlying complexity of the data and the logic used to access it. This can simplify the application's interaction with the database and reduce the risk of making mistakes.
- Performance: In some cases, creating a view can improve performance. For example, if you have a complex SELECT statement that is used frequently, creating a view can help the database optimize the execution of the statement by compiling it and storing the execution plan. This can result in faster execution times compared to executing the statement each time it is needed.
- Security: Views can be used to enforce security and data privacy. You can create views that restrict access to sensitive data, for example by only displaying a subset of columns or rows.
- Simplicity: Views can simplify the data model and make it easier to understand. By providing a high-level, simplified representation of the data, views can reduce the complexity of the underlying data structures and the logic used to access them.

Overall, the use of derived tables can lead to a more maintainable, secure, and performant database design.

Views can be utilized for on-the-fly transformations, such as adjusting the data model of another CDMS to match the Climate Data Model. They can also be used for generating products, such as an summarising data for an inventory plot.

