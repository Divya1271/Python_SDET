# 1 to 10
i=1
while (i<=10):
    print(i)
    i=i+1
print("Done")

#10 to 1
i=10
while (i>=1):
    print(i)
    i-=1
print("Done")

# 1 to 100
i=1
while (i<=100):
    print(i)
    i+=1
print("Done")

#Sum of first N natural numbers
n=int(input("Enter the value of n"))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)
print("Done")

#Factorial of a number
n=int(input("Enter the value of n"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("Factorial of a number",fact)

#Reverse of a number
n=int(input("Enter the value of n"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of the number",rev)

#Count the number of digits
n=int(input("Enter the number"))
count=0
while(n!=0):
    n=n//10
    count=count+1
print(count)




