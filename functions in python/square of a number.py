# no=[1,2,3,4]
# sq=list(map(lambda x:x**2,no))
# print(sq)

# from functools import reduce
# z=reduce(lambda x,y:x+y,[1,2,4,5])
# print(z)

subjects=['English','Maths','Hindi','Science']
marks=[98,76,89,90]
a=zip(subjects,marks)
print(type(a))
res=list(a)
print(type(res))
print(res)