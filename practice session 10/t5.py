def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
    print()
    return pattern
print(pattern(5))