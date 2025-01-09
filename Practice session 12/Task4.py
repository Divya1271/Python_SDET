class Library:
    total_books=100
    def newnumber(self,increase):
        Library.total_books+=increase
        print("The updated no of books is",Library.total_books)
l1=Library()
l1.newnumber(10)
l1.newnumber(20)







