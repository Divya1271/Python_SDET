n=int(input("Enter the number"))
factor = 2
print(f"Prime factors of {n} are:", end=" ")
while n > 1:
    if n % factor == 0:
       print(factor, end=" ")
       n //= factor
    else:
        factor += 1
