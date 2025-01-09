from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass
class FullTimeEmployee(Employee):
    def get_salary(self):
        print("I am a fulltime employee")
class PartTimeEmployee(Employee):
    def get_salary(self):
        print("I am a parttime employee")
obj1=FullTimeEmployee()
obj1.get_salary()
obj2=PartTimeEmployee()
obj2.get_salary()