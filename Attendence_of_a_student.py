total=int(input("Please enter the total number of classes held"))
attended=int(input("Please enter the total no of classes attended"))
percentage=((attended/total)*100)
print("Percentage of classes attended = ",percentage)
if percentage<75:
    print("Sorry! You are not allowed to sit in exams")
else:
    print("Yes you are allowed to sit in exams!")
