import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return 'welcome'


@app.get('/num/{num}')
def number(num: int):
    return 'this is the number', num


if __name__ == '__main__':
    uvicorn.run(app)