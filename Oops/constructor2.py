class Myclass:
    def __init__(self):
        print("I am a constructor of the class")
    def m1(self):
        print("This is the method of the class")
        print(self)
    def m2(self,a,b):
        return (a+b)
obj=Myclass()
obj.m1()
print(obj.m2(10,20))