# print("Hello,its a good day!")
# print("Good morning")
# try:
#     print(12/0)
# except Exception as e:
#     print(e)
# # except:
# #     print("The exception occured in the code")
# print("Arithmetic exception occured above")
#


#Example 2
# num1,num2=10,5
# try:
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Thrown zerodivision error exception")
# except FileNotFoundError:
#     print("FileNotFound error exception")
# except Exception as e:
#     print(e)
# else:
#     print("No exception found")
# finally:
#     print("Always execute")

#Example 3
# def enterage(num):
#     if num<0:
#         raise ValueError()
#     if num%2==0:
#         print("Age is even")
#     else:
#         print("Age is odd")
# num=-1
# try:
#     enterage(num)
# except ValueError:
#     print("This is exception in code")
#
# print("Program Terminated")

#Custom exceptions:We can define custom exception by creating a class

# class CustomError(Exception):
#     pass
# try:
#     raise CustomError("This is a custom error msg")
# except CustomError as e:
#     print(e)

class NegativeNumberError(Exception):
    def __init__(self,msg="Negative values are not allowed"):
        self.msg=msg
        super().__init__(self.msg)
def positive(num):
    if(num<0):
        raise NegativeNumberError("Give positive number")
    else:
        print(f"The number {num} is positive")
try:
    num=int(input("Enter the number:"))
    positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)