from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass
class B(A):
    def m1(self):
        print("I have a body now")
    def m2(self):
        print("Hello class B")
obj=B()
obj.m1()
obj.m2()
