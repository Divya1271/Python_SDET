marks1=int(input("Enter the marks in maths"))
marks2=int(input("Enter the marks in science"))
avg=((marks1+marks2))/2
if((marks1>80 and marks2>70) or (avg>=75)):
    print("You are eligible for admission")
else:
    print("You are not eligible")