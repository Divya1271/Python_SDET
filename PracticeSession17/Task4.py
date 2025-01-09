class Product:
    def __init__(self,price,stock):
        self.__price=price
        self.__stock=stock

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price):
        if(new_price>0):
            self.__price=new_price
        else:
            print("Price cannot be negative")
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,new_stock):
        if(new_stock>0):
            self.__stock=new_stock
        else:
            print("Stock cannot be negative")
p=Product(30000,150)
# print(p.price)
# print(p.stock)
p.price=20000
print(p.price)
p.stock=250
print(p.stock)
