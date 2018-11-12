salary=int(input("Please enter your salary amount: "))
years=int(input("Please enter your years of service: "))
if years>5:
    bonus=0.05*salary
    print("Your bonus amount is ",bonus)
else:
    bonus=0
    print("Sorry no bonus for you!")
print("The total amount = ",salary + bonus)
