n=int(input("Enter the value of n"))
a=0
b=1
for i in range(n-2):
    c=a+b
    a=b
    b=c
    n=n-1
print(c)
