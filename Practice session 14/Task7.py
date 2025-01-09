class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def give_raise(self,percent):
        newsal=self.salary+(self.salary*(percent/100))
        print(newsal)
e=Employee(101,"Ram",70000)
e.give_raise(10)
