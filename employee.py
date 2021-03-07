class Employee:
    def __init__(self, first_name, last_name, employee_id, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.annual_salary = annual_salary
        pass

    def employee_details(self):
        return f"First Name: {self.first_name} \n" + f"Last Name: {self.last_name} \n" + f"Employee Id: {self.employee_id} \n" + f"Annual Salary: £ {self.annual_salary} \n"
    

emp1 = Employee("Jamie", "Adams", 29846, 50000)
print(emp1.employee_details())



