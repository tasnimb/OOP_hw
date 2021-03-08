def discount():
    if employee_discount == ['yes', 'YES', 'Yes']:
        print("You have a 20% discount")

    elif occupation_nhs == ['yes', 'YES', 'Yes']:
        print("You have a 15% discount")
    elif age >= str(65):
        print("You get a 10% discount")
    else:
        print("You do not qualify for a discount")




# if age > 65:
#     10% discount
#
# if customer == employee:
#     discount 20%
#
# # def nhs(input("are your a nhrs worker:)
# #bool(if True return 15% discount, if False, nothing )
# if customer occupation == NHS:
#     discount