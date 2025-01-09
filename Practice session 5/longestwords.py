s=input("Enter the string")
w=s.split()
max=0
for i in w:
    if(len(i)>max):
        max=len(i)
print(max)




