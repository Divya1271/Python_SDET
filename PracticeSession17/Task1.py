class Vehicle:
    def m1(self):
        print("This is the method of Vehicle class")
class Car(Vehicle):
    def m2(self):
        print("Hi i am the method of car class")
obj=Car()
obj.m2()
print(issubclass(Car,Vehicle))