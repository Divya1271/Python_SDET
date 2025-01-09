class PrivateExample:
    __a=10
    def display(self):
        print(self.__a)
obj=PrivateExample()
obj.display()

class PublicExample:
    p=90
    def show(self):
        print("I can be accesed anywhere")
obj=PublicExample()
print(obj.p)
obj.show()

class ProtectedExample:
    _c=13
    def m1(self):
        print("Hello its a good day!")
class Subclass(ProtectedExample):
    def m2(self):
        print(self._c)
        print("This is a method of child class")
obj=Subclass()
obj.m1()
obj.m2()