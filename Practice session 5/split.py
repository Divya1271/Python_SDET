s=input("Enter the string:")
r=s[::-1]
print(r)
words=s.split()
for i in words:
    r=i[::-1]            #reverses the string at their own places
    print(r,end=" ")