from DoAnCuoiKy.models.Employee import Employee


class Staff(Employee):
    def __init__(self,EmployeeId,EmployeeName,UserName,PassWord):
        super().__init__(EmployeeId,EmployeeName,UserName,PassWord)
    def __str__(self):
        infor=super().__str__()
        return infor