# TODO: Depreciated - this should be removed when db.seeder is replaced
#       The rest of the codebase is using db.config for default db connection strings
#       This file may also be in use by the pygeoapi integration until it is updated.
import os

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Query


class OpenCDMSConfig:
    CDM_DB_HOST = os.getenv("CDM_DB_HOST", "127.0.0.1")
    CDM_DB_PORT = os.getenv("CDM_DB_PORT", "35432")
    CDM_DB_USER = os.getenv("CDM_DB_USER", "postgres")
    CDM_DB_PASS = os.getenv("CDM_DB_PASSWORD", "password")
    CDM_DB_NAME = os.getenv("CDM_DB_NAME", "postgres")
    CDM_DB_ENGINE = os.getenv("CDM_DB_ENGINE", "postgresql")
    CDM_DB_DRIVER = os.getenv("CDM_DB_DRIVER", "psycopg2")
config = OpenCDMSConfig()


def get_connection_string(
    engine: str,
    driver: str,
    user: str,
    password: str,
    host: str,
    port: str,
    db_name: str,
) -> str:
    return f"{engine}+{driver}://{user}:{password}@{host}:{port}/{db_name}"


def get_cdm_connection_string() -> str:
    return get_connection_string(
        engine=config.CDM_DB_ENGINE,
        driver=config.CDM_DB_DRIVER,
        user=config.CDM_DB_USER,
        password=config.CDM_DB_PASS,
        host=config.CDM_DB_HOST,
        port=config.CDM_DB_PORT,
        db_name=config.CDM_DB_NAME,
    )


def cdm_session():
    DB_URL = get_cdm_connection_string()
    db_engine = create_engine(DB_URL)
    SessionLocal = sessionmaker(bind=db_engine)
    session = SessionLocal()
    return session


def get_count(q: Query):
    """
    Return the number of rows that matches a query
    """
    count_q = q.statement.with_only_columns(
        func.count(), maintain_column_froms=True
    ).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count
