from person import
class Customer(Person):
    def __init__(self, first_name, last_name, age, customer_id, membership_type):
        super()__init__(first_name, last_name, age)
        self.customer_id = customer_id
        self.membership_type = membership_type

    pass
