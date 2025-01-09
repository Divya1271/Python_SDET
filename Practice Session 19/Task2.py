n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))
try:
    print("Both the numbers are integers")
except ValueError as e:
    print(e)
