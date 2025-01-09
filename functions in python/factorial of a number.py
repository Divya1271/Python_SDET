def fact(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i=i+1
        return(fact)
    print("The factorial of a number is",fact)
print(fact(5))