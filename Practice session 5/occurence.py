s=input("Enter the string")
mydic={}
for i in s:
    if i in mydic:
        mydic[i]+=1
    else:
        mydic[i]=1
print(mydic)
