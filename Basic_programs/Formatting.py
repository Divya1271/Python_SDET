#Example 1
name="Divya"
age=23
Rollno=101
print(name)
print(age)
print(Rollno)
#Example 2
name,age,Rollno="Divya",23,101
print("Name is",name)
print("Age is",age)
print("Rollno is",Rollno)
#Example 3
name,age,Rollno="Divya",23,101
print("Name is: %s" "Age is: %d" "Rollno is: %d" %(name,age,Rollno))
#Example 4
name,age,Rollno="Divya",23,101
print("Name is: {},Age is: {},Rollno is {}".format(name,age,Rollno))
#Example 5
name,age,Rollno="Divya",23,101
print(f"Name is: {name},Age is: {age},Rollno is: {Rollno}")