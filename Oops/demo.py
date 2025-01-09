class Myclass:

    def myfun(self):
        pass

    def display(self):
        print("Hello Python")

    def info(self,name,age):
        print("Hello",name,age)
#creation of objects
obj1=Myclass()
obj2=Myclass()

obj1.myfun()
obj1.display()
obj2.info("Divya",23)
obj2.myfun()
obj2.info("Mansi",24)