import random
r=random.randint(1,10)
count=0
while(True):
    n=int(input("Enter the value of your own choice"))
    count=count+1
    if(n>r):
       print("The number you entered is high")
    elif(n<r):
       print("The number you entered is low")
    else:
        print("You entered the same....Won!")
        print("The numbers of attempts are",count)
        break
