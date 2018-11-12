salary=int(input("Please enter your salary amount: "))
years=int(input("Please enter your years of service: "))
if years>5:
    bonus=0.05*salary
    salary=salary+bonus
    print("Your bonus amount is ",bonus)
else:
    print("Sorry no bonus for you!")
