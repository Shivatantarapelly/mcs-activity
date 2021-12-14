from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def home(limit, published: bool):
    if published:
        return f'welcome page {limit}'
    return 'not published'


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return 'welcome to about page num:', id


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"blog is created with title {request.title}"}


#

if __name__ == '__main__':
    uvicorn.run(app)
