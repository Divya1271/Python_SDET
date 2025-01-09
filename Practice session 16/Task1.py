class Vehicle:
    brand="Tata"
    model="Axc678"
    def show(self):
        print(self.brand,self.model)
class Car(Vehicle):
    num_doors=4
    def display(self):
        print(self.num_doors)
c=Car()
c.show()
c.display()
