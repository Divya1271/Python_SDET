class Myclass():

    def m1(self):
        print("This is an instance method")

    @staticmethod
    def m2(num):
        print(num)
mc=Myclass()
mc.m1()
# mc.m2(10)
Myclass.m2(20)