from pydantic import BaseModel

class Emni(BaseModel):
    name: str
    age:int
    emni:bool