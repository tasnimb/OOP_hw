class Employee:
    def __init__(self, firstName, lastName, employeeID, annualSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.annualSalary = annualSalary

    def fullName(self):
        return '{} {}'.format(self.firstName,self.lastName)

    # def __str__(self):

emp1 = Employee("Jamie", "Adams", 29846, 50000)

print(emp1.fullName())
