class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary
    def get_employee_info(self):
        print ("----Thông tin nhân viên----")
        print (f"Mã nhân viên:{self.employee_id}")
        print (f"Họ tên:{self.name}")
        print (f"Chức vụ:{self.position}")
        print (f"Lương:{self.salary}")
    def apply_raise(self,percentage):
        if(percentage<=0):
            print ("Phần trăm tăng lương phải lớn hơn 0")
            return
        increase=self.salary*(percentage/100)
        self.salary += increase
        print (f"Đã được tăng lương {percentage}% . Lương mới là {self.salary} VND")
class Manager(Employee):
    def __init__(self, employee_id, name, position, salary,team_size):
        super().__init__(employee_id, name, position, salary)
        self.team_size=team_size
    def get_team_info(self):
        print(f"Quản lý {self.team_size} thành viên trong nhóm")
emp1=Employee("E001","Nguyễn Văn An","Nhân viên IT",15000000)
emp1.get_employee_info()
emp1.apply_raise(20)
emp1.get_employee_info()
print("----------------------")
manage1=Manager("MĐ01","Trần Văn Cường","Trưởng phòng",30000000,8)
manage1.get_employee_info()
manage1.apply_raise(5)
manage1.get_team_info()
manage1.get_employee_info()