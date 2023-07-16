import configparser
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import parse

config = configparser.ConfigParser()
config.read("app/config.ini")

PASSWORD = parse.quote(config.get("database","PASSWORD"))
host = config.get("database","HOST")
username = config.get("database","USER")
database = config.get("database","DATABASE")

url = f"mysql+pymysql://{username}:{PASSWORD}@{host}:3306/{database}"

engine = create_engine(url=url)
local_session = sessionmaker(autoflush=False,
                             bind=engine)
Base = declarative_base()


def get_db():
    """
    Helps us to connect to the database
    """
    db = local_session()
    try:
        yield db
    finally:
        db.close()