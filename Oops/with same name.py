i,j=11,12
class Myclass:
    i,j=10,20
    def add(self,i,j):
        print(i,j)
        print(self.i+self.j)
        print(globals()['i'],globals()['j'])

    def display(self,num):
        print(num)

mc=Myclass()
mc.add(100,200)
mc.display(3)

