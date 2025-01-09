from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,l,b,r):
        self.l=l
        self.b=b
        self.r=r
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        a=self.l*self.b
        print("Area of rectangle is:",a)
class Circle(Shape):
    def area(self):
       b=3.14*(self.r*self.r)
       print("Area of circle is:",b)
obj=Rectangle(5,6,7)
obj1=Circle(6,7,8)
obj.area()
obj1.area()

