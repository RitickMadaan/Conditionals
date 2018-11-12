quantity=int(input("Please enter the quantity of your purchases"))
cost=quantity*100

if cost>1000:
    discount=0.1*cost
    cost=cost-discount
    print(cost)
else:
    print(cost)
