import random

from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Product import Product

products=[]
for i in range(1,101):
    proid=f'P{i}'
    proname=f'Product {i}'
    price=random.randrange(10,1000)
    quantity=random.randrange(1,100)
    cateid=f'C{random.randrange(1,21)}'
    p=Product(proid,proname,price,quantity,cateid)
    products.append(p)
print('List of Product:')
for prod in products:
    print(prod)
jff=JsonFileFactory()
filename='../dataset/products.json'
jff.write_data(products,filename)