first=int(input("First person please enter your age"))
second=int(input("Second person please enter your age"))
third=int(input("Third person please enter your age"))
if (first>second) and (first>third):
    oldest=first
    print("Oldest = First")
    if (second>third):
        print("Youngest = Third")
    else:
        print("Youngest = Second")
elif (second>first) and (second>third):
    oldest=second
    print("Oldest = Second")
    if(first>third):
        print("Youngest = Third")
    else:
        print("Youngest = First")
else:
    oldest=third
    print ("Oldest = Third")
    if(first>second):
        print("Youngest = Second")
    else:
        print("Youngest = First")
