def duplicates(mylist):
    mylist2=[]
    for i in mylist:
        if i not in mylist2:
            mylist2.append(i)
    return mylist2
print(duplicates([1,2,3,4,1,4,6,7]))