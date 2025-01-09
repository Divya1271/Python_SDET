class PrivateExample:
    __pv="I am a private variable"
    def display(self):
        print(self.__pv)
obj=PrivateExample()
obj.display()
# print(self.__pv)

#Example2
class PublicExample:
    def __init__(self):
        puv="I am public variable"
        print(puv)
    def display(self):
        print("Hello")
obj=PublicExample()
# print(obj.puv)
obj.display()

#Example 3
class ProtectedExample:
    _a=10
    def m1(self):
        print("Hi")
class Subclass(ProtectedExample):
    def display(self):
        print("I am a method")
        print(self._a)
obj=Subclass()
obj.m1()
obj.display()

