from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def a1(self):
        pass
class Child(Parent):
    def a1(self):
        print("Hello its a python session")
    def a2(self):
        print("We are learning python")
obj=Child()
obj.a1()
obj.a2()
obj1=Parent()


