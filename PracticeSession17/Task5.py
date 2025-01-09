class A:
    def m1(self):
        print("I am method 1")
class B(A):
    def m2(self):
        print("I am method 2")
        super().m1()
obj=B()
obj.m2()
obj.m1()