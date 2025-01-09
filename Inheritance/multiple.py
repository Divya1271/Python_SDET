# class A:
#     def m1(self):
#         print("Hello method1")
# class B:
#     def m2(self):
#         print("Hello method2")
# class C(A,B):
#     def m3(self):
#         print("Hello method3")
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

#Example2
class A:
    def m1(self):
        print("Hello method1")
class B:
    def m1(self):
        print("Hello method2")
class C(A,B):
    def m3(self):
        print("Hello method3")
obj=C()
obj.m1()
obj.m3()

