from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import utils
import schemas
from database import Base, engine
from dependencies import get_db
import uvicorn

app = FastAPI(title="todo api")

Base.metadata.create_all(bind=engine)


@app.get('/')
def home():
    return "welcome"


@app.get('/all_tasks')
def get_items(db: Session = Depends(get_db)):
    items = utils.get_tasks(db)
    return items


@app.post('/create-task/')
def create_task(task: schemas.Todo, db: Session = Depends(get_db)):
    task_created = utils.create_task(db, task=task)
    return {"task_created": task_created}


@app.get('/get_task/{id}/')
def get_task(task_id: int, db: Session = Depends(get_db)):
    task_get = utils.get_task_id(db=db, task_id=task_id)
    return task_get


@app.put("/update_task/{task_id}")
def update_task(task_id: int, task: str, db: Session = Depends(get_db)):
    db_todo = utils.update_task(db=db, task_id=task_id, task=task)
    return db_todo


@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_todo = utils.delete_task(db, task_id)
    return db_todo


if __name__ == '__main__':
    uvicorn.run(app)
