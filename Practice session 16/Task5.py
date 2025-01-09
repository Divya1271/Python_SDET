class Animal:
    def play_sound(self):
        print("Animals sounds")
class Dog(Animal):
    def make_sound(self):
        print("DOgs bark")
class Cat(Animal):
    def make_sound(self):
        print("Cats meow")
c=Cat()
c.play_sound()
c.make_sound()