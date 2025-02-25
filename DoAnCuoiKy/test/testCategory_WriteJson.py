from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Category import Category

categories=[]
for i in range(1,21):
    cate=Category(f'C{i}',f'Cate{i}')
    categories.append(cate)
print('List of Categories:')
for cate in categories:
    print(cate)
jff=JsonFileFactory()
filename='../dataset/categories.json'
jff.write_data(categories,filename)