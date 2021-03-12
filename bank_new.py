from account_new import Account
from savings_new import Savings

#Instantiate account

Lisa = Account(1000.00)
Lisa.deposit(550.23)
Lisa.withdraw(50)
print(Lisa.get_balance())
Lisa.withdraw(1550)
print(Lisa.get_balance())
# print(Lisa)

print("Your current balance is " + str(Lisa.get_balance()))


#instantiate savings account

Oprah = Savings(500, 100)
print(Oprah.all_money())
print(Oprah.savings)
Oprah.deposit_savings(700)
print(Oprah.savings)
Oprah.withdraw(200)
print(Oprah.savings)