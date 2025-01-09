myset={12,13,11,5,7}
# list1=list(myset)
# min=max=list1[0]
min=float('inf')
max=float('-inf')
for i in myset:
    if(i<min):
        min=i
    if(i>max):
        max=i
print(min,max)
# list1.remove(min)
# list1.remove(max)
# set2=set(list1)
# print(set2)
myset.remove(min)
myset.remove(max)
print(myset)


