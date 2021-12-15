

from pydantic import BaseModel


#
class Todo(BaseModel):
    task: str


class TodoDate(BaseModel):
    date: str


