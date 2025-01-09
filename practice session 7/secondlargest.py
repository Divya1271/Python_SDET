list1=[1,23,45,67,19]
second=largest=0
for i in list1:
    if(i>largest):
        second=largest
        largest=i
    elif(i>second and i!=largest):
        second=i
print("The second largest element is:",second)


