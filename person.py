from datetime import date
# dob = datetime.date(1982,8,7)

class Person:
    def __init__(self,first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def firstname(self):
        self.first_name = first_name

    def lastname(self, last_name):
        self.last_name = last_name

    def dob(self, age):
        self.age = int(age)

    # def calculateAge(self,birthDate):
    #     today = date.today()
    #     age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    #         return age

    def get_profile(self):
        return f" First Name: {self.first_name}\n Last Name: {self.last_name} \n Age: {self.age} \n"

person1 = Person("Greg", "James", 37)
print(person1.get_profile())


