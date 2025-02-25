from DoAnCuoiKy.libs.DataConnector import DataConnector

dc=DataConnector()
categories=dc.get_all_categories()
print('List of categories in database:')
for cate in categories:
    print(cate)
products=dc.get_all_products()
print('List of products in database:')
for prod in products:
    print(prod)
c10='C10'
products_c10=dc.get_product_bycategories(c10)
print('*'*20)
print('List of Products by Catagory C10:')
for pro10 in products_c10:
    print(pro10)
print('=>',len(products_c10))