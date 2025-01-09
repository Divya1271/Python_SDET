class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        rarea=self.l*self.b
        print("Area of Rectangle is",rarea)
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        carea=3.14*self.r*self.r
        print("Area of Circle is",carea)
r1=Rectangle(5,6)
r1.area()
c1=Circle(6)
c1.area()

