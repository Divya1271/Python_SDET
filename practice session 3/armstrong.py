n=int(input("Enter the value of n"))
num=n
count=0
while(n!=0):
    n=n//10
    count=count+1
s=0
while(n>0):
    digit=n%10
    s=s+(digit**count)
    n//10
if(n==s):
    print("The number is an armstrong no")
else:
    print("The number is not an armstrong no")


