class SchoolClass:
    def m1(self):
        print("I am the method of Student class")
class Student(SchoolClass):
    def m2(self):
        print("I am the method of student class")
class HighSchoolStudent(Student):
    def m3(self):
        print("I am the method of HighSchoolStudent")
obj=Student()
obj.m1()
obj.m2()
obj1=HighSchoolStudent()
obj1.m3()
obj1.m2()