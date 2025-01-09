class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"The person's information is :{self.name},{self.age}")
p1=Person("Rohan",23)
p2=Person("Rohit",24)
p1.show()
p2.show()