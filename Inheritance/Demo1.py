# class A:
#     def __init__(self):
#         print("I am constructor")
#     def m1(self):
#         print("Hi i am method of class A")
# class B(A):
#     def __init__(self):
#         print("I am constructor of class B")
#     def m2(self):
#         print("I am method of class B")
# Bobj=B()
# Bobj.m2()
# Bobj.m1()

#Example2

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
    def m2(self):
        print("Hello")
obj=A()
obj.m1()
obj.m2()