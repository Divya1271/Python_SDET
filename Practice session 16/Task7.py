class Shape:
    def draw(self):
        print("Drawing different shapes ")
class Square(Shape):
    def draw(self):
        print("Square is drawn")
class Triangle(Shape):
    def draw(self):
        print("Triangle is drawn")
class Circle(Shape):
    def draw(self):
        print("Circle is drawn")
List=[Square(),Triangle(),Circle()]
for i in List:
    i.draw()
    