"""
ORM:

-> object oriented way of dealing with databases
-> tables are classes
-> Fields are attributes

Steps for creating a table:

-> Create engine
-> Create session
-> create table
-> migrate

"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("postgresql://username:password@localhost:5432/data_basename",echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)()

Base = declarative_base()


class User(Base):
    __tablename__ = "test"

    username = Column(String, primary_key=True)
    password = Column(Integer)

    def __init__(self, username, password):
        self.username = username
        self.password = password


user = User("shiva", 123)
SessionLocal.add(user)
SessionLocal.commit()
