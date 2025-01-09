class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f" brand: {self.brand},model:{self.model}"

c=Car("Tata","Nexon")
print(c)
del c.brand
print(c)
