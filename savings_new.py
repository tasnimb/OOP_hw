from account_new import Account
class Savings(Account):

    interest_rate = 0.10

    def __init__(self, initial,savings):
        super().__init__(initial)
        self.savings = savings

    def all_money(self):
        return self._balance + self.savings

    def deposit_savings(self, amount):
        self.savings += amount
        return

    def withdraw(self, amount):
        self.savings -= amount
        return

    def savings_interest(self,amount):
        self.savings += amount
        if amount > 500:
            self.savings += amount * Savings.interest_rate
        else:
            return self.savings