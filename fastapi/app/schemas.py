from typing import List, Optional

from pydantic import BaseModel


#
class Todo(BaseModel):
    id: int
    task: str
