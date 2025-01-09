# s="Divya"
# r=s[::-1]
# if(r==s):
#     print("String is palindrome")
# else:
#     print("Not a palindrome")

s="madam"
print("Entered string is:",s)
r=""
for i in s:
    r=i+r
if(s==r):
    print("The string is palindrome")
else:
    print("The string is not a palindrome")