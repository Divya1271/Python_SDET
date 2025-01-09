def min_max(mylist):
    # list2 = []
    min = float('inf')
    max = float('-inf')
    for i in mylist:
        if i < min:
            min = i
            # list2.append(min)

        if i > max:
            max = i
            # list2.append(max)
    return min,max
    

listnew = [1, 2, 3, 4, 5]
print(min_max(listnew))
