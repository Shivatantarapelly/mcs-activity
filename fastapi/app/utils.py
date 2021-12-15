import datetime

from sqlalchemy.orm import Session
import models
import schemas


def get_tasks(db: Session):
    return db.query(models.User).all()


def create_task(db: Session, task: schemas.Todo):
    task_data = models.User(task=task.task, date=datetime.datetime.now())
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data


def get_task_id(db: Session, task_id: int):
    get_task = db.query(models.User).filter(models.User.id == task_id).first()
    return get_task


def update_task(db: Session, task_id: int, task: str):
    task_data = get_task_id(db=db, task_id=task_id)
    if task_data:
        task_data.task = task
        task_data.date = datetime.datetime.now()
        db.commit()
        db.refresh(task_data)
        return task_data
    else:
        new = models.User(id = task_id,task=task,date = datetime.datetime.now())
        db.add(new)
        db.commit()
        db.refresh(new)
        return new


def delete_task(db: Session, task_id: int):
    task_del = get_task_id(db=db, task_id=task_id)
    if task_del:
        db.delete(task_del)
        db.commit()
        return "task deleted"
    else:
        return "task not found"
