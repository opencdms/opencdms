#!/bin/bash

create_sql=`mktemp`


if [ -z "${POSTGRES_USER:-}" ]; then
    POSTGRES_USER=${POSTGRESQL_USERNAME}
fi

if [ -z "${POSTGRES_DB:-}" ]; then
    POSTGRES_DB=${POSTGRESQL_DATABASE}
fi

if [ -z "${PGDATA:-}" ]; then
    PGDATA=${POSTGRESQL_DATA_DIR}
fi

if [ -z "${POSTGRESQL_CONF_DIR:-}" ]; then
	POSTGRESQL_CONF_DIR=${PGDATA}
fi

cat <<EOF >${create_sql}
CREATE EXTENSION IF NOT EXISTS postgis CASCADE;
EOF

# create extension postgis extension in initial databases
psql -U "${POSTGRES_USER}" postgres -f ${create_sql}
psql -U "${POSTGRES_USER}" template1 -f ${create_sql}

if [ "${POSTGRES_DB:-postgres}" != 'postgres' ]; then
    psql -U "${POSTGRES_USER}" "${POSTGRES_DB}" -f ${create_sql}
fi