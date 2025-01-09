num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(num1>0 and num2>0):
    print("Both numbers are positive")
elif(num1<0 and num2<0):
    print("Both numbers are negative")
elif(num1>0 and num2<0):
    print("Mixed Signs")


