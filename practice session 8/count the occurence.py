mylist=[1,2,3,4,1,2]
count=0
mylist2=[]
for i in mylist:
    if i not in mylist2:
        mylist2.append(i)
        count=count+1
print(mylist2)

