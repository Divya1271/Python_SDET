n=int(input("Enter the value of n"))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
