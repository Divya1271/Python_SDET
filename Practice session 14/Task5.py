class Laptop:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def specification(self):
        print(f"The name of the laptop is:{self.brand} and model is:{self.model}")
l1=Laptop("Asus","Axc567")
l2=Laptop("Hp","Crt678")
l1.specification()
l2.specification()
