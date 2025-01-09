class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if new_age>0:
            self.__age=new_age
        else:
            print("Age cannot be negative")
s=Student("Divya",24)
print(s.name)
print(s.age)
s.name="Ram"
print(s.name)
s.age=34
print(s.age)