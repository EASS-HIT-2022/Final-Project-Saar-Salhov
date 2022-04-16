from math import prod
from traceback import print_tb
from typing import List
from xml.etree.ElementTree import tostring
from pydantic import BaseModel
from product import Product

class Receipts(BaseModel):
    id: int
    storeName: str
    products: List[Product] = None

product = [{
    'id': 1,
    'name': 'Tshirt',
    'color': 'blue',
    'price': 10
},
{    'id': 2,
    'name': 'Tshirt',
    'color': 'red',
    'price': 15}]

# print(product[0])
# product1 = Product(**product[0])
# product2 = Product(**product[1])

# external_data = {
#     'id': 1,
#     'storeName': 'saar',
#     'product': [product1, product2],
# }

# # print(external_data)
# # print(*external_data)
# # print(**external_data)
# test = Receipts(**external_data)
# print(test.dict())



