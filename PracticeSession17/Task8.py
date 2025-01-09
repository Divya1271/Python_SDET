class Animal:
    def display(self):
        print("Animals live in jungle")
class Dog(Animal):
    def show(self):
        print("Dogs bark")
obj=Dog()
obj.show()
print(isinstance(obj,Dog))