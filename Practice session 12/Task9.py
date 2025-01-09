class Book:
    def book_info(self,title,author="Unknown"):
        print(f"The title and author of the book is:{title},{author}")
b1=Book()
b1.book_info("The road not taken")
b1.book_info("The Ultimate choice","Collen Hoover")