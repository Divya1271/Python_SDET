class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
        print("The area of a circle is:",area)
    def circumference(self):
        circumference=2*3.14*self.radius
        print("The circumference of a circle is:",circumference)
c=Circle(4)
c.area()
c.circumference()