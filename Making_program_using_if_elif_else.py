number = input("Enter the number you want to check ")
if (int(number)%2!=0) or (int(number)==0) or (int(number)==1):
    print("Weird")
else:
    if (int(number)>=2) and (int(number)<=5):
        print("Not Weird")
    elif (int(number)>=6) and (int(number)<=20):
        print("Weird")
    else:
        print("Not Weird")
