from pydantic import BaseModel


class Product(BaseModel):
    name: str
    color: str
    price: float

