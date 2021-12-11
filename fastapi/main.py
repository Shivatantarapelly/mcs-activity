import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return 'welcome'

@app.get('/about/{id}')
def about(id):
    return 'welcome to about page num:',id


if __name__ == '__main__':
    uvicorn.run(app)