class Library:
    def __init__(self):
        self.noOfBooks=0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.noOfBooks=len(self.books)

    def show(self):
        print(f"Library has {self.noOfBooks} Books")
        print(f"Books are:\n{self.books}")
lists=['A','B','C','D','E','F','G','H','I','K','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l1=Library()
l1.addBook("HK DASS")
for li in lists:
    l1.addBook(li)
l1.show()