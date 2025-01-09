class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,employee_id,salary):
        self.employee_id=employee_id
        self.salary=salary
    def show(self):
        print(self.employee_id,self.salary)
p=Person("Ram",30)
p.show()
e=Employee(101,60000)
e.show()
