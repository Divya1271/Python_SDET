str=input("Which operation do you want to operate:")
strr=input("Enter operator:+,-,*,/ ")
n1=int(input("Enter the value of n1: "))
n2=int(input("Enter the value of n2: "))
str1="Addition"
str2="Subtraction"
str3="Multiplication"
str4="Division"
if(str==str1):
    n3=n1+n2
    print(n3)
elif(str==str2):
    n3=n2-n1
    print(n3)
elif(str==str3):
    n3=n1*n2
    print(n3)
elif(str==str4):
    n3=n1/n2
    print(n3)
else:
    print("Invalid Operation")


