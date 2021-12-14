from sqlalchemy.orm import Session, exc
import models
import schemas


def get_tasks(db: Session):
    return db.query(models.User).all()


def get_tasks_id(db: Session, task_id: int):
    return db.query(models.User).filter(models.User.id == task_id).first()


def create_task(db: Session, task: schemas.Todo) -> schemas.Todo:
    task_data = models.User(content=task.id, description=task.task)
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data


def update_task(db: Session, task_id: int, done: bool):
    task_data = db.query(models.User).filter(models.User.id == task_id).first()
    task_data.done = done
    db.commit()
    db.refresh(task_data)
    return task_data


def delete_task(db: Session, task_id: int, done: bool):
    task_data = db.query(models.User).filter(models.User.id == task_id).delete()
    if not task_data:
        raise exc.NoResultFound
    return {'id': str(task_id)}
