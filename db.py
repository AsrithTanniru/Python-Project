#db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()

