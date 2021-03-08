from person import Person
class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id, store_location, annual_salary):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id
        self.store_location = store_location
        self.annual_salary = annual_salary

    def employee_details(self):
        return f"First Name: {self.first_name} \n" + f"Last Name: {self.last_name} \n" + f"Employee Id: {self.employee_id} \n" + f"Store Location: {self.store_location}\n" + f"Annual Salary: £ {self.annual_salary}\n"
    





