class A:
    def m1(self):
        print("This is a method of class A")
class B(A):
    def m1(self):
        print("This is a method of class B")
obj=B()
obj.m1()

#Super Keyword
class A:
    def m1(self):
        print("This is a method of class A")
class B(A):
    def m1(self):
        print("This is a method of class B")
        super.m1()
obj=B()
obj.m1()
