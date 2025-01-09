class Book:
    def __init__(self,bname,bpublishedyear):
        self.bname=bname
        self.bpublishedyear=bpublishedyear
    def display(self):
        print(self.bname,self.bpublishedyear)
    def __str__(self):
        return self.bname
b=Book("The road not taken",1980)
b.display()
print(b)
