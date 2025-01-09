num1=int(input("Enter the value for first number:"))
num2=int(input("Enter the value for second number:"))
try:
    ans=num1/num2
    print(ans)
except Exception as e:
    print(e)