import array
from operator import index

arr=array.array('i',[1,2,3,4])

#Accessing elements
# print(arr[0])    #Output will be 1 here

#Modifying elements
arr[1]=10
print(arr)

#Adding elements
arr.append(6)
print(arr)

#Removing elements
arr.remove(10)
print(arr)

#Adding multiple elements
arr.extend([5,6])
print(arr)

#Inserting at specific index
arr.insert(2,20)
print(arr)

#Removing the element at specific index
arr.pop(1)
print(arr)

#Array slicing
print(arr[1:3])

#Returns the index of the element of an array
print(arr.index(4))

#buffer-info
print(arr.buffer_info())