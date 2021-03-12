class Person:
    def __init__(self,firstname,lastname,age):
        self._firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def full_profile(self):
        return f"First name:{self.get_firstname()}\nSurname:{self.get_lastname()}\nAge:{self.get_age()}"