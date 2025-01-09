# def greet(*name):
#     print("Hello",{name})
#
# greet("David")
# greet("David","john","Marry","Bob")

# def student_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#
# student_info(name="Divya",age=23)

# def display_info(*args,**kwargs):
#     print("positional arguments",args)
#     print("Keyword arguments",kwargs)
# display_info(1,2,3,name="Divya",age=23,city="kaithal")

# def greet(name,*args):
#     print(name,args)
#
# greet("John","Divya",23,"Kaithal")

def greet(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f"{i} {j}")
greet(300,"Merry","Dvaid","John",34)

