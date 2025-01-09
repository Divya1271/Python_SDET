import sys
sys.path.append(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\module and packages\PackA")
sys.path.append(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\module and packages\PackB")
#Approach1
# import emp as e
# import std as s
#
# e1=e.Employee()
# e1.disemp("Divya",101)
# s1=s.Student()
# s1.disstd("Mansi",23)


#Approach2
# import emp
# import std
# e=emp.Employee()
# e.disemp("Anjali",102)
# s=std.Student()
# s.disstd("Ritika",21)

#Approach3
from emp import *
from std import *

e1=Employee()
e1.disemp("Ram",103)
s1=Student()
s1.disstd("Sham",24)


