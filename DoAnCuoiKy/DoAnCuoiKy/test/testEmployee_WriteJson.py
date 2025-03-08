from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Employee import Employee

employees=[]
employees.append(Employee('E1','Khánh','khanhs','123'))
employees.append(Employee('E2','Hùng','hung','456'))
employees.append(Employee('E3','Đăng','dang','789'))
employees.append(Employee('E4','Phong','phong','000'))
print('Danh sách Employee:')
for ep in employees:
    print(ep)
jff=JsonFileFactory()
filename='../dataset/employees.json'
jff.write_data(employees,filename)