start=int(input("Enter the starting number of the range:"))
end=int(input("Enter the ending number of the range:"))
list=[]
is_prime=True
for i in range(start,end):
    if(start%i==0):
        is_prime=False
if(is_prime==True):
    list.append(start)
print(list)


