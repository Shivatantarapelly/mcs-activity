from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel


class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None


class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


app = FastAPI()


@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.post('/package/', response_model=Package,response_model_include={"description"})
async def make_package(package: PackageIn):
    return package
