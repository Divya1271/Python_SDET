class Transport:
    def move(self):
        print("Modes of transportation")
class Airplane(Transport):
    def move(self):
        print("It is airways")
class Ship(Transport):
    def move(self):
        print("It is waterways")
class Car(Transport):
    def move(self):
        print("It is roadways")
list=[Airplane(),Ship(),Car()]
for i in list:
    i.move()