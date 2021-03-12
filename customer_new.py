from person_new import Person

class Customer(Person):
    def __init__(self,firstname,lastname,age,occupation):
        super().__init__(firstname,lastname,age)
        self._occupation = occupation

    def get_occupation(self):
        return self._occupation()

    def __str__(self):
         return f"Firstname:{self.get_firstname()}\nSurname:{self.get_lastname()}\nAge:{self.get_age()}\nOccupation:{self._occupation}"



customer1 = Customer('Jane','Doe',39,'Actress')
print(customer1.__str__())