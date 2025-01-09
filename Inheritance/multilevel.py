class A:
    x,y=100,200
    def __init__(self):
        print("Hello i am constructor")
    def m1(self):
        print(self.x+self.y)
class B(A):
    p,q=10,20
    def __init(self):
        print("I am constructor of class B")
    def m2(self):
        print(self.p+self.q)
class C(B):
    def __init__(self):
        m,n=12,13
        print("This is the constructor of class C")
    def m3(self):
        print(self.m+self.n)
obj=C
obj.m1()
obj.m2()
obj.m3()
