class Employee:
    def __init__(self, first_name, last_name, employee_id, annual_salary,pension_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.annual_salary = annual_salary
        self.pension_rate = pension_rate
        pass

    def employee_details(self):
        return f"First Name: {self.first_name} \n" + f"Last Name: {self.last_name} \n" + f"Employee Id: {self.employee_id} \n" + f"Annual Salary: £ {self.annual_salary} \n" + f"Pension Rate : {self.pension_rate} % \n"
    
    def calculate_annual_pension(self):
        return f"{self.first_name} {self.last_name} annual pension contribution is £ {self.annual_salary * self.pension_rate} \n"

emp1 = Employee("Jamie", "Adams", 29846, 50000, 3)
print(emp1.employee_details())
emp1_savings = Employee("Jamie", "Adams", 29846, 50000, 0.03)
print(emp1_savings.calculate_annual_pension())

emp2 = Employee("Helen", "Joshua", 29768, 60000, 4.6)
print(emp2.employee_details())
emp2_savings = Employee("Helen", "Joshua", 29768, 60000, 0.046)
print(emp2_savings.calculate_annual_pension())

