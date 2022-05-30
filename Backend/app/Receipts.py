from math import prod
from traceback import print_tb
from typing import List
from xml.etree.ElementTree import tostring
from pydantic import BaseModel
from product import Product

class Receipts(BaseModel):
    username: str
    storeName: str
    products: List[Product] = None



