class Vehicle:
    def display(self):
        print("We are dealing with different vehicles")
class Car(Vehicle):
    def print(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def show(self):
        print("Bike has 2 wheels")
obj=Car()
obj1=Bike()
obj.print()
obj.display()
obj1.show()
obj1.display()
obj1.print()    #invalid