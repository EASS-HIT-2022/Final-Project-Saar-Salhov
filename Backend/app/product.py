from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    color: str
    price: float

