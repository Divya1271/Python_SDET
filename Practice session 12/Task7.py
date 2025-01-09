class Employee:
    name=""
    salary=10000
    def basic_salary(self,name,salary):
       def update_salary(hike):
           update_salary=salary+(salary*(hike/100))
           return update_salary
       print("The modified salary is",update_salary)
e1=Employee()
e1.basic_salary("Dev",50000)