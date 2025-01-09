def is_even(n):
    if(n%2==0):
        print("The no is even")
    else:
        print("Not even")
def is_prime(n):
    is_prime=True
    while(n!=0):
        if(n%2==0):
            is_prime=False
        if(is_prime==True):
            print("The no is prime")
        else:
            print("The no is not a prime number")