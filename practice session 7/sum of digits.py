n=int(input("Enter the value of n:"))
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("The sum of digits is:",sum)