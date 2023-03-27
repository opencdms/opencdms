## OpenCDMS Tests

Tests are divided into `unit` tests and `integration` tests.

* Unit tests have few dependencies and test small behaviours.
* Integration tests require specific dependencies, such as a PostgreSQL database

You can run the tests using the following commands:
- `opencdms test unit` (run unit tests)
- `opencdms test integration` (run integration tests)
- `opencdms test` (run all tests)

See [docs.opencdms.org/developer/tests][tests] for more information

[tests]: https://docs.opencdms.org/developer/tests
