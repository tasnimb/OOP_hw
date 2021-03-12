class Account:
    numCreated = 0

    def __init__(self,initial):
        self._balance = initial
        Account.numCreated += 1

    def deposit(self,amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        self._balance -= amount
        return

    def get_balance(self):
        return self._balance