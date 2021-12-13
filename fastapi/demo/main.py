from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.get('/home')
def get():
    return 'hello shiva'


@app.get('/home/{name}')
def get(name):
    return f'hello {name}'


class Item(BaseModel):
    name: str
    number: int


@app.post('/home/post')
def post(item: Item):
    name = item.name
    number = item.number
    return f'Hello {name} you are in new number {number}'


if __name__ == '__main__':
    uvicorn.run(app, port=5000)
