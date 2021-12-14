from fastapi import FastAPI, Depends
from typing import List
from pydantic import BaseModel, Field
import databases
import sqlalchemy
from datetime import datetime
import aiosqlite

DATABASE_URL = "sqlite:///./store.db"

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)

register = sqlalchemy.Table(
    "register",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(500)),
    sqlalchemy.Column("data_created", sqlalchemy.DateTime())
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event(("shutdown"))
async def shutdown():
    await database.disconnect()


class RegisterIn(BaseModel):
    name: str = Field(...)


class Register(BaseModel):
    id: int
    name: str
    date_created: str


@app.post('/register/')
async def create(r: Register):
    query = register.insert().values(
        name=r.name,
        date_created=datetime.now()
    )
    record_id = await database.execute(query)
    query= register.select().where(register.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}
