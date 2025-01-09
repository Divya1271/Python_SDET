n=5
number=1
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(f"{number:2}",end=" ")
        number=number+1
    for l in range(i+1):
        print(f"{number:2}",end=" ")
        number=number+1
    print()
