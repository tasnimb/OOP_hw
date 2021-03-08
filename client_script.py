from person import Person
from employee import Employee
from customer import Customer
from discounts import discount

first_name = input("Please enter your first name:")
second_name = input("Enter your surname: ")
employee_discount = input("Are you an employee?: ")
occupation_nhs = input("Are you an NHS worker?: ")
age = input(str("Enter your age: "))


person1 = Person("Greg", "James", 37)
print(person1.get_profile())

emp1 = Employee("Jamie", "Adams", 17, 28696, "London Cheapside", 17000)
print(emp1.employee_details())

customer1 = Customer('Tasnim', 'b', 22, 2342, 'premium')
customer1.first_name()





