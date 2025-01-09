s=input("Enter the string you want to enter:")
l=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in s:
    if i in l:
        count+=1
print("The no of vowels in the entered string are:",count)