from os import getenv
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel

load_dotenv()


DATABASE_USER = getenv("DATABASE_USER")
DATABASE_PASSWORD = quote_plus(getenv("DATABASE_PASSWORD"))
DATABASE_HOST = getenv("DATABASE_HOST")
DATABASE_PORT = getenv("DATABASE_PORT")
DATABASE_NAME = getenv("DATABASE_NAME")

connector = (
    f"mariadb+mariadbconnector://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

engine = create_engine(connector)

SQLModel.metadata.create_all(engine)
