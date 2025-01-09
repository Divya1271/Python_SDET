n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
while (n2 != 0):
    n1, n2 = n2, n1 % n2
print(n1)
