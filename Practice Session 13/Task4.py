class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(name,marks)
    def update(self,increase):
        self.marks+=increase
        print(f"The modified values are {self.name} and {self.marks}")
s=Student("Divya",90)
s.update(5)
