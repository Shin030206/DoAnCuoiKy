from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Manager import Manager

mngs=[]
mngs.append(Manager('E1','Khánh','khanhs','123'))
print('Danh sách Manager:')
for mg in mngs:
    print(mg)
jff=JsonFileFactory()
filename='../dataset/manager.json'
jff.write_data(mngs,filename)