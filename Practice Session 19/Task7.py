class InvalidAgeError(Exception):
    def __init__(self,age):
        self.age=age
def acage(age):
    if(age<18):
        raise InvalidAgeError("You are not allowed to vote")
    else:
        print("You are allowed to vote")
try:
    age=int(input("Enter the age of a person:"))
    acage(age)
except Exception as e:
    print(e)
