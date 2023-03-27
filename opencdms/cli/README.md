`opencdms.cli` contains all of the code for the `opencdms` command line
interface (CLI)

Some of the commands made available from the cli, like `db`, `docs` and
`test` relate to specific subpackages in this repository. These commands
may only be available if the corresponding subpackage has been installed:

| command | subpackage   | installation          |
|---------|--------------|-----------------------|
| db      | /opencdms/db | opencdms install db   |
| docs    | /docs        | opencdms install docs |
| test    | /tests       | opencdms install test |

You can also install the default set of subpackages with `opencdms install`.
