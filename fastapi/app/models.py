# from flask_sqlalchemy import model
#
# from database import Base
# from sqlalchemy import Column, String, Integer, Boolean, engine
#
#
# class User(Base):
#     __tablename__ = "todo"
#     identity = Column(String, primary_key=True, autoincrement=True)
#     name = Column(String, index=True)
#     due_date = Column(String, index=True)
#     description = Column(String, index=True)


from sqlalchemy import Column, Integer, String,DateTime

from database import Base


class User(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True,index=True)
    task = Column(String(20))
    date = Column(DateTime)


