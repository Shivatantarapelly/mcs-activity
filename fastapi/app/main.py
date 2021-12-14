from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import utils
import schemas
from dependencies import get_db

app = FastAPI(title="todo api")


@app.get('/tasks', response_model=List[schemas.Todo])
def get_items(db: Session = Depends(get_db)):
    items = utils.get_tasks(db)
    return items


@app.get('/tasks/{task_id}', response_model=schemas.Todo)
def get_item_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = utils.get_tasks_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_task


@app.post('/create-task/', response_model=schemas.Todo)
def create_task(task : schemas.Todo, db: Session = Depends(get_db)) -> schemas.Todo:
    return utils.create_task(db, task=task)


@app.put("/update_task/{task_id}")
def update_task(task_id: int, done:bool, db:Session = Depends(get_db)):
    db_todo = utils.update_task(db, task_id,done)
    return db_todo


@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int, done:bool, db:Session = Depends(get_db)):
    db_todo = utils.delete_task(db, task_id,done)
    return db_todo