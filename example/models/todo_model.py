from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    title:str
    description:str
    completed:bool
