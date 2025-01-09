n=5
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    #print()
#for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(0,n-i):
        print("*",end=" ")

    for j in range(i,n-1):
        print("*",end=" ")
    print()