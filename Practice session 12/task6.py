class Calculator:
    def add(self,a,b):
        c=a+b
        print("Addition of two numbers is",c)
    @staticmethod
    def info():
            print("This is a calculator class")
c1=Calculator()
c1.add(10,20)
Calculator.info()
