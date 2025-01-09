from operator import index

mylist=[1,2,3,2,5]
# num=int(input("Enter the num"))
result=[]
count=0
r=2
for i in range(len(mylist)):
    if(mylist[i]==r):
        result.append(i)
        count+=1
print(result)
print(count)


