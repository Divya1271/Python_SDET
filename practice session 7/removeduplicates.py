list1=[1,2,3,4,2,2]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# list=[1,2,3,4,4,6,7]
#
# i=0
# while(i<len(list)):
#     j=i+1
#     while(j<len(list)):
#         if list[i]==list[j]:
#             list.pop(j)
#         else:
#             j=j+1
#     i=i+1
#
# print(list)
