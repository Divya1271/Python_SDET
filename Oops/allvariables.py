i,j=10,15   #Global variables

class Myclass:
    a,b=15,25
    def add(self,x,y):
        print(x,y)
        print(self.a+self.b)
        print(i,j)
m1=Myclass()
m1.add(11,13)