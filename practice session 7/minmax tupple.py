mytupple=tuple(map(int,input("Enter the tupple:").split(",")))
min=max=mytupple[0]
for i in mytupple:
    if(i<min):
        min=i
    if(i>max):
        max=i
print(min,max)