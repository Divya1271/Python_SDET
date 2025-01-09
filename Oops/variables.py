#global
#Local
#Instance

class Myclass:
    a,b=10,20

    def add(self):
        #print(a,b)    #this will generate an error
        print(self.a+self.b)

mc1=Myclass()
mc1.add()