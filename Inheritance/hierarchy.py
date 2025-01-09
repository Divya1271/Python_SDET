class A:
    a,b=10,20
    def m1(self):
        print(self.a+self.b)
class B(A):
    c,d=100,200
    def m2(self):
        print(self.c+self.d)
class D(A):
    e,f=30,40
    def m3(self):
        print(self.e+self.f)
obj1=B()
obj1.m2()
obj2=D()
obj2.m3()
obj1.m1()
