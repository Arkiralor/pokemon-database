'''
Declares and define the database settings.
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker

import os
from dotenv import load_dotenv
import psycopg2 as pg

load_dotenv()

DB_TYPE = os.getenv('DB_TYPE')
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']
PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']

if DB_TYPE == "SQLite":
    SQLALCHEMY_DATABASE_URI = "sqlite:///pokemon.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={
        'check_same_thread': False})

elif DB_TYPE == "PostgreSQL":
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
    engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
