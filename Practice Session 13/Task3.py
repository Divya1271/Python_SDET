class Car:
    def __init__(self,cbrand,cmodel):
        self.cbrand=cbrand
        self.cmodel=cmodel
    def display(self):
        print(self.cbrand,self.cmodel)
    def __str__(self):
        return f"Cbrand is :{self.cbrand} and Cmodel is :{self.cmodel}"
c=Car("Tata","Nexon")
c.display()
print(c)
del c.cbrand
print(c)
