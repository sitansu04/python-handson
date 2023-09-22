from pydantic import BaseModel


class Items(BaseModel):
    name: str
    description: str
    catagory: str
    mrp: int
    selling_price: int
