class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        area=self.length*self.breadth
        print(f"The area of rectangle is:{area}")
r=Rectangle(10,20)
r.area()
