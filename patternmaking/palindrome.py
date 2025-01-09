n=int(input("Enter the value of n"))
num=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(num==rev):
    print("The number is palindrome")
else:
    print("The number is not a palindrome")