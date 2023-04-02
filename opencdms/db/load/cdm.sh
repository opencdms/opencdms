#!/bin/bash

# Pass all command-line arguments to psql

# Load code tables
psql "$@" << !
\COPY cdm.observation_type FROM 'code_tables/observation_type.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observed_property FROM 'code_tables/observed_property.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observing_procedure FROM 'code_tables/observing_procedure.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.record_status FROM 'code_tables/status.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.source_type FROM 'code_tables/source_type.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
!

# Load data tables
psql "$@" << EOF
\COPY cdm.host FROM 'data_tables/hosts.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.source FROM 'data_tables/source.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.user FROM 'data_tables/users.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1990.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1991.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1992.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1993.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1994.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1995.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1996.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1997.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1998.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_1999.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2000.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2001.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2002.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2003.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2004.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2005.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2006.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2007.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2008.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2009.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2010.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2011.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
\COPY cdm.observation FROM 'data_tables/CA_6016527_2012.csv' WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA' QUOTE E'\b';
EOF