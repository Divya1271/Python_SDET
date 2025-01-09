class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def show(self):
        print(f"Make,model and year of different cars is {self.make},{self.model},{self.year}")
    def start_engine(self):
        print("Engine is starting")
c1=Car("Kia","Ax345",2015)
c2=Car("Nexon","Bcv678",2019)
c3=Car("Swift","Wch789",2017)
c1.show()
c2.show()
c3.show()