import array
n=int(input("Enter the no of rotations:"))
arr=array.array('i',[11,23,12,4,1])
print(arr[n:6]+arr[0:n])