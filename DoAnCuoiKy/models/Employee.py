class Employee:
    def __init__(self,EmployeeId,EmployeeName,UserName,PassWord):
        self.EmployeeId=EmployeeId
        self.EmployeeName=EmployeeName
        self.UserName=UserName
        self.PassWord=PassWord
    def __str__(self):
        return f'{self.UserName}\t{self.PassWord}'