from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        None
class Tiger(Animal):
    def eat(self):
        print("Eat non-veg")
class Cow(Tiger):
    def eat(self):
        print("Eat veg")    #overriding concept
obj=Cow()
obj.eat()