from person_new import Person


class Employee(Person):

    tax = 0.20

    def __init__(self, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary

    def get_salary(self):
        return self.salary()

    def tax_paid(self):
        return self.salary * Employee.tax

    def __str__(self):
        return f"Firstname:{self.get_firstname()}\nSurname:{self.get_lastname()}\nAge:{self.get_age()}" \
                f"\nSalary:{self.salary}\nTax paid:{self.tax_paid()}"