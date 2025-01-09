import array
arr=array.array("i",[10,6,3,18,11])
def min_max(arr):
    min=float("inf")
    max=float("-inf")
    for i in arr:
        if(i<min):
          min=i
        if(i>max):
          max=i
    return min,max
print("The min and max in the given array elements is:",min_max(arr))

