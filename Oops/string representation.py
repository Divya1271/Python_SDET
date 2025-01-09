# class Myclass:
#     def __str__(self):
#         return "Hello i am method"
# obj=Myclass()
# print(obj)
#

#Example2
class Employee:
    def __init__(self,name,sal):
        self.ename=name
        self.esal=sal

    def display(self):
        print(self.ename,self.esal)
    def __str__(self):
        return self.ename
obj=Employee("Divya",50000)
obj.display()
print(obj)
