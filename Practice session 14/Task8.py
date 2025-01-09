class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def set_discount(self,discount):
        newprice=self.price-(self.price-(discount))
        print(newprice)
p1=Product("Sweater",1000)
p2=Product("Jacket",1200)
p1.set_discount(0.5)
p2.set_discount(0.5)