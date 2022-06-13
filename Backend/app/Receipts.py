from math import prod
from sqlite3 import Date
from traceback import print_tb
from typing import List
from xml.etree.ElementTree import tostring
from pydantic import BaseModel
from product import Product

class Receipts(BaseModel):
    date: Date
    username: str
    storeName: str
    products: List[Product] = None


