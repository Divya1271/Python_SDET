class Shopping_cart:
    def __init__(self):
        self.items=[]
    def additem(self,name,quantity):
        if name not in self.items:
            self.items.append(name)
            self.quantity=quantity
        elif name in self.items:
            self.quantity+=quantity
        print(self.items,self.quantity)
    def removeitem(self,name):
        if name in self.items:
            self.items.remove(name)
            self.quantity-=1
        print(self.items,self.quantity)
s=Shopping_cart()
s.additem("Hoodie",5)
s.additem("Sweater",1)
s.additem("Hoodie",2)
s.removeitem("Hoodie")




