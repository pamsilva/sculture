import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, dotenv_values

load_dotenv()

if "SQLALCHEMY_DATABASE_URL" not in os.environ:
    SQLALCHEMY_DATABASE_URL = dotenv_values(".env")["SQLALCHEMY_DATABASE_URL"]
else:
    SQLALCHEMY_DATABASE_URL = os.environ["SQLALCHEMY_DATABASE_URL"]


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    return db
