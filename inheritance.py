#inheritance
#practise：1、人力系统
'''
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f'employee_name:{self.name},employee_id:{self.id}')

class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary

    def calulate_monthly_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_salary(self):
        return self.daily_salary * self.work_days

Jason = FullTimeEmployee('Jason','01',10000)
Boston = PartTimeEmployee('Boston','007',180,10)
Jason.print_info()
Boston.print_info()
print(Jason.calulate_monthly_salary())
print(Boston.calculate_monthly_salary())
'''


