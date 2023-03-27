import os

from dotenv import load_dotenv

load_dotenv()


def get_connection_string(engine: str, driver: str, user: str, password: str, host: str, port: str, db_name: str) -> str:
    return f"{engine}+{driver}://{user}:{password}@{host}:{port}/{db_name}"


def get_clide_connection_string() -> str:
    return get_connection_string(
        engine="postgresql",
        driver="psycopg2",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=os.getenv("CLIDE_PORT"),
        db_name=os.getenv("CLIDE_DB_NAME")
    )


def get_climsoft_4_1_1_connection_string() -> str:
    return get_connection_string(
        engine="mysql",
        driver="mysqldb",
        user="root",
        password="password",
        host="127.0.0.1",
        port=os.getenv("CLIMSOFT_4_1_1_PORT"),
        db_name=os.getenv("CLIMSOFT_DB_NAME")
    )


def get_mch_english_connection_string(port_override: str = None) -> str:
    return get_connection_string(
        engine="mysql",
        driver="mysqldb",
        user="root",
        password="password",
        host="127.0.0.1",
        port=os.getenv("MCH_ENGLISH_PORT") if port_override is None else port_override,
        db_name=os.getenv("MCH_DB_NAME")
    )


def get_midas_connection_string(port_override: str = None) -> str:
    return get_connection_string(
        engine="postgresql",
        driver="psycopg2",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=os.getenv("MIDAS_PORT") if port_override is None else port_override,
        db_name=os.getenv("MIDAS_DB_NAME")
    )


def get_surface_connection_string(port_override: str = None) -> str:
    return get_connection_string(
        engine="postgresql",
        driver="psycopg2",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=os.getenv("SURFACE_PORT", 45432) if port_override is None else port_override,
        db_name=os.getenv("SURFACE_DB_NAME", "postgres")
    )

