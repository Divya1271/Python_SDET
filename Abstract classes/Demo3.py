from abc import ABC,abstractmethod

class Shape(ABC):                 #It's better to create the constructor in base class to avoid duplication
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
    def __init__(self,l,b):
        self.l=l
        self.b=b
class Rectangle(Shape):
    # def __init__(self,l,b):
    #     self.l=l
    #     self.b=b
    def area(self):
            area=self.l*self.b
            print("Area is:",area)
    def perimeter(self):
            perimeter=2*(self.l+self.b)
            print("Perimeter is:",perimeter)
obj=Rectangle(10,20)
obj.area()
obj.perimeter()