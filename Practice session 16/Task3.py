class Animal:
    def make_sound(self):
        print("Sounds of different animal")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meoww")
class Cow(Animal):
    def make_sound(self):
        print("Murmur")
obj1=Dog()
obj2=Cat()
obj3=Cow()
obj1.make_sound()
obj2.make_sound()
obj3.make_sound()