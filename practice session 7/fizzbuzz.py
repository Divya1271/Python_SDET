n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("Fizzbuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)
