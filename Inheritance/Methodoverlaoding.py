# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("hello" +  name)
#         else:
#             print("Hello")
# h=Human()
# h.sayhello("Divya")
# h.sayhello()

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal=Calculation()
cal.add()
cal.add(10,20)
cal.add(10,20,70)