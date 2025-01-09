class Employee:
    def __init__(self,ename,esal):
        self.ename=ename
        self.esal=esal
        print(ename,esal)
    def __str__(self):
        return f"The employee name is:{self.ename} and salary is {self.esal}"
e=Employee("Divya",50000)
print(e)