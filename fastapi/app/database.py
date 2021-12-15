from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, engine

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Shiva@1995@localhost:3306/tracker"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# meta = MetaData()
# conn = engine.connect()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


