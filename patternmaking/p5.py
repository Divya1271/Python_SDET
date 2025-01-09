n=5
for i in range(n):
    for j in range(0,n):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()