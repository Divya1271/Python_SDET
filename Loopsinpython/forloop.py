# for i in range(1,11):
#     print(i)
#
# #print 1 to 100
# for i in range(1,101):
#     print(i)
#
# #Sum of n natural numbers using for loop
# n=int(input("Enter the value of n"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("Sum of n natural numbers:",sum)
#
# #print even numbers from 1 to 20
# n=int(input("Enter the value of n"))
# for i in range(2,21,2):
#     print(i)
#
# #Factorial of a number
# n=int(input("Enter the value of n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("Factorial of a number is",fact)
#
# #Multiplication
# n=int(input("Enter the value of n"))
# for i in range(1,11):
#     print(f"{n}*{i}=",n*i)

#To check whether the number is prime or not
n=int(input("Enter the value of n"))
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime==True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")



