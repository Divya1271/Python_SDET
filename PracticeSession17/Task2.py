class Person:
    def m1(self):
        print("I am a good person")
class Employee(Person):
    def m2(self):
        print("You belong to CA department")
obj=Employee()
obj.m1()
obj.m2()