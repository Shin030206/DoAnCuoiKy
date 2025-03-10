from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Staff import Staff

staffs=[]

staffs.append(Staff('ST1','Hùng','hung','456'))
staffs.append(Staff('ST2','Đăng','dang','789'))
staffs.append(Staff('ST3','Phong','phong','000'))
print('Danh sách Staff:')
for st in staffs:
    print(st)
jff=JsonFileFactory()
filename='../dataset/staff.json'
jff.write_data(staffs,filename)