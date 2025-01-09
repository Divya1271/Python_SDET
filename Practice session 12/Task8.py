class Counter:
    count=0
    def m1(self):
        Counter.count+=1
        print(self.count)
a=Counter()
a.m1()
b=Counter()
b.m1()
c=Counter()
c.m1()