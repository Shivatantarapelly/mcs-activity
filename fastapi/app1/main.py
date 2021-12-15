import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from models import Base
from database import engine
from database import SessionLocal
from fastapi import Depends
import utils

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home():
    return {"name": "shiva"}


@app.post('/create_friend')
def create_friend(first_name: str, last_name: str, age: int, db: Session = Depends(get_db)):
    friend = utils.create_friend(db=db, first_name=first_name, last_name=last_name, age=age)
    return {"friend": friend}


@app.get('/get_friend/{id}/')
def get_friend(id: int, db: Session = Depends(get_db)):
    friend = utils.get_friend(db=db, id=id)
    return friend


@app.put('/update/{id}/')
def update_friend(id: int, first_name: str, last_name: str, age: int, db: Session = Depends(get_db)):
    db_friend = utils.get_friend(db=db, id=id)
    if db_friend:
        update_friend = utils.update_friend(db=db, id=id, first_name=first_name, last_name=last_name, age=age)
        return update_friend
    else:
        return {"error": f'Friend with id {id} does not exist'}


@app.delete("/delete_friend/{id}/")
def delete_friend(id: int, db: Session = Depends(get_db)):
    db_friend = utils.get_friend(db=db, id=id)
    if db_friend:
        return utils.delete_friend(db=db, id=id)
    else:
        return {"error": f'Friend with id {id} does not exist'}


@app.get("/list_friends")
def list_friends(db:Session = Depends(get_db)):
    friends_list = utils.list_friends(db=db)
    return friends_list


if __name__ == "__main__":
    uvicorn.run(app)
